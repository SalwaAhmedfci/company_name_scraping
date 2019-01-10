#bigRating strong margRtSm h1


#!/usr/bin/env python
import time
import requests
from bs4 import  BeautifulSoup
from pandas import DataFrame
from urllib.request import urlopen
from pip._vendor.distlib.compat import raw_input
from requests import get
from userAgent import user_agents, randomUserAgents
import lxml



companyname = raw_input("enter company name: ")
head = randomUserAgents()
start = time.time()

page_link ="https://www.glassdoor.com/Reviews/company-reviews.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword='{0}'&sc.keyword='{1}'&locT=&locId=&jobType=".format(companyname,companyname)



def soup(url,headers):
    session = requests.Session()
    req = session.get(url, headers=headers)
    bs = BeautifulSoup(req.text, 'lxml')
    return bs


bs = soup(page_link, head)
rate = bs.find('span', {'class', "bigRating strong margRtSm h1"}).get_text()

print(rate)
