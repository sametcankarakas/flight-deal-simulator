import requests
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, url, headers, flight_parameters):
        self.url = url
        self.headers = headers
        self.flight_parameters = flight_parameters
        self.response = requests.get(url=self.url, headers=self.headers, params=self.flight_parameters)
        self.response.raise_for_status()
        self.flight_result = self.response.json()
        print(self.flight_result)


    # def request_check(self):


    # def price_check(self):
    #     self.price = self.price_check()