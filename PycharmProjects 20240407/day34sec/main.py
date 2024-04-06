import requests
from datetime import datetime as dt

parameters = {
    'lat': -31.950527,
    'lng': 115.860458,
    'formatted': 0
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
data = response.json()
sunrise = ":".join(data['results']['sunrise'].split("T")[1].split(":")[0:2])
sunset = ":".join(data['results']['sunset'].split("T")[1].split(":")[0:2])

time = dt.now().strftime("%H:%M")
print(time, "|", sunrise, "|", sunset)
