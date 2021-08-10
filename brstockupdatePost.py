#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# In[ ]:


from instagrapi import Client
from bs4 import BeautifulSoup
from urllib.request import urlopen
from PIL import Image, ImageDraw, ImageFont
from datetime import date
import json
import holidays


# In[ ]:


# is it holiday
br_holidays = holidays.BR()
today = date.today()

if today.weekday() > 5 or today.strftime("%Y-%m-%d") in br_holidays:
    #quit()
    pass


# In[ ]:


# Load config
with open('.env') as env:
    config = json.loads(env.read())

fileName = 'daily.jpg'
url = "https://economia.uol.com.br/cotacoes/bolsas"
page = urlopen(url)
html = page.read().decode("utf-8" )
soup = BeautifulSoup(html, "html.parser")


# In[ ]:


stockData = []

for trSections in soup.find("section", class_="stock-rankings").div.find_all("tr")[:10]:
    stockData.append(trSections.get_text("|", strip=True).split("|"))


# In[ ]:


#stockData.insert(0, ['= ' + today.strftime("%d/%m/%Y") + ' ='])

img = Image.new('RGB', (1000, 1000), color = (73, 109, 137))
fnt = ImageFont.truetype('env/arialBold.ttf', 70)
d = ImageDraw.Draw(img)
d.text((200, 0), '= ' + today.strftime("%d/%m/%Y") + ' =', font=fnt, fill=(255, 255, 0))


# In[ ]:


for stockIndex in range(len(stockData)):
    stockData[stockIndex][0] = stockData[stockIndex][0].replace('.SA', '')
    d = ImageDraw.Draw(img)
    
    color = (0, 255, 0)
    if stockData[stockIndex][1][0] == '-':
        color = (255, 76, 76)
            
    d.text((0,(stockIndex+1.5) *80), ' '+" ".join(stockData[stockIndex]), font=fnt, fill=color)

img.save(fileName,quality="maximum")
#display(img)


# In[ ]:


cl = Client()
cl.login(config['INSTA_USERNAME'], config['INSTA_PASSWORD'])


# In[ ]:


cl.photo_upload(fileName, 'this is a test')

