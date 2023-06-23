import requests
from datetime import datetime

MY_LAT = 24.265240
MY_LONG = 87.250191

parameter = {
    "lat" : MY_LAT,
    "lng" : MY_LONG,
    "formatted" : 0
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params = parameter)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset = data['results']['sunset'].split('T')[1].split(':')[0]
print("Sunrise: ", sunrise)
print("Sunset: ", sunset)

time_now = datetime.now().hour
print(time_now)