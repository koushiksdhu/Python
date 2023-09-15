import requests
import os

# os.environ['API_KEY'] = "f9e2765be6434fe6806a97413cd0bfc7" Added in ENV by the command: [setx API_KEY f9e2765be6434fe6806a97413cd0bfc7]
api_key = os.environ.get('API')
# print(api_key)

ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
WEATHER_PARAMS = {
    "q": input("Enter the city name: "),        # City Name
    "appid": api_key
}

req = requests.get(ENDPOINT, params=WEATHER_PARAMS) 

print(f"Status Code: {req.status_code}")
req.raise_for_status()
weather_data = req.json()   # To see the status code.
print(weather_data)




