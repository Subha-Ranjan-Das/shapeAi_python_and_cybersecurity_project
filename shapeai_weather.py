# -*- coding: utf-8 -*-
"""shapeai_weather.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ny1kv09tpTvKYM2S3RmdKNWUPZoAzq3f
"""

import requests
from datetime import datetime


api_key = '5bd53b857cdfaeef5a5ea39ac2dafef8'
location = input("Enter the city name:")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()


temp_city = ((api_data['main']['temp'])- 273.15 )
weather_desc = (api_data['weather'][0]['description'])
hmdt = (api_data['main']['humidity'])
wind_spd = (api_data['wind']['speed'])
date_time = datetime.now().strftime("%d %b %y | %I:%M:%S %p ")

print("-----------------------------------------------------")
print("Weather stats for - {} || {}".format(location.upper(), date_time))
print("-----------------------------------------------------")
print("Current temperature is: {:.2f} deg C".format(temp_city))
print("current weather desc  :",weather_desc)
print("current Humidity      :",hmdt,'%')
print("current wind speed    :",wind_spd , 'kmph')


with open('weather.txt','w') as f:
 f.write("-----------------------------------------------------------------\n")
 f.write("Weather stats for - {} || {}\n".format(location.upper(), date_time))
 f.write("------------------------------------------------------------------\n")
 f.write("Current temperature is: {:.2f} deg C\n".format(temp_city))
 f.write("current weather desc  :"+weather_desc+"\n")
 f.write("current Humidity      :"+str(hmdt)+'% \n')
 f.write("current wind speed    :"+str(wind_spd)+ 'kmph')