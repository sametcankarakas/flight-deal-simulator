import requests
import os
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        # self.sheety_auth = os.environ["SHEETY_BEARER_AUTH"]
        self.sheety_endpoint = "https://api.sheety.co/59490a34d8d35b5278e99d96c81bd616/flightDeals/prices"


    def sheety_response(self):
        self.sheety_response = requests.get(url=self.sheety_endpoint)
        self.sheety_response.raise_for_status()
        self.response = self.sheety_response.json()
        return self.response



