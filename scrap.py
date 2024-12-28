from bs4 import BeautifulSoup
from os import system
from time import sleep
from requests import get

while True:
    URL = "https://giftcardpro.com.br/produto/comprar-boosteroid-cloud-gaming-1-mes/"
    page = get(URL)

    soup = BeautifulSoup(page.text, 'html.parser')

    stock = soup.find("p", class_="out-of-stock")
    
    if stock == None or stock.text.lower() != 'fora de estoque':
        system('notify-send "Boosteroid Update" "The boosteroid gift card is now in stock!"')

    sleep(3600)