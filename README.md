# PyMeow
The simple way to get cats 🐱
## About

This is a simple python wrapper for using API of https://thecatapi.com/.
By this module you can get images of cats🐱 or information of their breeds.
You can see examples in the [examples folder](https://github.com/funnyruler/pymeow/tree/main/examples).
All entities are represented as dataclasses.
API have more than 60k images, breeds and facts about cats.
I recommend to [sign up](https://thecatapi.com/#pricing) and get API key, its free and this removes most of the restrictions and limits.



## Development
`pymeow` is being actively developed, and new API changes should arrive on `pymeow` very quickly. `pymeow` uses `requests` and `dataclasses` as models for its methods.
In future i will add `async` version of this wrapper.


## Installation

`pymeow` requires python 3.7 or higher. This module can be installed by pip:
```
pip install pymeow
```

## Usage
```python
from pymeow import Client


client = Client(api_key='your_api_key')
random_cat = client.get_cat(has_breeds=True)  # get random cat with breads(requires api key)

print(random_cat)
# >>> [Cat(image_info=CatPic(id='fsEMVl7f5', url='https://cdn2.thecatapi.com/images/fsEMVl7f5.jpg', width=1080, height=1080), breed_info=Breed(weight={'imperial': '8 - 20', 'metric': '4 - 9'}, id='raga', name='Ragamuffin', cfa_url='http://cfa.org/Breeds/BreedsKthruR/Ragamuffin.aspx', vetstreet_url='http://www.vetstreet.com/cats/ragamuffin', vcahospitals_url='https://vcahospitals.com/know-your-pet/cat-breeds/ragamuffin', temperament='Affectionate, Friendly, Gentle, Calm', origin='United States', country_codes='US', country_code='US', description='The Ragamuffin is calm, even tempered and gets along well with all family members. Changes in routine generally do not upset her. She is an ideal companion for those in apartments, and with children due to her patient nature.', life_span='12 - 16', indoor=0, lap=1, alt_names='', adaptability=5, affection_level=5, child_friendly=4, dog_friendly=5, energy_level=3, grooming=3, health_issues=3, intelligence=5, shedding_level=3, social_needs=3, stranger_friendly=5, vocalisation=1, experimental=0, hairless=0, natural=0, rare=0, rex=0, suppressed_tail=0, short_legs=0, wikipedia_url='https://en.wikipedia.org/wiki/Ragamuffin_cat', hypoallergenic=0, reference_image_id='SMuZx-bFM'))]
```