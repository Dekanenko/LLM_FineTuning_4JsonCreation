from langchain_openai import ChatOpenAI
from langchain.prompts import StringPromptTemplate
from langchain_core.output_parsers.string import StrOutputParser
from langchain.output_parsers import PydanticOutputParser
from langchain_core.exceptions import OutputParserException

from pydantic import BaseModel
from loguru import logger
from langchain.llms.base import LLM

from src.prompts import BasePair

from dotenv import load_dotenv

load_dotenv()


async def _text_generation(
    prompt: StringPromptTemplate,
    text_gen_llm: LLM = ChatOpenAI(
        model="gpt-4o-mini", temperature=1.1, max_tokens=1024
    ),
):
    text_gen_chain = prompt | text_gen_llm | StrOutputParser()

    response = await text_gen_chain.ainvoke({})
    return response


async def _json_generation(
    prompt: StringPromptTemplate,
    pydantic_object: BaseModel,
    input_text: str | None = None,
    errors: list[str] | None = None,
    retry_num: int = 1,
    json_gen_llm: LLM = ChatOpenAI(
        model="gpt-4o-mini", temperature=0.7, max_tokens=2048
    ),
):
    json_gen_chain = prompt | json_gen_llm | StrOutputParser()
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
        # logger.debug(f"Error occured: \n{e}\nRetry num:{retry_num}")
        if retry_num == 0:
            # logger.warning(f"Cannot parse the string, last error:\n{e}")
            return None

        if errors:
            errors.append(str(e))
        else:
            errors = [str(e)]

        return await _json_generation(
            prompt=prompt,
            input_text=input_text,
            pydantic_object=pydantic_object,
            errors=errors,
            retry_num=retry_num - 1,
            json_gen_llm=json_gen_llm,
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
    text_gen_llm: LLM = ChatOpenAI(
        model="gpt-4o-mini", temperature=1.1, max_tokens=1024
    ),
    json_gen_llm: LLM = ChatOpenAI(
        model="gpt-4o-mini", temperature=0.7, max_tokens=2048
    ),
):
    data_samples = []
    errors = 0
    for _ in range(sample_num):
        generated_text = ""
        if pair.text_generation_prompt:
            generated_text = await _text_generation(
                prompt=pair.text_generation_prompt,
                text_gen_llm=text_gen_llm,
            )

        data_sample = await _json_generation(
            prompt=pair.json_generation_prompt,
            pydantic_object=pair.model,
            input_text=generated_text,
            json_gen_llm=json_gen_llm,
        )

        if data_sample:
            data_samples.append(data_sample)
        else:
            errors += 1

    return data_samples, errors
