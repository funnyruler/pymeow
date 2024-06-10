from pymeow.models import CatPic, Breed, Cat
from typing import List


def convert_breed_info(breeds: List[dict]) -> List[Breed]:
    """
    A function that converts a list of dictionaries to a list of Breed objects.

    Parameters:
        breeds (List[dict]): A list of dictionaries containing information about the breed.

    Returns:
        List[Breed]: A list of Breed objects containing information about the breed.
    """
    breed_list = []
    for breed in breeds:
        breed_info = {field: breed.get(field, None) for field in Breed.__annotations__}
        breed_list.append(Breed(**breed_info))
    return breed_list


def convert_pic_info(pic_info: dict) -> CatPic:
    """
    A function that converts a dictionary to a CatPic object.

    Parameters:
        pic_info (dict): A dictionary containing information about the cat image.

    Returns:
        CatPic: A CatPic object containing information about the cat image.
    """
    pic_info = {field: pic_info.get(field, None) for field in CatPic.__annotations__}
    return CatPic(**pic_info)


def convert_json_to_obj(json_data: dict) -> List[CatPic]:
    """
    A function that converts a dictionary to a list of CatPic objects.

    Parameters:
        json_data (dict): A dictionary containing information about the cat images.

    Returns:
        List[CatPic]: A list of CatPic objects containing information about the cat images.
    """
    result_list = []
    for i in json_data:
        if 'breeds' in i:
            breed_info = convert_breed_info(i['breeds'])
        else:
            breed_info = None
        del i['breeds']
        pic_info = convert_pic_info(i)
        result_list.append(Cat(breed_info=breed_info, image_info=pic_info))
    return result_list