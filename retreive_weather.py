import requests
import cped

#33.44
#-94.04

class get_weather():
    def __init__(self, key, url, city, days=7, units="imperial"):
        self.key = key
        self.url = url
        self.city = city
        self.days = days
        self.units = units


    def retreive_forecast(sefl):
      pass


onecall = "https://api.openweathermap.org/data/3.0/onecall"
base_url = "http://api.openweathermap.org/data/2.5/forecast/daily"

# print("Warning: City list does not include all cities in the world")
# city = input("Enter a city name: ")

#print("Now lets get the coordinates")
#lat = input("whats the latitude?: ")
#lon = input("whats the longitude?: ")

lat = "33.44"
lon = "-94.04"

exclusion = "current,minutely,hourly,alerts"

units = "imperial"

request_url = f"{onecall}?appid={cped.api_key}&lat={lat}&lon={lon}&exclude={exclusion}&units={units}"

response = requests.get(request_url)


if response.status_code == 200:
    data = response.json()
    #weather = data['weather'][0]['description']
    print("Retrieved successfully")

else:
    print("An error occured")
    print(response.status_code)
    print(response.json())


weather = []

for item in data['daily']:
    full_day = []
    full_day.append(item['dt'])
    full_day.append(item['temp']['min'])
    full_day.append(item['temp']['max'])
    weather.append(full_day)

print(weather)