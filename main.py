#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
import os
from data_manager import DataManager
import datetime

#
# tequila_api_key = os.environ["TEQUILA_API_KEY"]
# tequila_search_endpoint = "https://tequila-api.kiwi.com/v2/search"
#
#
# header = {
#     "apikey": tequila_api_key
# }
# flight_parameters = {
#     "fly_from": "TR",
#     "fly_to": "FRA",
#     "date_from": "05/02/2022",
#     "date_to": "15/02/2022",
#     "limit": 10
# }
#
# response_flight = requests.get(url=tequila_search_endpoint, headers=header, params=parameters)
# response_flight.raise_for_status()
#
# flights_with_price = response_flight.json()["data"]
# print(response_flight.text)
# flight_list = []
#
# for number in flights_with_price:
#     if number["price"] < 60:
#         flight_list.append(number)
#
# print(flight_list)

where_to = input("Enter city name where you want to fly?: ").title()

#
# sheety_result = DataManager()
# result = sheety_result.sheety_response()
result = {'prices': [{'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 66, 'id': 2}, {'city': 'Berlin', 'iataCode': 'BER', 'lowestPrice': 88, 'id': 3}, {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 485, 'id': 4}, {'city': 'Sydney', 'iataCode': 'SYD', 'lowestPrice': 551, 'id': 5}, {'city': 'London', 'iataCode': 'LON', 'lowestPrice': 333, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414, 'id': 7}, {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 343, 'id': 8}, {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 453, 'id': 9}, {'city': 'Cape Town', 'iataCode': 'CPT', 'lowestPrice': 411, 'id': 10}]}
for _ in result["prices"]:
    if _["city"] == where_to.title():
        print(f"the price of {where_to} in the sheet is: €"f"{_['lowestPrice']}")
        break
    print(_)
