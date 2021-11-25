import os
class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, city_iata):
        self.tequila_api_key = os.environ["TEQUILA_API_KEY"]
        self.tequila_search_endpoint = "https://tequila-api.kiwi.com/v2/search"
        self.city_from = "Istanbul"
        self.fly_from = "SAW"
        # self.city_to = city
        self.city_to_iata = city_iata
        self.date_from = "27/11/2021"
        self.date_to = "27/04/2022"

    def flight_parameters(self):
        self.parameters = {
            "fly_from": self.fly_from,
            "fly_to": self.city_to_iata,
            "date_from": self.date_from,
            "date_to": self.date_to,
        }
        return self.parameters
