import requests
from datetime import datetime
import smtplib
import time

my_email = "kohdi111@gmail.com"
password = "ttut mwrx vtpb msuw"

MY_LAT = -31.950527
MY_LONG = 115.860458


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

def ready():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) % 24
    sunrise += round((int(data["results"]["sunrise"].split("T")[1].split(":")[1]) % 24) / 60, 2)
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) % 24
    sunset += round((int(data["results"]["sunset"].split("T")[1].split(":")[1]) % 24) / 60, 2)

    time_now = (datetime.now().hour + round((datetime.now().minute / 60), 2) + 16) % 24

    is_dark = sunset < time_now < sunrise
    is_lat = iss_latitude - 5 < MY_LAT < iss_latitude + 5
    is_lon = iss_longitude - 5 < MY_LONG < iss_longitude + 5

    return True#is_dark * is_lat * is_lon

while True:
    if ready():
        print("We are go!")
        connection = smtplib.SMTP("smtp.gmail.com", 587, timeout=30)
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=f"Subject: Look Up!\n\nISS is up there nowsies")
        print("sent")
        connection.quit()
    time.sleep(60)
