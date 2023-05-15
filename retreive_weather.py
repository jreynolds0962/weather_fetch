import requests
import cped


class get_weather():
    def __init__(self, key, url, city, days=7, units="imperial", lat="33.44", lon="-94.04"):
        self.key = key
        self.url = url
        self.city = city
        self.days = days
        self.units = units
        self.lat = lat
        self.lon = lon

    def get_lat_and_lon(self):
        print("Now lets get the coordinates")
        lat = input("whats the latitude?: ")
        self.lat = lat
        lon = input("whats the longitude?: ")
        self.lon = lon



    def retreive_forecast(self):
        request_url = f"{self.url}?appid={cped.api_key}&lat={self.lat}&lon={self.lon}&exclude={exclusion}&units={self.units}"

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

        return weather
      


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