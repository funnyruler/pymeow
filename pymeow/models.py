from pydantic import BaseModel
from typing import List, Optional, Union


class CatPic(BaseModel):
    id: Optional[str] = None
    url: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None


class Breed(BaseModel):
    weight: Optional[dict] = None
    id: Optional[str] = None
    name: Optional[str] = None
    cfa_url: Optional[str] = None
    vetstreet_url: Optional[str] = None
    vcahospitals_url: Optional[str] = None
    temperament: Optional[str] = None
    origin: Optional[str] = None
    country_codes: Optional[str] = None
    country_code: Optional[str] = None
    description: Optional[str] = None
    life_span: Optional[str] = None
    indoor: Optional[int] = None
    lap: Optional[int] = None
    alt_names: Optional[str] = None
    adaptability: Optional[int] = None
    affection_level: Optional[int] = None
    child_friendly: Optional[int] = None
    dog_friendly: Optional[int] = None
    energy_level: Optional[int] = None
    grooming: Optional[int] = None
    health_issues: Optional[int] = None
    intelligence: Optional[int] = None
    shedding_level: Optional[int] = None
    social_needs: Optional[int] = None
    stranger_friendly: Optional[int] = None
    vocalisation: Optional[int] = None
    experimental: Optional[int] = None
    hairless: Optional[int] = None
    natural: Optional[int] = None
    rare: Optional[int] = None
    rex: Optional[int] = None
    suppressed_tail: Optional[int] = None
    short_legs: Optional[int] = None
    wikipedia_url: Optional[str] = None
    hypoallergenic: Optional[int] = None
    reference_image_id: Optional[str] = None


class Cat(BaseModel):
    image_info: CatPic
    breed_info: Union[List[Breed], Breed] = None


class UserVote(BaseModel):
    id: Optional[int] = None
    image_id: Optional[str] = None
    sub_id: Optional[str] = None
    value: Optional[int] = None
    created_at: Optional[str] = None
    image: Optional[dict] = None


class Fact(BaseModel):
    id: Optional[str] = None
    fact: Optional[str] = None
    breed_id: Optional[str] = None
    title: Optional[str] = None
