import requests #pip install requests
from bs4 import BeautifulSoup #pip install bs4
import pygame #pip install  pygame
import time 

# To play a ding if the product is in our budget 
pygame.mixer.init()
pygame.mixer.music.load("ding.wav")

# Set your budjet
my_price = int(10000) 

# initializing Currency Symbols to substract it from our string
currency_symbols = ['€', '	£', '$', "¥", "HK$", "₹", "¥", "," ] 

# the URL we are going to use
URL = ('https://www.amazon.in/G731GT-Graphics-i5-9300H-Windows-G731GT-AU022T/dp/B07S36XJ8Q/ref=sr_1_3?crid=2T1YQNU9F8MMO&keywords=asus+rog+laptop&qid=1568612002&sprefix=Asus+%2Caps%2C685&sr=8-3')

# Google "My User Agent" And Replace It
headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'} 

def checking_price():

    page = requests.get(URL, headers=headers)
    soup  = BeautifulSoup(page.content, 'html.parser')

    #Finding the elements
    product_title = soup.find (id= "productTitle").get_text()
    product_price = soup.find (id= "priceblock_ourprice").get_text()

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
    else:
        print("The Price Is Too High!")

while True:
    checking_price()
    time.sleep(3600) #It is set to run the program once in an hour! You can change by changing the value in seconds!