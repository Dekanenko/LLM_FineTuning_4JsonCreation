from langchain_openai import ChatOpenAI
from langchain.prompts import StringPromptTemplate
from langchain_core.output_parsers.string import StrOutputParser
from langchain.output_parsers import PydanticOutputParser
from langchain_core.exceptions import OutputParserException

from pydantic import BaseModel
from loguru import logger

from src.prompts import BasePair


async def _text_generation(
    prompt: StringPromptTemplate,
    text_gen_model: str = "gpt-4o-mini",
    text_gen_temperature: float = 1.3,
):
    llm = ChatOpenAI(
        model=text_gen_model, temperature=text_gen_temperature, max_tokens=4096
    )
    text_gen_chain = prompt | llm | StrOutputParser()

    response = await text_gen_chain.ainvoke({})
    return response


async def _json_generation(
    prompt: StringPromptTemplate,
    pydantic_object: BaseModel,
    input_text: str | None = None,
    errors: list[str] | None = None,
    retry_num: int = 2,
    json_gen_model: str = "gpt-4o-mini",
    json_gen_temperature: float = 0.7,
):
    llm = ChatOpenAI(
        model=json_gen_model, temperature=json_gen_temperature, max_tokens=4096
    )
    json_gen_chain = prompt | llm | StrOutputParser()
    parser = PydanticOutputParser(pydantic_object=pydantic_object)

    try:
        response = await json_gen_chain.ainvoke(
            {
                "input_text": input_text,
                "format_instructions": parser.get_format_instructions(),
                "errors": errors,
            }
        )
        parser.parse(response)
    except OutputParserException as e:
        logger.debug(f"Error occured: \n{e}\nRetry num:{retry_num}")
        if retry_num == 0:
            logger.warning(f"Cannot parse the string, last error:\n{e}")
            return None

        if errors:
            errors.append(str(e))
        else:
            errors = [str(e)]

        return await _json_generation(
            prompt=prompt,
            pydantic_object=pydantic_object,
            errors=errors,
            retry_num=retry_num - 1,
            json_gen_model=json_gen_model,
            json_gen_temperature=json_gen_temperature,
        )

    prompt_text = prompt.format(
        input_text=input_text,
        format_instructions=parser.get_format_instructions(),
        errors=errors,
    )

    return {"input": prompt_text, "output": response}


async def generate(
    pair: BasePair,
    sample_num: int = 1,
):
    data_samples = []
    for _ in range(sample_num):
        generated_text = ""
        if pair.text_generation_prompt:
            generated_text = await _text_generation(pair.text_generation_prompt)

        data_sample = await _json_generation(
            prompt=pair.json_generation_prompt,
            pydantic_object=pair.model,
            input_text=generated_text,
        )

        if data_sample:
            data_samples.append(data_sample)

    return data_samples
