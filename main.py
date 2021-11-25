#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_data import FlightData
import datetime

#
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
where_to_iata = ""
#
# sheety_result = DataManager()
# result = sheety_result.sheety_response()
result = {'prices': [{'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 66, 'id': 2}, {'city': 'Berlin', 'iataCode': 'BER', 'lowestPrice': 88, 'id': 3}, {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 485, 'id': 4}, {'city': 'Sydney', 'iataCode': 'SYD', 'lowestPrice': 551, 'id': 5}, {'city': 'London', 'iataCode': 'LON', 'lowestPrice': 333, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414, 'id': 7}, {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 343, 'id': 8}, {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 453, 'id': 9}, {'city': 'Cape Town', 'iataCode': 'CPT', 'lowestPrice': 411, 'id': 10}]}
for _ in result["prices"]:
    if _["city"] == where_to:
        where_to_iata = _["iataCode"]
        where_to_price = _["lowestPrice"]
        print(f"the price of {where_to}-{where_to_iata} in sheet price is: €"f"{where_to_price}")
        break

enter_flight_data = FlightData(city_iata=where_to_iata)
get_flight_data = enter_flight_data.flight_parameters()
print(get_flight_data)

