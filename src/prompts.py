from pydantic import BaseModel
from langchain.prompts import StringPromptTemplate

from src.models import *


class BasePair(BaseModel):
    model: BaseModel = None
    text_generation_prompt: StringPromptTemplate = None
    json_generation_prompt: StringPromptTemplate = None


class CharacterNamesPair(BasePair):
    class TextGenerationPrompt(StringPromptTemplate):
        template = "Generate a small text (no more than 200 words) including characters with their names and surnames."

        def format(self):
            return self.template

    class JsonGenerationPrompt(StringPromptTemplate):
        template = (
            "You are a name and surname extractor. Your task is to identify and extract the names and surnames of characters from the given text.\n"
            "### Input:\n{input_text}\n\n"
            "### Instructions:\n"
            "1. Extract characters' names and surnames clearly.\n"
            "2. Ensure that the JSON file contains a list of unique name-surname pairs (no duplicates).\n\n"
            "### Format Instructions:\n"
            "1. Do NOT include headers, comments, or any additional text—only generate the JSON file.\n"
            "2. Strictly adhere to the following JSON format:\n"
            "{format_instructions}\n"
            "{error_description}\n"
            "### Generated JSON file:\n"
        )

        def format(
            self,
            input_text: str,
            format_instructions: str,
            errors: list[str] | None = None,
        ):
            error_description = ""

            if errors:
                error_description = (
                    "Previously encountered errors:\n"
                    + "\n".join(error for error in errors)
                    + "\nMake sure to fix them and provide correct output.\n\n"
                )

            prompt = self.template.format(
                input_text=input_text,
                format_instructions=format_instructions,
                error_description=error_description,
            )

            return prompt

    def __init__(self):
        super().__init__()
        self.model = CharacterNames
        self.text_generation_prompt = self.TextGenerationPrompt(input_variables=[])
        self.json_generation_prompt = self.JsonGenerationPrompt(input_variables=[])


class FictionalCharacterPair(BasePair):
    class JsonGenerationPrompt(StringPromptTemplate):
        template = (
            "You are a creator of fictional characters. Your task is to create a unique character for the game.\n"
            "### Instructions:\n"
            "1. Character must be unique and have engaging properties and story.\n"
            "2. You must keep the biography concise, no more than 60 words."
            "2. Provide information about character's attack, skill and ultimate concisely, no more than 30 words each.\n"
            "3. Be very creative and do not hesitate creating complex characters.\n"
            "### Format Instructions:\n"
            "1. Do NOT include headers, comments, or any additional text—only generate the JSON file.\n"
            "2. Strictly adhere to the following JSON format:\n"
            "{format_instructions}\n"
            "{error_description}\n"
            "### Generated JSON file:\n"
        )

        def format(
            self,
            input_text: str,
            format_instructions: str,
            errors: list[str] | None = None,
        ):
            error_description = ""

            if errors:
                error_description = (
                    "Previously encountered errors:\n"
                    + "\n".join(error for error in errors)
                    + "\nMake sure to fix them and provide correct output.\n\n"
                )

            prompt = self.template.format(
                format_instructions=format_instructions,
                error_description=error_description,
            )

            return prompt

    def __init__(self):
        super().__init__()
        self.model = FictionalCharacter
        self.json_generation_prompt = self.JsonGenerationPrompt(input_variables=[])


class TShirtOrderPair(BasePair):
    class TextGenerationPrompt(StringPromptTemplate):
        template = "Generate a small text (no more than 50 words) making an order for a t-shirt. Describe the desired t-shirt in vivid details."

        def format(self):
            return self.template

    class JsonGenerationPrompt(StringPromptTemplate):
        template = (
            "You are a t-shirt order extractor. Your task is to identify and extract the t-shirt order details from the given text.\n"
            "### Input:\n{input_text}\n\n"
            "### Instructions:\n"
            "1. Extract t-shirt order details including type, size, color, quantity, and gender.\n"
            "2. If specific details are not mentioned, use the default values.\n\n"
            "### Format Instructions:\n"
            "1. Do NOT include headers, comments, or any additional text—only generate the JSON file.\n"
            "2. Strictly adhere to the following JSON format:\n"
            "{format_instructions}\n"
            "{error_description}\n"
            "### Generated JSON file:\n"
        )

        def format(
            self,
            input_text: str,
            format_instructions: str,
            errors: list[str] | None = None,
        ):
            error_description = ""

            if errors:
                error_description = (
                    "Previously encountered errors:\n"
                    + "\n".join(error for error in errors)
                    + "\nMake sure to fix them and provide correct output.\n\n"
                )

            prompt = self.template.format(
                input_text=input_text,
                format_instructions=format_instructions,
                error_description=error_description,
            )

            return prompt

    def __init__(self):
        super().__init__()
        self.model = TShirtOrder
        self.text_generation_prompt = self.TextGenerationPrompt(input_variables=[])
        self.json_generation_prompt = self.JsonGenerationPrompt(input_variables=[])


class FilmIdeaPair(BasePair):
    class JsonGenerationPrompt(StringPromptTemplate):
        template = (
            "You are a visionary film creator known for generating unique, thought-provoking movie concepts. Create an original film idea that challenges conventions and captivates audiences.\n"
            "### Instructions:\n"
            "1. Create a bold, innovative concept that hasn't been seen before in cinema.\n"
            "2. Develop 2-5 complex characters with compelling motivations and internal conflicts.\n"
            "3. The plot should feature unexpected twists and meaningful themes.\n"
            "4. The setting should be vivid and contribute to the story's atmosphere.\n"
            "5. Consider unique style elements (e.g., narrative structure, visual approach).\n"
            "6. The tone should be consistent and serve the story's purpose.\n"
            "7. Ensure the budget is realistic for the scope of the film.\n\n"
            "### Format Instructions:\n"
            "1. Do NOT include headers, comments, or any additional text—only generate the JSON file.\n"
            "2. Strictly adhere to the following JSON format:\n"
            "{format_instructions}\n"
            "{error_description}\n"
            "### Generated JSON file:\n"
        )

        def format(
            self,
            input_text: str,
            format_instructions: str,
            errors: list[str] | None = None,
        ):
            error_description = ""

            if errors:
                error_description = (
                    "Previously encountered errors:\n"
                    + "\n".join(error for error in errors)
                    + "\nMake sure to fix them and provide correct output.\n\n"
                )

            prompt = self.template.format(
                format_instructions=format_instructions,
                error_description=error_description,
            )

            return prompt

    def __init__(self):
        super().__init__()
        self.model = FilmIdea
        self.json_generation_prompt = self.JsonGenerationPrompt(input_variables=[])


class ItineraryPair(BasePair):
    class JsonGenerationPrompt(StringPromptTemplate):
        template = (
            "You are a travel itinerary planner. Create a detailed travel itinerary that maximizes the traveler's experience.\n"
            "### Instructions:\n"
            "1. Plan activities that are logistically feasible and time-appropriate.\n"
            "2. Include specific start and end times for each activity.\n"
            "3. Consider travel time between locations.\n"
            "4. Include various modes of transportation when needed.\n"
            "5. Be realistic with timing and costs.\n"
            "6. Ensure activities are appropriate for the destination.\n\n"
            "### Format Instructions:\n"
            "1. Do NOT include headers, comments, or any additional text—only generate the JSON file.\n"
            "2. Strictly adhere to the following JSON format:\n"
            "{format_instructions}\n"
            "{error_description}\n"
            "### Generated JSON file:\n"
        )

        def format(
            self,
            input_text: str,
            format_instructions: str,
            errors: list[str] | None = None,
        ):
            error_description = ""

            if errors:
                error_description = (
                    "Previously encountered errors:\n"
                    + "\n".join(error for error in errors)
                    + "\nMake sure to fix them and provide correct output.\n\n"
                )

            prompt = self.template.format(
                format_instructions=format_instructions,
                error_description=error_description,
            )

            return prompt

    def __init__(self):
        super().__init__()
        self.model = Itinerary
        self.json_generation_prompt = self.JsonGenerationPrompt(input_variables=[])


class RecipePair(BasePair):
    class JsonGenerationPrompt(StringPromptTemplate):
        template = (
            "You are a professional chef creating detailed recipes. Create a complete recipe with precise measurements and clear instructions.\n"
            "### Instructions:\n"
            "1. Provide a clear, descriptive title for the recipe.\n"
            "2. List all ingredients with exact quantities and units.\n"
            "3. Write step-by-step cooking instructions in a logical order.\n"
            "4. Include total cooking time in minutes.\n"
            "5. Specify the cuisine type.\n"
            "6. Include nutrition facts when possible (calories, protein, fat, carbs).\n\n"
            "### Format Instructions:\n"
            "1. Do NOT include headers, comments, or any additional text—only generate the JSON file.\n"
            "2. Strictly adhere to the following JSON format:\n"
            "{format_instructions}\n"
            "{error_description}\n"
            "### Generated JSON file:\n"
        )

        def format(
            self,
            input_text: str,
            format_instructions: str,
            errors: list[str] | None = None,
        ):
            error_description = ""

            if errors:
                error_description = (
                    "Previously encountered errors:\n"
                    + "\n".join(error for error in errors)
                    + "\nMake sure to fix them and provide correct output.\n\n"
                )

            prompt = self.template.format(
                format_instructions=format_instructions,
                error_description=error_description,
            )

            return prompt

    def __init__(self):
        super().__init__()
        self.model = Recipe
        self.json_generation_prompt = self.JsonGenerationPrompt(input_variables=[])


class EventPair(BasePair):
    class TextGenerationPrompt(StringPromptTemplate):
        template = "Generate a text (no more than 100 words) where different people (they must be named) describe their event. Mention the date, time, location and the people attending."

        def format(self):
            return self.template

    class JsonGenerationPrompt(StringPromptTemplate):
        template = (
            "You are an event details extractor. Your task is to identify and extract event information from the given text.\n"
            "### Input:\n{input_text}\n\n"
            "### Instructions:\n"
            "1. Extract the event title, date, start time, end time, and location.\n"
            "2. Identify all attendees mentioned in the text, including their names and email addresses.\n"
            "3. For each attendee, set has_confirmed to true if their attendance is confirmed, false otherwise.\n\n"
            "### Format Instructions:\n"
            "1. Do NOT include headers, comments, or any additional text—only generate the JSON file.\n"
            "2. Strictly adhere to the following JSON format:\n"
            "{format_instructions}\n"
            "{error_description}\n"
            "### Generated JSON file:\n"
        )

        def format(
            self,
            input_text: str,
            format_instructions: str,
            errors: list[str] | None = None,
        ):
            error_description = ""

            if errors:
                error_description = (
                    "Previously encountered errors:\n"
                    + "\n".join(error for error in errors)
                    + "\nMake sure to fix them and provide correct output.\n\n"
                )

            prompt = self.template.format(
                input_text=input_text,
                format_instructions=format_instructions,
                error_description=error_description,
            )

            return prompt

    def __init__(self):
        super().__init__()
        self.model = Events
        self.text_generation_prompt = self.TextGenerationPrompt(input_variables=[])
        self.json_generation_prompt = self.JsonGenerationPrompt(input_variables=[])


class ResumePair(BasePair):
    class TextGenerationPrompt(StringPromptTemplate):
        template = "Generate one resume (no more than 100 words) outlining the following information: full name, email, phone number, education, work experience, skills. Make it unique and creative."

        def format(self):
            return self.template

    class JsonGenerationPrompt(StringPromptTemplate):
        template = (
            "You are a resume information extractor. Your task is to identify and extract resume details from the given text.\n"
            "### Input:\n{input_text}\n\n"
            "### Instructions:\n"
            "1. Extract the person's full name, email, and phone number if provided.\n"
            "2. Identify all education entries, including institution, degree, and graduation year.\n"
            "3. Extract work experience details, including company, role, and years.\n"
            "4. List all mentioned skills.\n\n"
            "### Format Instructions:\n"
            "1. Do NOT include headers, comments, or any additional text—only generate the JSON file.\n"
            "2. Strictly adhere to the following JSON format:\n"
            "{format_instructions}\n"
            "{error_description}\n"
            "### Generated JSON file:\n"
        )

        def format(
            self,
            input_text: str,
            format_instructions: str,
            errors: list[str] | None = None,
        ):
            error_description = ""

            if errors:
                error_description = (
                    "Previously encountered errors:\n"
                    + "\n".join(error for error in errors)
                    + "\nMake sure to fix them and provide correct output.\n\n"
                )

            prompt = self.template.format(
                input_text=input_text,
                format_instructions=format_instructions,
                error_description=error_description,
            )

            return prompt

    def __init__(self):
        super().__init__()
        self.model = Resume
        self.text_generation_prompt = self.TextGenerationPrompt(input_variables=[])
        self.json_generation_prompt = self.JsonGenerationPrompt(input_variables=[])


class GameArtifactPair(BasePair):
    class JsonGenerationPrompt(StringPromptTemplate):
        template = (
            "You are a legendary artificer crafting unique magical items and artifacts. Create an extraordinary artifact for a fantasy game world.\n"
            "### Instructions:\n"
            "1. Create a powerful and unique artifact with an intriguing name and compelling description.\n"
            "2. Define its location in a way that ties into the artifact's lore.\n"
            "3. Design meaningful buffs that enhance the wielder's capabilities.\n"
            "4. Balance the artifact with interesting defuffs or drawbacks.\n"
            "5. Consider the artifact's type (weapon, armor, accessory, etc.) and its rarity level.\n"
            "6. Determine if it's unique (one of a kind) and if it can be traded between players.\n"
            "7. Set an appropriate value that reflects its power and rarity.\n\n"
            "### Format Instructions:\n"
            "1. Do NOT include headers, comments, or any additional text—only generate the JSON file.\n"
            "2. Strictly adhere to the following JSON format:\n"
            "{format_instructions}\n"
            "{error_description}\n"
            "### Generated JSON file:\n"
        )

        def format(
            self,
            input_text: str,
            format_instructions: str,
            errors: list[str] | None = None,
        ):
            error_description = ""

            if errors:
                error_description = (
                    "Previously encountered errors:\n"
                    + "\n".join(error for error in errors)
                    + "\nMake sure to fix them and provide correct output.\n\n"
                )

            prompt = self.template.format(
                format_instructions=format_instructions,
                error_description=error_description,
            )

            return prompt

    def __init__(self):
        super().__init__()
        self.model = GameArtifact
        self.json_generation_prompt = self.JsonGenerationPrompt(input_variables=[])


class BookReviewPair(BasePair):
    class TextGenerationPrompt(StringPromptTemplate):
        template = "Generate a book review (no more than 200 words). Mention data about the reviewer (name, email, rating, review). Mention the title, author, publication year, genre of the book. Provide an interesting review."

        def format(self):
            return self.template

    class JsonGenerationPrompt(StringPromptTemplate):
        template = (
            "You are a book review information extractor. Your task is to identify and extract book review details from the given text.\n"
            "### Input:\n{input_text}\n\n"
            "### Instructions:\n"
            "1. Extract the book details (title, author, publication year, genre).\n"
            "2. Extract the reviewer's information (name, email).\n"
            "3. Identify the rating given by the reviewer (must be a number).\n"
            "4. Extract the detailed review text.\n\n"
            "### Format Instructions:\n"
            "1. Do NOT include headers, comments, or any additional text—only generate the JSON file.\n"
            "2. Strictly adhere to the following JSON format:\n"
            "{format_instructions}\n"
            "{error_description}\n"
            "### Generated JSON file:\n"
        )

        def format(
            self,
            input_text: str,
            format_instructions: str,
            errors: list[str] | None = None,
        ):
            error_description = ""

            if errors:
                error_description = (
                    "Previously encountered errors:\n"
                    + "\n".join(error for error in errors)
                    + "\nMake sure to fix them and provide correct output.\n\n"
                )

            prompt = self.template.format(
                input_text=input_text,
                format_instructions=format_instructions,
                error_description=error_description,
            )

            return prompt

    def __init__(self):
        super().__init__()
        self.model = BookReview
        self.text_generation_prompt = self.TextGenerationPrompt(input_variables=[])
        self.json_generation_prompt = self.JsonGenerationPrompt(input_variables=[])


class TextSummaryPair(BasePair):
    class TextGenerationPrompt(StringPromptTemplate):
        template = "Generate a unique text on any topic. Generate around 100 words."

        def format(self):
            return self.template

    class JsonGenerationPrompt(StringPromptTemplate):
        template = (
            "You are a text summarizer. Your task is to analyze and summarize the given text.\n"
            "### Input:\n{input_text}\n\n"
            "### Instructions:\n"
            "1. Create a concise summary that captures the main points of the text.\n"
            "2. The summary should be no more than 25% of the original text length.\n"
            "3. Extract 1-10 relevant keywords that represent the key concepts.\n\n"
            "### Format Instructions:\n"
            "1. Do NOT include headers, comments, or any additional text—only generate the JSON file.\n"
            "2. Strictly adhere to the following JSON format:\n"
            "{format_instructions}\n"
            "{error_description}\n"
            "### Generated JSON file:\n"
        )

        def format(
            self,
            input_text: str,
            format_instructions: str,
            errors: list[str] | None = None,
        ):
            error_description = ""

            if errors:
                error_description = (
                    "Previously encountered errors:\n"
                    + "\n".join(error for error in errors)
                    + "\nMake sure to fix them and provide correct output.\n\n"
                )

            prompt = self.template.format(
                input_text=input_text,
                format_instructions=format_instructions,
                error_description=error_description,
            )

            return prompt

    def __init__(self):
        super().__init__()
        self.model = TextSummary
        self.text_generation_prompt = self.TextGenerationPrompt(input_variables=[])
        self.json_generation_prompt = self.JsonGenerationPrompt(input_variables=[])


class GameIdeaPair(BasePair):
    class JsonGenerationPrompt(StringPromptTemplate):
        template = (
            "You are a visionary game designer tasked with creating an innovative and engaging game concept.\n"
            "### Instructions:\n"
            "1. Create a unique game concept that combines compelling gameplay mechanics with an engaging narrative.\n"
            "2. Design 2-5 memorable characters with distinct personalities, motivations, and story arcs.\n"
            "3. Craft a rich setting that enhances the game's atmosphere and influences gameplay.\n"
            "4. Develop an intriguing plot with meaningful conflicts and satisfying resolution.\n"
            "5. Consider the game's genre and how it affects the overall experience.\n"
            "6. Specify the target platform(s) and technical requirements.\n"
            "7. Ensure the game idea is feasible and marketable while maintaining creativity.\n\n"
            "### Format Instructions:\n"
            "1. Do NOT include headers, comments, or any additional text—only generate the JSON file.\n"
            "2. Strictly adhere to the following JSON format:\n"
            "{format_instructions}\n"
            "{error_description}\n"
            "### Generated JSON file:\n"
        )

        def format(
            self,
            input_text: str,
            format_instructions: str,
            errors: list[str] | None = None,
        ):
            error_description = ""

            if errors:
                error_description = (
                    "Previously encountered errors:\n"
                    + "\n".join(error for error in errors)
                    + "\nMake sure to fix them and provide correct output.\n\n"
                )

            prompt = self.template.format(
                format_instructions=format_instructions,
                error_description=error_description,
            )

            return prompt

    def __init__(self):
        super().__init__()
        self.model = GameIdea
        self.json_generation_prompt = self.JsonGenerationPrompt(input_variables=[])


class HousePair(BasePair):
    class JsonGenerationPrompt(StringPromptTemplate):
        template = (
            "You are a visionary architect and real estate expert tasked with creating a detailed description of a unique property.\n"
            "### Instructions:\n"
            "1. Create a distinctive house with compelling architectural features and a cohesive design theme.\n"
            "2. Design multiple rooms that flow together logically and serve clear purposes.\n"
            "3. Craft rich descriptions that highlight unique features, materials, and design elements.\n"
            "4. Consider the property's location and how it influences the design and value.\n"
            "5. Include both practical amenities and luxurious or unexpected features.\n"
            "6. Ensure room sizes are realistic and proportional.\n"
            "7. Set an appropriate price based on features, location, and market conditions.\n\n"
            "### Format Instructions:\n"
            "1. Do NOT include headers, comments, or any additional text—only generate the JSON file.\n"
            "2. Strictly adhere to the following JSON format:\n"
            "{format_instructions}\n"
            "{error_description}\n"
            "### Generated JSON file:\n"
        )

        def format(
            self,
            input_text: str,
            format_instructions: str,
            errors: list[str] | None = None,
        ):
            error_description = ""

            if errors:
                error_description = (
                    "Previously encountered errors:\n"
                    + "\n".join(error for error in errors)
                    + "\nMake sure to fix them and provide correct output.\n\n"
                )

            prompt = self.template.format(
                format_instructions=format_instructions,
                error_description=error_description,
            )

            return prompt

    def __init__(self):
        super().__init__()
        self.model = House
        self.json_generation_prompt = self.JsonGenerationPrompt(input_variables=[])


class SollarSystemPair(BasePair):
    class JsonGenerationPrompt(StringPromptTemplate):
        template = (
            "You are a cosmic architect tasked with designing an extraordinary and unique solar system.\n"
            "### Instructions:\n"
            "1. Create a distinctive star system with compelling astronomical features and coherent cosmic dynamics.\n"
            "2. Design a central star with unique properties that influence the entire system.\n"
            "3. Craft 2-8 diverse planets with fascinating characteristics, atmospheres, and potential for life.\n"
            "4. Consider the system's location in the galaxy and how it affects its development.\n"
            "5. Include both common astronomical phenomena and unexpected cosmic features.\n"
            "6. Ensure planetary distances and sizes follow basic astronomical principles.\n"
            "7. Make the system scientifically plausible while maintaining creativity.\n\n"
            "### Format Instructions:\n"
            "1. Do NOT include headers, comments, or any additional text—only generate the JSON file.\n"
            "2. Strictly adhere to the following JSON format:\n"
            "{format_instructions}\n"
            "{error_description}\n"
            "### Generated JSON file:\n"
        )

        def format(
            self,
            input_text: str,
            format_instructions: str,
            errors: list[str] | None = None,
        ):
            error_description = ""

            if errors:
                error_description = (
                    "Previously encountered errors:\n"
                    + "\n".join(error for error in errors)
                    + "\nMake sure to fix them and provide correct output.\n\n"
                )

            prompt = self.template.format(
                format_instructions=format_instructions,
                error_description=error_description,
            )

            return prompt

    def __init__(self):
        super().__init__()
        self.model = SollarSystem
        self.json_generation_prompt = self.JsonGenerationPrompt(input_variables=[])
