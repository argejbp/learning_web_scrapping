# This is my first web scrapping program :)
# It can tell you the current temperature
# Given a city and country



#   HOW TO USE FROM COMMAND LINE (Windows OS)
#   py current_temperature.py city, country


import sys
import requests as rq
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim

#It's defined a function to get the current ambient temperature of a given city 

def TempInCityCountry(latitude, longitude):

    #The url of Weather Channel is defined using latitude and logitude of the given city
    URL = "https://weather.com/weather/today/l/{},{}?par=google&temp=c".format(latitude, longitude)
    weather_page = rq.get(URL)                                          #This line requests the html code of the web page using its url

    #This block of code checks if the html was downloaded correctly
    try:
        weather_page.raise_for_status()
    except Exception as exc:
        print('There was a problem: %s' %(exc))

    weather_soup = BeautifulSoup(weather_page.text, 'html.parser')                  #This line parses the html code, creating a BeautifulSoup object
    Current_Temp = weather_soup.select(".CurrentConditions--tempValue--3KcTQ")      #This line finds the lines of code with the class ".CurrentConditions--tempValue--3KcTQ", which holds the temperature 
    Temp = Current_Temp[0].getText()                                                #This line gets the text within the angle braquets of the code line 

    print('\nCurrent Temperature in {}, {}: {}'.format(city, country , Temp))       #This line prints the temperature, city and country
    print('Source: The Weather Channel')



if len(sys.argv) > 1:                                   #This logical block of code checks if there's given arguments in the console
    info = sys.argv[1:]
    info = ' '.join(info)
    info = info.split(', ')

    city = info[0]
    country = info[1]

    geolocator = Nominatim(user_agent="Armando Bonilla")
    loc = geolocator.geocode(city+','+ country)            #This line helps to locate the coordinates of the city 
    TempInCityCountry(loc.latitude, loc.longitude)          #Calling the function to get the current ambient temperature of the given city 


else:
    print("\nYour input has less arguments than expected\nRemember you must enter: City, Country")
    

