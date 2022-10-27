import requests #pip install requests
from bs4 import BeautifulSoup #pip install bs4
import pygame #pip install  pygame
import os
import time
import json
from colored import fg, attr

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
    soup  = BeautifulSoup(page.text, 'html.parser')

    #Finding the elements
    product_title = soup.find('span', id='productTitle').getText()
    product_price = soup.find('span', class_ = "a-offscreen").getText()

    # using replace() to remove currency symbols
    for i in currency_symbols : 
        product_price = product_price.replace(i, '')

    #Converting the string to integer
    product_price = int(float(product_price))

    ProductTitleStrip = product_title.strip()
    print(f"{fg('green_1')}The Product Name is:{attr('reset')}{fg('dark_slate_gray_2')} {ProductTitleStrip}{attr('reset')}")
    print(f"{fg('green_1')}The Price is:{attr('reset')}{fg('orange_red_1')} {product_price}{attr('reset')}")



    # checking the price
    if(product_price<my_price):
        pygame.mixer.music.play()
        print(f"{fg('medium_orchid_1b')}You Can Buy This Now!{attr('reset')}")
        time.sleep(3) # audio will be played first then exit the program. This time for audio playing.
        exit()
    else:
        print(f"{fg('red_1')}The Price Is Too High!{attr('reset')}")

while True:
    checking_price()
    time.sleep(settings['remind-time']) #It is set to run the program once in an hour! You can change by changing the value in seconds!
