import requests
from requests.models import Response
from pymeow.exceptions import EmptyTokenException, RequestException
from pymeow.models import Breed, Cat, CatPic, UserVote, Fact
from pymeow.utils import convert_json_to_obj, split_image_path


class Client:
    def __init__(self, api_key: str = None) -> None:
        """
        :param api_key: The API key from https://thecatapi.com. You can get it from https://thecatapi.com/signup
        """
        self.uri = "https://api.thecatapi.com/v1/"
        self.api_key = api_key

    def get_cat(self, limit: int = 1, page: int = 0, order: str = "RAND", has_breeds: bool = False,
                breed_ids: str = None,  sub_id: str = None) -> list[Cat] | Cat:
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
            list[dict]: A list of dictionaries containing information about the retrieved cat images.
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

    def get_breed_info(self, breed: str) -> Breed | list:
        """
        A function that retrieves information about a specific breed.

        Parameters:
            breed (str): The breed for which information is to be retrieved.(e.g. "bengal")

        Returns:
            list[dict]: A list of dictionaries containing information about the breed.
        """
        url = self.uri + f"breeds/search?q={breed}"
        response = self._request(url=url, method="GET", headers=self._get_headers())
        if response.status_code == 200:
            r_json = response.json()
            if r_json:
                return Breed(**r_json[0])
            else:
                return []

    def get_all_breeds(self) -> list[Breed]:
        """
        A function that retrieves information about all breeds by sending a GET request to the specified URI.
        Returns:
            list[dict]: A list of dictionaries containing information about all the breeds.
        """
        url = self.uri + "breeds"
        response = self._request(url=url, method="GET", headers=self._get_headers())
        if response.status_code == 200:
            r_json = response.json()
            return [Breed(**breed) for breed in r_json]

    def upload_image(self, file_path: str, sub_id: str = None, breed_ids: str = None) -> CatPic:
        """
        A function that uploads an image to the specified URI.
        Parameters:
            file_path (str): File_path to the image.
            sub_id (str): a string you can use to segment your images, e.g. knowing which of your own users uploaded it
            breed_ids (str): comma separated string of breed ids contained in the image.
        """
        url = self.uri + "images/upload"
        image_name, image_path = split_image_path(file_path)
        files = [
            ('file', (image_name, open(image_path, 'rb'), 'image/jpeg'))
        ]
        response = self._request(url=url, method="POST",
                                 data={"sub_id": sub_id, "breed_ids": breed_ids},
                                 headers=self._get_headers(),
                                 files=files)
        if response.status_code in (200, 201):
            r_json = response.json()
            return CatPic(**r_json)
        else:
            raise RequestException(response.status_code, response.text)

    def delete_image(self, image_id: str) -> bool:
        """
        A function that deletes an image from the specified URI.

        Parameters:
            image_id (str): The ID of the image to delete.

        Returns:
            bool: True if the image was deleted successfully, otherwise raise an exception.
        """
        if not self.api_key:
            raise EmptyTokenException("You must have an API key to access this method. "
                                      "To get an API key, go to https://thecatapi.com/signup")
        url = self.uri + f"images/{image_id}"
        response = self._request(url=url, method="DELETE", headers=self._get_headers({"Content-Type": "application/json"}))
        if response.status_code in (200, 201, 204):
            return True
        else:
            raise RequestException(response.status_code, response.text)

    def get_upload_images(self, limit: int = 10, page: int = 0, order: str = "DESC",
                          sub_id: str = None, breed_ids: str = None, category_ids: str = None,
                          format: str = "json", original_filename: str = None, user_id: str = None) -> list[CatPic]:
        """
        A function that retrieves information about all images uploaded to the specified URI.

        Parameters:
            limit (int): The maximum number of images to return. Defaults to 10.
            page (int): The page number to return. Defaults to 0.
            order (str): The order in which to return the images. Defaults to "DESC".
            sub_id (str): a string you can use to segment your images, e.g. knowing which of your own users uploaded it
            breed_ids (str): comma separated string of breed ids contained in the image.
            category_ids (str): comma separated string of category ids contained in the image.
            format (str): default is 'json', pass 'src' to redirect the request to the image's url - this is useful
             for setting the 'src' of an image tag.
            original_filename (str): The original filename of the image.
            user_id (str): default applied your unique user_id from welcome email,
             filter to only show images from your account that you have uploaded.

        Returns:
            list[CatPic]: A list of CatPic objects containing information about all the images.
        """
        if not self.api_key:
            raise EmptyTokenException("You must have an API key to access this method. "
                                      "To get an API key, go to https://thecatapi.com/signup")
        url = self.uri + "images"
        response = self._request(url=url, method="GET", headers=self._get_headers(),
                                 params={"limit": limit, "page": page, "order": order,
                                         "sub_id": sub_id, "breed_ids": breed_ids,
                                         "category_ids": category_ids, "format": format,
                                         "original_filename": original_filename, "user_id": user_id})
        if response.status_code == 200:
            r_json = response.json()
            return [CatPic(**image) for image in r_json]
        else:
            raise RequestException(response.status_code, response.text)

    def vote(self, image_id: str, sub_id: str, value: int) -> UserVote:
        """
        You can allow your Users to Vote on any Image, and give a score between 1 and 10.

        Parameters:
            image_id (str): The ID of the image to vote on.
            sub_id (str): The sub ID of the image to vote on.
            value (int): The value of the vote (1 for up vote, -1 for down vote).

        Returns:
            UserVote: A UserVote object containing information about the user vote.
        """
        if not self.api_key:
            raise EmptyTokenException("You must have an API key to access this method. "
                                      "To get an API key, go to https://thecatapi.com/signup")
        url = self.uri + f"votes"
        response = self._request(url=url, method="POST",
                                 json={"image_id": image_id, "sub_id": sub_id, "value": value},
                                 headers=self._get_headers())
        if response.status_code in (200, 201):
            r_json = response.json()
            return UserVote(**r_json)
        else:
            raise RequestException(response.status_code, response.text)

    def get_votes(self, attach_image: int = 0, sub_id: str = None, page: int = 0,
                  limit: int = 100, order: str = 'ASC') -> list[UserVote]:
        """
        Retrieve any created Votes. This can be filtered by sub_id,
         and paginated using page and limit Query string parameters.

        Parameters:
            attach_image (int): 0 to not attach image, 1 to attach image.
            sub_id (str): The sub ID of the image to vote on.
            page (int): The page number of results to retrieve (default is 0).
            limit (int): The number of results per page (default is 100).
            order (str): The order in which to retrieve results (default is "ASC").

        Returns:
            list[UserVote]: A list of UserVote objects containing information about the retrieved votes.
        """
        if not self.api_key:
            raise EmptyTokenException("You must have an API key to access this method. "
                                      "To get an API key, go to https://thecatapi.com/signup")
        url = self.uri + "votes"
        response = self._request(url=url, params={"attach_image": attach_image, "sub_id": sub_id,
                                                  "page": page, "limit": limit, "order": order},
                                 method="GET", headers=self._get_headers())
        if response.status_code == 200:
            r_json = response.json()
            return [UserVote(**v) for v in r_json]
        else:
            raise RequestException(response.status_code, response.text)

    def get_vote_by_id(self, vote_id: int | str) -> UserVote:
        """
        Method to retrieve vote by vote_id

        Parameters:
            vote_id (int): The ID of the vote to retrieve.

        Returns:
            UserVote: A UserVote object containing information about the retrieved vote.
        """
        if not self.api_key:
            raise EmptyTokenException("You must have an API key to access this method. "
                                      "To get an API key, go to https://thecatapi.com/signup")
        url = self.uri + f"votes/{vote_id}"
        response = self._request(url=url, method="GET", headers=self._get_headers())
        if response.status_code == 200:
            r_json = response.json()
            return UserVote(**r_json)
        else:
            raise RequestException(response.status_code, response.text)

    def delete_vote(self, vote_id: int | str) -> dict:
        """
        Method to delete vote by vote_id

        Parameters:
            vote_id (int): The ID of the vote to delete.

        Returns:
            dict: A dictionary containing information about the deleted vote, e.g, {'message': 'SUCCESS'}
        """
        if not self.api_key:
            raise EmptyTokenException("You must have an API key to access this method. "
                                      "To get an API key, go to https://thecatapi.com/signup")
        url = self.uri + f"votes/{vote_id}"
        response = self._request(url=url, method="DELETE", headers=self._get_headers())
        if response.status_code == 200:
            return response.json()
        else:
            raise RequestException(response.status_code, response.text)

    def get_random_fact(self, page: int = 0, limit: int = 1, order: str = "RAND") -> list[Fact]:
        """
        Retrieve random facts. This can be filtered by page and limit Query string parameters.

        Parameters:
            page (int): The page number of results to retrieve (default is 0).
            limit (int): The number of results per page (default is 1).
            order (str): The order in which to retrieve results (default is "RAND").

        Returns:
            list[Fact]: A list of Fact objects containing information about the retrieved facts.
        """
        if not self.api_key:
            raise EmptyTokenException("You must have an API key with premium to access this method. "
                                      "To get an API key, go to https://thecatapi.com/signup")
        url = self.uri + "facts/"
        response = self._request(url=url, params={"page": page, "limit": limit, "order": order},
                                 method="GET", headers=self._get_headers())
        if response.status_code == 200:
            r_json = response.json()
            return [Fact(**f) for f in r_json]
        else:
            raise RequestException(response.status_code, response.text)

    def get_breed_fact(self, breed_name: str, limit: int = 1, page: int = 0, order: str = "ASC") -> list[Fact]:
        """
        Retrieve random facts. This can be filtered by page and limit, ordered by order Query string parameters.

        Parameters:
            breed_name (str): The name of the breed to retrieve facts for.
            limit (int): The number of results per page (default is 1).
            page (int): The page number of results to retrieve (default is 0).
            order (str): The order in which to retrieve results (default is "ASC").

        Returns:
            list[Fact]: A list of Fact objects containing information about the retrieved breed.
        """
        if not self.api_key:
            raise EmptyTokenException("You must have an API key with premium to access this method. "
                                      "To get an API key, go to https://thecatapi.com/signup")
        url = f'https://api.thecatapi.com/v1/breeds/{breed_name}/facts'
        response = self._request(url=url, method="GET", headers=self._get_headers(),
                                 params={"limit": limit, "page": page, "order": order})
        if response.status_code == 200:
            r_json = response.json()
            return [Fact(**f) for f in r_json]
        else:
            raise RequestException(response.status_code, response.text)

    def get_version(self) -> dict:
        """
        Get the current version of the API.

        Returns:
            dict: A dictionary containing information about the current version of the API.
        """
        response = self._request(url=self.uri, method="GET", headers=self._get_headers())
        if response.status_code == 200:
            return response.json()
        else:
            raise RequestException(response.status_code, response.text)

    def _get_headers(self, *args) -> dict:
        headers = {}
        for arg in args:
            headers.update(arg)
        if self.api_key:
            headers.update({"x-api-key": self.api_key})
        return headers

    @staticmethod
    def _request(url: str, method: str, params: dict = None,
                 data: dict = None, json: dict = None, headers: dict = None,
                 files: list = None, timeout: float = 30.0) -> Response:
        try:
            response = requests.request(url=url, method=method, params=params,
                                        headers=headers, data=data, timeout=timeout, files=files, json=json)
            return response
        except RequestException:
            raise RequestException

    def __repr__(self):
        return f"Client(api_key={self.api_key}, uri={self.uri})"
