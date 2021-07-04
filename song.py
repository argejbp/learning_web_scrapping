# This is my second web scrapping program :)
# It stores the lyrics of a given song 

#   HOW TO USE FROM COMMAND LINE (Windows OS)
#   py song.py artist, song

import requests as rq
from bs4 import BeautifulSoup
import sys

def get_page(link):                 #This functions makes a requests to the web page for its HTML source code
    
    page = rq.get(link)
    try:
        page.raise_for_status()
    except Exception as exc:
        print('There was a problem: %s' %(exc))
    
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup
    
def get_lyrics(l1):                 #This function gets the lyrics from the BeautifulSoup object of the web page
    dirty_lyrics = l1.find_all('div', {'class':{'lyrics'}})

    if len(dirty_lyrics) > 0:
        clean_lyrics = dirty_lyrics[0].getText()
        return clean_lyrics
    else:
        print('There was some mistake in getting the lyrics')
        return None

def songfile(lyrics):               #This functions stores the lyrics in a file
    with open('song_lyrics.txt', 'a') as text:
        for i in lyrics:
            text.write(i)
    return None
    
  

if len(sys.argv) > 1:               #This logical block of code checks if there's given arguments in the console
    
    #This block of code formats the input from the console to add it to an URL 

    info = sys.argv[1:]
    info = '-'.join(info)
    search_string = info.replace(',', '')

    #What I told you before
    URL = 'https://genius.com/{}-lyrics'.format(search_string)
    
    #Calling the previously defined functions 
    soup_page = get_page(URL)
    some_lyrics = get_lyrics(soup_page)
    songfile(some_lyrics)



else:
    #Check yourself little penguin
    print("\nYour input has less arguments than expected\nRemember you must enter: artist, song")
