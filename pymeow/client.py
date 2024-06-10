import requests
from requests.models import Response
from pymeow.exceptions import EmptyTokenException, RequestException
from pymeow.models import Breed, Cat
from pymeow.utils import convert_json_to_obj, convert_breed_info
from typing import List, Dict


class Client:
    def __init__(self, api_key: str = None) -> None:
        """
        :param api_key: The API key from https://thecatapi.com. You can get it from https://thecatapi.com/signup
        """
        self.uri = "https://api.thecatapi.com/v1/"
        self.api_key = api_key

    def get_cat(self, limit: int = 1, page: int = 0, order: str = "RAND", has_breeds: bool = False,
                breed_ids: str = None,  sub_id: str = None) -> List[Cat]:
        """
        A function that retrieves cat images url with id and sizes based on the specified parameters.
        Parameters available only if you have an API key

        Parameters:
            limit (int): The number of images to retrieve (default is 1).
            page (int): The page number of results to retrieve (default is 0).
            order (str): The order in which to retrieve images (default is "RAND").
            has_breeds (int): Indicator for whether to retrieve images with breeds (default is 0).
            breed_ids (str): The IDs of specific breeds to retrieve images for.
            sub_id (str): The sub ID for the request.

        Returns:
            List[dict]: A list of dictionaries containing information about the retrieved cat images.
        """
        args = locals().copy()
        del args['self']
        if (args['limit'] > 10 or args['has_breeds']) and not self.api_key:
            raise EmptyTokenException("You must have an API key to get more than 10 images or use params."
                                      "To get an API key, go to https://thecatapi.com/signup")
        url = self.uri + "images/search"
        response = self._request(url=url, method="GET", params=args, headers=self._get_headers())
        if response.status_code == 200:
            r_json = response.json()
            return convert_json_to_obj(r_json)
        else:
            raise RequestException(response.status_code, response.text)

    def get_breed_info(self, breed: str) -> Breed:
        """
        A function that retrieves information about a specific breed.

        Parameters:
            breed (str): The breed for which information is to be retrieved.(e.g. "bengal")

        Returns:
            List[dict]: A list of dictionaries containing information about the breed.
        """
        url = self.uri + f"breeds/search?q={breed}"
        response = self._request(url=url, method="GET", headers=self._get_headers())
        if response.status_code == 200:
            r_json = response.json()
            return convert_breed_info(r_json)

    def get_all_breeds(self) -> List[Breed]:
        """
        A function that retrieves information about all breeds by sending a GET request to the specified URI.
        Returns:
            List[dict]: A list of dictionaries containing information about all the breeds.
        """
        url = self.uri + "breeds"
        response = self._request(url=url, method="GET", headers=self._get_headers())
        if response.status_code == 200:
            r_json = response.json()
            return convert_breed_info(r_json)

    def _get_headers(self) -> Dict:
        headers = {}
        if self.api_key:
            headers = {"x-api-key": self.api_key}
        return headers

    @staticmethod
    def _request(url: str, method: str, params: dict = None, json: dict = None,
                 headers: dict = None, timeout: float = 30.0) -> Response:
        try:
            response = requests.request(url=url, method=method, params=params,
                                        headers=headers, json=json, timeout=timeout)
            return response
        except RequestException:
            raise RequestException

    def __repr__(self):
        return f"Client(api_key={self.api_key}, uri={self.uri})"
