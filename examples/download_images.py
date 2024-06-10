import os
import urllib3
from pymeow import Client


def download_photo(url: str) -> None:
    pool_manager = urllib3.PoolManager()
    file_name = url.split('/')[-1]
    response = pool_manager.request('GET', url)
    with open(os.path.join('images', file_name), 'wb') as f:
        f.write(response.data)
    print(f'Downloaded {file_name}')


client = Client()
cats = client.get_cat(limit=10)
if not os.path.exists('images'):
    os.mkdir('images')
for cat in cats:
    download_photo(cat.image_info.url)
