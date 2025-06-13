import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content  # Returns the raw response body (bytes)

    def load_json(self):
        response = requests.get(self.url)
        return response.json()  # Parses and returns the JSON response
