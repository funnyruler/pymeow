from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class CatPic:
    id: str
    url: str
    width: int
    height: int


@dataclass(frozen=True)
class Breed:
    weight: dict
    id: str
    name: str
    cfa_url: str
    vetstreet_url: str
    vcahospitals_url: str
    temperament: str
    origin: str
    country_codes: str
    country_code: str
    description: str
    life_span: str
    indoor: int
    lap: int
    alt_names: str
    adaptability: int
    affection_level: int
    child_friendly: int
    dog_friendly: int
    energy_level: int
    grooming: int
    health_issues: int
    intelligence: int
    shedding_level: int
    social_needs: int
    stranger_friendly: int
    vocalisation: int
    experimental: int
    hairless: int
    natural: int
    rare: int
    rex: int
    suppressed_tail: int
    short_legs: int
    wikipedia_url: str
    hypoallergenic: int
    reference_image_id: str


@dataclass(frozen=True)
class Cat:
    image_info: CatPic
    breed_info: List[Breed]
