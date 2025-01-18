import requests
import json
import math
import matplotlib.pyplot as plt
import numpy as np
from pytz import timezone 
from datetime import datetime

country = input("Enter your country : ")
city = input("Enter your nearest city : ")
country = country.capitalize()
city = city.capitalize()
counURL = "&country={}".format(country)
api_url = 'https://api.api-ninjas.com/v1/geocoding?city={}'.format(city)
response = requests.get(api_url + counURL, headers={'X-Api-Key': 'ADD YOUR API KEY HERE'})
if response.status_code == requests.codes.ok:
    lat = response.json()[0]['latitude']
    long = response.json()[0]['longitude']
    wet_url = 'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={APIKEY}'.format(latitude=lat,longitude=long,APIKEY="ADD YOUR API KEY HERE")
    resp = requests.get(wet_url)
    if resp.status_code == requests.codes.ok:
        data = resp.json()
        Description = data['weather'][0]['description']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        temp_min = data['main']['temp_min']
        temp_max = data['main']['temp_max']
        ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%H')
        ind_time = int(ind_time)
        Temperature = [temp,feels_like,temp_min,temp_max]
        time = []
        for i in range(ind_time,ind_time+4):
             if(i>23):
                 i = i - 24
                 time.append(i)
             else:
                 time.append(i)
        np_Temperature = np.array(Temperature)
        np_time = np.array(time)
        np_Temperature = np_Temperature - 273.15
        plt.plot(np_time,np_Temperature)
        plt.xlabel('Time')
        plt.ylabel('Temperature')
        Temp = math.ceil(np_Temperature[0])
        plt.title("Current Temperature @ {} is {}°C".format(city,Temp))
        plt.legend
        plt.show()
        print("AIR PRESSURE :",data['main']['pressure'])
        print("HUMIDITY :",data['main']['humidity'])
        print("SEA LEVEL :",data['main']['sea_level'])
        print("WINDSPEED :",data['wind']['speed'],"km/hr")
    else:
        print("Error")
else:
    print("Error: Try entering the city name properly.")


