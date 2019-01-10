#bigRating strong margRtSm h1


#!/usr/bin/env python
import time
import requests
from bs4 import  BeautifulSoup
from pandas import DataFrame
from urllib.request import urlopen
from pip._vendor.distlib.compat import raw_input

from userAgent import user_agents, randomUserAgents
import lxml



companyname = raw_input("enter company name: ")


page_link ="https://www.glassdoor.com/Reviews/company-reviews.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword='{0}'&sc.keyword='{1}'&locT=&locId=&jobType=".format(companyname,companyname)
head = randomUserAgents()


r = requests.get(page_link,head)

data = r.text

soup = BeautifulSoup(data,'lxml')
print(soup)
for rate in soup.find_all('span', class_='bigRating strong margRtSm h1'):

    print(rate)