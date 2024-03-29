#!/usr/bin/env python

from instagrapi import Client
from bs4 import BeautifulSoup
from urllib.request import urlopen
from PIL import Image, ImageDraw, ImageFont
from datetime import date
import json
import holidays


# is it holiday
br_holidays = holidays.BR()
today = date.today()
if today.weekday() > 5 or today.strftime("%Y-%m-%d") in br_holidays:
    quit()

# Load config
with open('.env') as env:
    config = json.loads(env.read())

fileName = 'daily.jpg'
url = "https://economia.uol.com.br/cotacoes/bolsas"
page = urlopen(url)
html = page.read().decode("utf-8" )
soup = BeautifulSoup(html, "html.parser")


# Getting stock data from website
stockData = []
for trSections in soup.find("section", class_="stock-rankings").div.find_all("tr")[:10]:
    stockData.append(trSections.get_text("|", strip=True).split("|"))


# Set up image
img = Image.new('RGB', (1000, 1000), color = (73, 109, 137))
fnt = ImageFont.truetype('arialBold.ttf', 70)
d = ImageDraw.Draw(img)
d.text((200, 0), '= ' + today.strftime("%d/%m/%Y") + ' =', font=fnt, fill=(255, 255, 0))


# Insert stock image
for stockIndex in range(len(stockData)):
    stockData[stockIndex][0] = stockData[stockIndex][0].replace('.SA', '')
    d = ImageDraw.Draw(img)
    
    color = (0, 255, 0)
    if stockData[stockIndex][1][0] == '-':
        color = (255, 76, 76)
            
    d.text((0,(stockIndex+1.5) *80), ' '+" ".join(stockData[stockIndex]), font=fnt, fill=color)

img.save(fileName,quality="maximum")


# Send to insta
cl = Client()
cl.login(config['INSTA_USERNAME'], config['INSTA_PASSWORD'])
cl.photo_upload(fileName, 'Stocks ' + today.strftime("%d/%m/%Y"))

