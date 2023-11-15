#Task 1: Build a Web Scraper
# level 3
import requests
from bs4 import BeautifulSoup
#requests library is used send a get request to the given website link
response=requests.get("https://www.hindustantimes.com/world-news")
#The response from the website is stored in "response" variable
a=BeautifulSoup(response.content,"html.parser")#html content of the response
title=a.title.text
paras=a.find_all("p")
print(title)
for i in paras:
    print(i.text)