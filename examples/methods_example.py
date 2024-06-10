from pymeow import Client


client = Client()
breeds = client.get_all_breeds()
for breed in breeds:
    print(breed)
'''
Breed(weight={'imperial': '7  -  10', 'metric': '3 - 5'}, id='abys', name='Abyssinian', cfa_url='http://cfa.org/Breeds/BreedsAB/Abyssinian.aspx', vetstreet_url='http://www.vetstreet.com/cats/abyssinian', vcahospitals_url='https://vcahospitals.com/know-your-pet/cat-breeds/abyssinian', temperament='Active, Energetic, Independent, Intelligent, Gentle', origin='Egypt', country_codes='EG', country_code='EG', description='The Abyssinian is easy to care for, and a joy to have in your home. They’re affectionate cats and love both people and other animals.', life_span='14 - 15', indoor=0, lap=1, alt_names='', adaptability=5, affection_level=5, child_friendly=3, dog_friendly=4, energy_level=5, grooming=1, health_issues=2, intelligence=5, shedding_level=2, social_needs=5, stranger_friendly=5, vocalisation=1, experimental=0, hairless=0, natural=1, rare=0, rex=0, suppressed_tail=0, short_legs=0, wikipedia_url='https://en.wikipedia.org/wiki/Abyssinian_(cat)', hypoallergenic=0, reference_image_id='0XYvRd7oD')
...
Breed(weight={'imperial': '12 - 18', 'metric': '5 - 8'}, id='ycho', name='York Chocolate', cfa_url=None, vetstreet_url=None, vcahospitals_url=None, temperament='Playful, Social, Intelligent, Curious, Friendly', origin='United States', country_codes='US', country_code='US', description="York Chocolate cats are known to be true lap cats with a sweet temperament. They love to be cuddled and petted. Their curious nature makes them follow you all the time and participate in almost everything you do, even if it's related to water: unlike many other cats, York Chocolates love it.", life_span='13 - 15', indoor=0, lap=1, alt_names='York', adaptability=5, affection_level=5, child_friendly=4, dog_friendly=5, energy_level=5, grooming=3, health_issues=1, intelligence=5, shedding_level=3, social_needs=4, stranger_friendly=4, vocalisation=5, experimental=0, hairless=0, natural=0, rare=0, rex=0, suppressed_tail=0, short_legs=0, wikipedia_url='https://en.wikipedia.org/wiki/York_Chocolate', hypoallergenic=0, reference_image_id='0SxW2SQ_S')
'''

breed_info = client.get_breed_info('bengal')
print(breed_info)
'''
Breed(weight={'imperial': '6 - 12', 'metric': '3 - 7'}, id='beng', name='Bengal', cfa_url='http://cfa.org/Breeds/BreedsAB/Bengal.aspx', vetstreet_url='http://www.vetstreet.com/cats/bengal', vcahospitals_url='https://vcahospitals.com/know-your-pet/cat-breeds/bengal', temperament='Alert, Agile, Energetic, Demanding, Intelligent', origin='United States', country_codes='US', country_code='US', description="Bengals are a lot of fun to live with, but they're definitely not the cat for everyone, or for first-time cat owners. Extremely intelligent, curious and active, they demand a lot of interaction and woe betide the owner who doesn't provide it.", life_span='12 - 15', indoor=0, lap=0, alt_names=None, adaptability=5, affection_level=5, child_friendly=4, dog_friendly=5, energy_level=5, grooming=1, health_issues=3, intelligence=5, shedding_level=3, social_needs=5, stranger_friendly=3, vocalisation=5, experimental=0, hairless=0, natural=0, rare=0, rex=0, suppressed_tail=0, short_legs=0, wikipedia_url='https://en.wikipedia.org/wiki/Bengal_(cat)', hypoallergenic=1, reference_image_id='O3btzLlsO')
'''

cats = client.get_cat(has_breeds=True, limit=2)  # only with api key
for cat in cats:
    print(cat)
'''
Cat(image_info=CatPic(id='2bPsrIcp-', url='https://cdn2.thecatapi.com/images/2bPsrIcp-.jpg', width=960, height=1440), breed_info=Breed(weight={'imperial': '5 - 11', 'metric': '2 - 5'}, id='rblu', name='Russian Blue', cfa_url='http://cfa.org/Breeds/BreedsKthruR/RussianBlue.aspx', vetstreet_url='http://www.vetstreet.com/cats/russian-blue-nebelung', vcahospitals_url='https://vcahospitals.com/know-your-pet/cat-breeds/russian-blue', temperament='Active, Dependent, Easy Going, Gentle, Intelligent, Loyal, Playful, Quiet', origin='Russia', country_codes='RU', country_code='RU', description='Russian Blues are very loving and reserved. They do not like noisy households but they do like to play and can be quite active when outdoors. They bond very closely with their owner and are known to be compatible with other pets.', life_span='10 - 16', indoor=0, lap=1, alt_names='Archangel Blue, Archangel Cat', adaptability=3, affection_level=3, child_friendly=3, dog_friendly=3, energy_level=3, grooming=3, health_issues=1, intelligence=3, shedding_level=3, social_needs=3, stranger_friendly=1, vocalisation=1, experimental=0, hairless=0, natural=1, rare=0, rex=0, suppressed_tail=0, short_legs=0, wikipedia_url='https://en.wikipedia.org/wiki/Russian_Blue', hypoallergenic=1, reference_image_id='Rhj-JsTLP'))
Cat(image_info=CatPic(id='Yx3nQTUHu', url='https://cdn2.thecatapi.com/images/Yx3nQTUHu.jpg', width=1400, height=1050), breed_info=Breed(weight={'imperial': '5 - 10', 'metric': '2 - 5'}, id='tang', name='Turkish Angora', cfa_url='http://cfa.org/Breeds/BreedsSthruT/TurkishAngora.aspx', vetstreet_url='http://www.vetstreet.com/cats/turkish-angora', vcahospitals_url='https://vcahospitals.com/know-your-pet/cat-breeds/turkish-angora', temperament='Affectionate, Agile, Clever, Gentle, Intelligent, Playful, Social', origin='Turkey', country_codes='TR', country_code='TR', description='This is a smart and intelligent cat which bonds well with humans. With its affectionate and playful personality the Angora is a top choice for families. The Angora gets along great with other pets in the home, but it will make clear who is in charge, and who the house belongs to', life_span='15 - 18', indoor=0, lap=None, alt_names='Ankara', adaptability=5, affection_level=5, child_friendly=4, dog_friendly=5, energy_level=5, grooming=2, health_issues=2, intelligence=5, shedding_level=2, social_needs=5, stranger_friendly=5, vocalisation=3, experimental=0, hairless=0, natural=1, rare=0, rex=0, suppressed_tail=0, short_legs=0, wikipedia_url='https://en.wikipedia.org/wiki/Turkish_Angora', hypoallergenic=0, reference_image_id='7CGV6WVXq'))
'''
