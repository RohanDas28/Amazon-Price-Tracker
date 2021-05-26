import requests #pip install requests
from bs4 import BeautifulSoup #pip install bs4
import pygame #pip install  pygame
import os
import time
import json

#Opening The Settings.json file
with open('settings.json','r') as file:
    settings = json.load(file)

# To play a ding if the product is in our budget 
pygame.mixer.init()
pygame.mixer.music.load(settings["remind-sound-path"])

# Set your budjet
my_price = settings['budget']

# initializing Currency Symbols to substract it from our string
currency_symbols = ['€', '	£', '$', "¥", "HK$", "₹", "¥", "," ] 

# the URL we are going to use
URL = settings['url']

# Google "My User Agent" And Replace It
headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'} 

#Checking the price
def checking_price():
    page = requests.get(URL, headers=headers)
    soup  = BeautifulSoup(page.content, 'html.parser')

    #Finding the elements
    product_title = soup.find('span', id='productTitle').text.strip()
    product_price = soup.find('span', id='priceblock_ourprice').text.strip()

    # using replace() to remove currency symbols
    for i in currency_symbols : 
        product_price = product_price.replace(i, '')

    #Converting the string to integer
    product_price = int(float(product_price))


    print("The Product Name is:" ,product_title.strip())
    print("The Price is:" ,product_price)



    # checking the price
    if(product_price<my_price):
        pygame.mixer.music.play()
        print("You Can Buy This Now!")
        time.sleep(3) # audio will be played first then exit the program. This time for audio playing.
        exit()
    else:
        print("The Price Is Too High!")

while True:
    checking_price()
    time.sleep(settings['remind-time']) #It is set to run the program once in an hour! You can change by changing the value in seconds!
