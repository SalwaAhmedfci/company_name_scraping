# bigRating strong margRtSm h1


# !/usr/bin/env python
import requests
from bs4 import BeautifulSoup
from pip._vendor.distlib.compat import raw_input

from userAgent import randomUserAgents

companyname = raw_input("enter company name: ")
head = randomUserAgents()

page_link = "https://www.glassdoor.com/Reviews/company-reviews.htm?suggestCount=0&suggestChosen=false&clickSource" \
            "=searchBtn&typedKeyword='{0}'&sc.keyword='{1}'&locT=&locId=&jobType=".format(
        companyname, companyname)


def soup(url, headers):
    session = requests.Session()
    req = session.get(url, headers=headers)
    bs = BeautifulSoup(req.text, 'lxml')
    return bs


bs = soup(page_link, head)
rate = bs.find('span', {'class', "bigRating strong margRtSm h1"}).get_text()

print(rate)
