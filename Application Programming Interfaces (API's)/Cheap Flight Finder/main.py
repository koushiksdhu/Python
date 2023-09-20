from flight_search import FlightSearch
from data_manager import DataManager
import datetime as dt

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()

ORIGIN_CITY_IATA = "CCU"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data[0]:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tommorow = dt.datetime.now() + dt.timedelta(days=1)
four_months_from_today = dt.datetime.now() + dt.timedelta(days=(4*30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tommorow,
        to_time=four_months_from_today
    )


print(sheet_data)
