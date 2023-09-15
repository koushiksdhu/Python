import requests
import datetime as dt


# API KEYS:
HEADERS = {
    "x-app-id": "9b4ba3b9",
    "x-app-key": "9521afefb97226b262b907abb596a89d",
}


exercise = input("Tell me which exercise you did: ")

NUT_ENDPOINT = " https://trackapi.nutritionix.com/v2/natural/exercise"
NUT_PARAMS = {
    "query": exercise,
}

nut_res = requests.post(url=NUT_ENDPOINT, json=NUT_PARAMS, headers=HEADERS)
data = nut_res.json()

data_formatted = {
    "workout": {
        "date": str(dt.date.today()),
        "time": dt.datetime.now().strftime("%H:%M:%S"),
        "exercise": data['exercises'][0]['name'].capitalize(),
        "duration": data['exercises'][0]['duration_min'],
        "calories": data['exercises'][0]['nf_calories']
    }
}


# print(data_formatted)
SHEETY_HEADERS = {
    "Authorization": "Bearer koushik91558522"
}
SHEETY_API_ENDPOINT = "https://api.sheety.co/b3d5070a1477bf97c2596fc0956192e5/workout/workouts"

sheety_res = requests.post(url=SHEETY_API_ENDPOINT,
                           json=data_formatted,
                           headers=SHEETY_HEADERS)
print(sheety_res.json())
