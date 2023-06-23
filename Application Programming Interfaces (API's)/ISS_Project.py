import requests
from datetime import datetime
import smtplib
import time

email = "ksprojecttesting@gmail.com"
password = "swhnqizfjzgglswx"

MY_LAT = 22.572645
MY_LONG = 88.363892

parameters = {
    "lat" : MY_LAT,
    "lng" : MY_LONG,
    "formatted" : 0
}

def is_iss_overhead():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status
    iss_data = iss_response.json()
    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_postion"]["longitude"])
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
    
def is_night():
    sun_response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
    sun_response.raise_for_status
    sun_data = sun_response.json()
    sunrise = int(sun_data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(sun_data['results']['sunset'].split('T')[1].split(':')[0])
    
    curr_time = datetime.now().hour
    
    if curr_time >= sunset or curr_time <= sunrise:
        return True
    
while True: 
    time.sleep(60)
    if is_iss_overhead() and  is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(
            from_addr = email,
            to_addrs = "kkoushikssadhu@gmail.com",
            msg = "Subject: Look Up! \n\n The ISS is above you in the sky."
        )
        
