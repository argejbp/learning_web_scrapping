# This is my first web scrapping program :)
# It can tell you the current temperature
# Given a city and country


import requests as rq
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim



#It's defined a function to get the current ambient temperature of a given city 

def TempInCityCountry(latitude, longitude):

    #The url of Weather Channel is defined using latitude and logitude of the given city
    URL = "https://weather.com/weather/today/l/{},{}?par=google".format(latitude, longitude)
    weather_page = rq.get(URL)                                          #This line requests the html code of the web page using its url

    #This block of code checks if the html was downloaded correctly
    try:
        weather_page.raise_for_status()
    except Exception as exc:
        print('There was a problem: %s' %(exc))

    weather_soup = BeautifulSoup(weather_page.text, 'html.parser')                  #This line parses the html code, creating a BeautifulSoup object
    Current_Temp = weather_soup.select(".CurrentConditions--tempValue--3a50n")      #This line finds the lines of code with the class ".CurrentConditions--tempValue--3a50n", which holds the temperature 
    Temp = Current_Temp[0].getText()                                                #This line gets the text within the angle braquets of the code line 

    return Temp
    # print('\nCurrent Temperature in {}, {}: {}'.format(city, country , Temp))       #This line prints the temperature, city and country
    # print('Source: The Weather Channel')


def get_temp(city, country):
    geolocator = Nominatim(user_agent="Armando Bonilla")
    loc = geolocator.geocode(city + ',' + country)                #This line helps to locate the coordinates of the city 
    temp = TempInCityCountry(loc.latitude, loc.longitude)         #Calling the function to get the current ambient temperature of the given city 
    return temp

