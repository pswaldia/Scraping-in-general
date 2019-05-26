###################################################################################################################     
#                                                                                                                 #
#              WEB SCRAPING USING BEAUTIFUL-SOUP LIBRARY , FROM goodreads website                                 # 
#              https://www.goodreads.com                                                                          #
###################################################################################################################


import requests
url=requests.get("https://www.goodreads.com/book/popular_by_date/2018")
from bs4 import BeautifulSoup
soup=BeautifulSoup(url.text,'html.parser')
result=soup.findAll('img')
links=[]
names=[]
for i in range(6,26):
    links.append(result[i].get('src'))
    names.append(result[i].get('alt'))
author=soup.findAll('a',{'class':'authorName'})
authorName=[]
for i in range(1,21):
    authorName.append(author[i].span.text)

rating=soup.findAll('span',{'class':'minirating'})
rate=[]
for i in range(20):
    rate.append(rating[i].text[:5])

import pandas as pd
df=pd.DataFrame({'Title':names,'Image':links,'Ratings':rate,'author':authorName})
df.to_csv('goodreads.csv') 

