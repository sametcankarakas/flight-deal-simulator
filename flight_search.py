import requests
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def check_flights(self, url, headers, flight_parameters):
        self.response = requests.get(url, headers, flight_parameters)



