#Pulls JSON data from weather API and parses it for current weather in selected city. 
import requests
city = input("What city would you like to see the weather for?\n")
url = "http://api.weatherapi.com/v1/current.json?key=f4ac01d56f574f4d863192109252407&q="+city+"&aqi=no"
response = requests.get(url)
weather_json = response.json()

temp = weather_json.get("current").get("temp_f")
description = weather_json.get("current").get("condition").get("text")

print("The current weather in", city, "is", description, "and", temp, "degrees")
