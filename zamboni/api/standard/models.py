# -*- coding: utf-8 -*-

import requests


class PublicBase():
    """
    Abstract Base Class for all public API operators.

    This class is abstract and should not be instantiated.

    :param endpoint: A Public NHL API Endpoint
    :type endpoint: str
    :param parameters: k,v pairs that populate missing
        values in Endpoint
    :type parameters: dict
    """
    def __init__(
            self,
            endpoint,
            parameters,
            *args,
            **kwargs):

        self.endpoint = endpoint
        self.parameters = parameters

    def format_endpoint(self, parameters):
        # TODO: Add error handling if missing parameters
        url = self.endpoint
        formatted_url = url.format(**parameters)
        return formatted_url

    def get_data(self):
        try:
            r = requests.get(self.format_endpoint(self.endpoint, self.parameters))
            blob = r.json()
            return blob
        except requests.exceptions.RequestException as e:
            print(e)
            # TODO: Better Exception Handling if API is Down

        return -1
