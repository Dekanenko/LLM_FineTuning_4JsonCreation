from pydantic import BaseModel, Field, EmailStr, conlist
from enum import Enum
from typing import Optional

class CharacterNames(BaseModel):
    class FullName(BaseModel):
        name: str = Field(description="Name of the character")
        surname: str = Field(description="Surname of the character")
    
    fullname_list: list[FullName] = Field(description="List of full names for every character")


class FictionalCharacter(BaseModel):
    class CharacterType(str, Enum):
        MAGE = "mage"
        ARCHER = "archer"
        WARRIOR = "warrior"
    
    class CharacterRace(str, Enum):
        HUMAN = "human"
        ELF = "elf"
        ORK = "ork"
    
    name: str = Field(description="Name of the character")
    age: int = Field(description="Age of the character")
    character_type: CharacterType = Field(description="Type of the character")
    biography: str = Field(description="Character's biography")
    character_race: CharacterRace = Field(description="Character's race")
    weapon: str = Field(description="Character's weapon")
    attack_description: str = Field(description="The description of the attack")
    skill_description: str = Field(description="The description of the skill")
    ultimate_description: str = Field(description="The description of the ultimate")


class TShirtOrder(BaseModel):
    class Gender(str, Enum):
        MALE = "male"
        FEMALE = "female"
        UNIXSEX = "unisex"
    
    class Type(str, Enum):
        HENLEY = "henley"
        VNECK = "vneck"
        CREWNECK = "crewneck"
        POLO = "polo"
        TANKTOP = "tanktop"
        JERSEY = "jersey"
        RAGLAN = "raglan"
        SLEEVELESS = "sleeveless"

    class Size(str, Enum):
        S = "S"
        M = "M"
        L = "L"
        XL = "XL"
        XXL = "XXL"
        
    type: Type = Field(description="Type of the t-shirt", default=Type.VNECK)
    size: Size = Field(description="Size of the t-shirt", default=Size.M)
    color: str = Field(description="Color of the t-shirt", default="black")
    quantity: int = Field(description="Quantity of the t-shirt", default=1)
    gender: Gender = Field(description="Gender of the t-shirt", default=Gender.UNIXSEX)
    picture_description: str = Field(description="Description of the picture")


class FilmIdea(BaseModel):
    class Genre(str, Enum):
        ACTION = "action"
        COMEDY = "comedy"
        DRAMA = "drama"
        HORROR = "horror"
        MYSTERY = "mystery"
        ROMANCE = "romance"
        SCIENCE_FICTION = "science_fiction"
        THRILLER = "thriller"
    
    class Character(BaseModel):
        class Gender(str, Enum):
            MALE = "male"
            FEMALE = "female"
            OTHER = "other"

        name: str = Field(description="Name of the character")
        age: int = Field(description="Age of the character")
        gender: Gender = Field(description="Gender of the character")
        role: str = Field(description="Role of the character")
        biography: str = Field(description="Biography of the character")
        
    genre: Genre = Field(description="Genre of the film")
    title: str = Field(description="Title of the film")
    description: str = Field(description="Description of the film")
    characters: conlist(Character, min_length=1, max_length=5) = Field(..., description="Characters of the film")
    plot: str = Field(description="Plot of the film")
    setting: str = Field(description="Setting of the film")
    style: str = Field(description="Style of the film")
    tone: str = Field(description="Tone of the film")
    budget: int = Field(description="Budget of the film")


class Itinerary(BaseModel):
    class Activity(BaseModel):
        name: str = Field(description="Name of the activity")
        start_time: str = Field(description="Start time of the activity")
        end_time: str = Field(description="End time of the activity")
        location: str = Field(description="Location of the activity")
        cost: Optional[float] = Field(description="Cost of the activity", default=None)

    class Transport(BaseModel):
        mode: str = Field(description="Mode of the transport")
        departure: str = Field(description="Departure of the transport")
        arrival: str = Field(description="Arrival of the transport")
        cost: Optional[float] = Field(description="Cost of the transport", default=None)

    traveler_name: str = Field(description="Name of the traveler")
    destination: str = Field(description="Destination of the itinerary")
    start_date: str = Field(description="Start date of the itinerary")
    end_date: str = Field(description="End date of the itinerary")
    activities: list[Activity] = Field(description="Activities of the itinerary")
    transports: list[Transport] = Field(description="Transports of the itinerary")


class Recipe(BaseModel):
    class Ingredient(BaseModel):
        name: str
        quantity: float
        unit: str

    class Instruction(BaseModel):
        step_number: int
        description: str

    class NutritionFacts(BaseModel):
        calories: float
        protein: float
        fat: float
        carbs: float

    title: str
    cuisine: str
    ingredients: list[Ingredient]
    instructions: list[Instruction]
    total_time_minutes: int
    nutrition: Optional[NutritionFacts] = None


class Events(BaseModel):
    class Event(BaseModel):
        class Attendee(BaseModel):
            name: str
            email: EmailStr
            has_confirmed: bool

        title: str
        date: str
        start_time: str
        end_time: str
        location: str
        attendees: list[Attendee]

    events: list[Event]

class Resume(BaseModel):
    class Education(BaseModel):
        institution: str
        degree: str
        graduation_year: int

    class WorkExperience(BaseModel):
        company: str
        role: str
        start_year: int
        end_year: Optional[int] = None

    full_name: str
    email: EmailStr
    phone_number: Optional[str] = None
    education: list[Education]
    work_experience: list[WorkExperience]
    skills: list[str]


class GameArtifact(BaseModel):
    class Buff(BaseModel):
        name: str
        description: str

    class Defuff(BaseModel):
        name: str
        description: str

    name: str = Field(description="Name of the artifact")
    location: str = Field(description="Location of the artifact")
    buffs: list[Buff] = Field(description="Buffs of the artifact")
    defuffs: list[Defuff] = Field(description="Defuffs of the artifact")
    description: str = Field(description="Description of the artifact")
    type: str = Field(description="Type of the artifact")
    rarity: str = Field(description="Rarity of the artifact")
    value: int = Field(description="Value of the artifact")
    is_unique: bool = Field(description="Is the artifact unique")
    is_tradable: bool = Field(description="Is the artifact tradable")


class BookReview(BaseModel):
    class Reviewer(BaseModel):
        name: str = Field(description="Name of the reviewer")
        email: EmailStr = Field(description="Email of the reviewer")
        rating: int = Field(description="Rating of the reviewer")
        review: str = Field(description="Review of the reviewer")

    title: str = Field(description="Title of the book")
    author: str = Field(description="Author of the book")
    publication_year: int = Field(description="Publication year of the book")
    genre: str = Field(description="Genre of the book")
    reviewer: Reviewer = Field(description="Reviewer of the book")


class TextSummary(BaseModel):
    text: str = Field(description="Text to summarize")   
    summary: str = Field(description="Summary of the text")
    keywords: conlist(str, min_length=1, max_length=10) = Field(description="Keywords of the text")


class GameIdea(BaseModel):
    class Genre(str, Enum):
        ACTION = "action"
        COMEDY = "comedy"
        DRAMA = "drama"
        HORROR = "horror"
        MYSTERY = "mystery"
    
    class Character(BaseModel):
        name: str = Field(description="Name of the character")
        age: int = Field(description="Age of the character")
        gender: str = Field(description="Gender of the character")
        role: str = Field(description="Role of the character")
        biography: str = Field(description="Biography of the character")

    class Setting(BaseModel):
        name: str = Field(description="Name of the setting")
        description: str = Field(description="Description of the setting")

    class Plot(BaseModel):
        title: str = Field(description="Title of the plot")
        description: str = Field(description="Description of the plot")

    class Conflict(BaseModel):
        name: str = Field(description="Name of the conflict")
        description: str = Field(description="Description of the conflict")

    class Resolution(BaseModel):
        name: str = Field(description="Name of the resolution")
        description: str = Field(description="Description of the resolution")

    genre: Genre = Field(description="Genre of the game")
    characters: list[Character] = Field(description="Characters of the game")
    setting: Setting = Field(description="Setting of the game")
    plot: Plot = Field(description="Plot of the game")
    conflict: Conflict = Field(description="Conflict of the game")
    resolution: Resolution = Field(description="Resolution of the game")
    description: str = Field(description="Description of the game")
    type: str = Field(description="Type of the game")
    platform: str = Field(description="Platform of the game")
    release_date: str = Field(description="Release date of the game")
    rating: float = Field(description="Rating of the game")


class House(BaseModel):
    class Room(BaseModel):
        class Type(str, Enum):
            BEDROOM = "bedroom"
            LIVING_ROOM = "living_room"
            KITCHEN = "kitchen"
            BATHROOM = "bathroom"
            OFFICE = "office"
            GARAGE = "garage"

        name: str = Field(description="Name of the room")
        description: str = Field(description="Description of the room")
        area: float = Field(description="Area of the room")
        type: Type = Field(description="Type of the room")

    name: str = Field(description="Name of the house")
    rooms: list[Room] = Field(description="Rooms of the house")
    description: str = Field(description="Description of the house")
    location: str = Field(description="Location of the house")
    price: int = Field(description="Price of the house")
    is_unique: bool = Field(description="Is the house unique")
    is_tradable: bool = Field(description="Is the house tradable")


class SollarSystem(BaseModel):
    class Planet(BaseModel):
        name: str = Field(description="Name of the planet")
        description: str = Field(description="Description of the planet")
        size: float = Field(description="Size of the planet")
        population: int = Field(description="Population of the planet")
        distance_from_sun: float = Field(description="Distance from the sun")
    
    class Star(BaseModel):
        name: str = Field(description="Name of the star")
        description: str = Field(description="Description of the star")
        size: float = Field(description="Size of the star")
        temperature: float = Field(description="Temperature of the star")
        radius: float = Field(description="Radius of the star")
        

    name: str = Field(description="Name of the solar system")
    description: str = Field(description="Description of the solar system")
    planets: list[Planet] = Field(description="Planets of the solar system")
    central_star: Star = Field(description="Central star of the solar system")