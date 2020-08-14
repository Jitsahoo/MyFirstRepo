import requests

"""
This class is used to send the http request {GET,POST,PUT,DELETE} and return the response object
"""


class Request:
    def __init__(self, url):
        self.url = url
        self.contentType = 'application/json'

    """ 
    This methods performs post operation and returns response
    """
    def post_request(self, json):
        response = requests.post(self.url,  json=json)
        return response

    """ 
    This methods performs get operation and returns response
    """
    def get_request(self):
        response = requests.get(self.url)
        return response

    """ 
        This methods performs put operation and returns response
    """
    def put_request(self ,json):
        response = requests.put(self.url, json=json)
        return response

    """ 
            This methods performs delete operation and returns response
    """
    def delete_request(self):
        response = requests.delete(self.url)
        return response
