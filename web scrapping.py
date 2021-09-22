#!/usr/bin/env python
# coding: utf-8

# In[2]:



import pandas as pd
import requests
from bs4 import BeautifulSoup

baseurl = 'https://www.tunisianet.com.tn/'

headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}

productlinks=[]
for x in range(1,16):
    r = requests.get(f"https://www.tunisianet.com.tn/301-pc-portable-tunisie?page={x}")
    
    soup = BeautifulSoup(r.content,'lxml')
    
    productlist = soup.find_all('div', class_='wb-image-block col-lg-3 col-xl-3 col-md-4 col-sm-4 col-xs-6')
    for item in productlist :
          for link in item.find_all('a', href=True):
              productlinks.append(link['href'])
print((productlinks))

laptoplist=[]
for link in productlinks :
    r = requests.get(link, headers = headers)
    soup = BeautifulSoup(r.content,'lxml') 
    price = soup.find('div',class_='current-price').span.text.strip()
    name = soup.find('div',class_='row probg').h1.text.strip()
    
    laptops={
              'nom': name,
              'prix': price
              } 
    laptoplist.append(laptops)
    df = pd.DataFrame(laptoplist)
# print(df)
path = ('laptopsTunisianet.csv')
df.to_csv(path, encoding='utf-8-sig')


# In[ ]:




