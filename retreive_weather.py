import requests
import cped


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

print("Now lets get the coordinates")
lat = input("whats the latitude?: ")
lon = input("whats the longitude?: ")

exclusion = "current,minutely,hourly,alerts"

units = "imperial"

request_url = f"{onecall}?appid={cped.api_key}&lat={lat}&lon={lon}&exclude={exclusion}&units={units}"

response = requests.get(request_url)


if response.status_code == 200:
    data = response.json()
    #weather = data['weather'][0]['description']
    #print(f"We're looking at a {weather} day")
    #temperature = round((data['main']['temp'] - 273.15), 2)
    #print(f"the temperature in {city} is {temperature} celcius")


    print(data)
else:
    print("An error occured")
    print(response.status_code)
    print(response.json())
