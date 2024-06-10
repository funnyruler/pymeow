from requests.exceptions import RequestException


class EmptyTokenException(RequestException):
    """Empty token was passed"""
