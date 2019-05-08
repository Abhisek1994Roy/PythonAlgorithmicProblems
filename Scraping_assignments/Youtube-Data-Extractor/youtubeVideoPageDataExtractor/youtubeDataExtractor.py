#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import json
import ast
import os
from urllib.request import Request, urlopen

# For ignoring SSL certificate errors

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Input from user

url = input('Enter Youtube Video Url- ')

# Making the website believe that you are accessing it using a mozilla browser

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

# Creating a BeautifulSoup object of the html page for easy extraction of data.

soup = BeautifulSoup(webpage, 'html.parser')
html = soup.prettify('utf-8')
company_json = {}
other_details = {}

# button title="I like this"  - number of likes
# button title="I dislike this"  - number of dislikes
# span class="watch-title"  - Title
# div class="watch-view-count"
# span class="yt-subscription-button-subscriber-count-branded-horizontal yt-subscriber-count"
# <span class="standalone-collection-badge-renderer-text">
# <a class="yt-uix-sessionlink" data-sessionlink="ei=SRLTXN-9IuW5z7sPkYeDiAI" data-url="/results?search_query=%23GameOfThrones" href="/results?search_query=%23GameOfThrones">
# #GameOfThrones
# </a>
# <a class="yt-uix-sessionlink" data-sessionlink="ei=SRLTXN-9IuW5z7sPkYeDiAI" data-url="/results?search_query=%23RaminDjawadi" href="/results?search_query=%23RaminDjawadi">
# #RaminDjawadi
# </a>
# <a class="yt-uix-sessionlink" data-sessionlink="ei=SRLTXN-9IuW5z7sPkYeDiAI" data-url="/results?search_query=%23TheNightKing" href="/results?search_query=%23TheNightKing">
# #TheNightKing
# </a>
# </span>

# for span in soup.findAll('span',
#                          attrs={'class': 'Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)'
#                          }):
#     company_json['PRESENT_VALUE'] = span.text.strip()

# for div in soup.findAll('div', attrs={'class': 'D(ib) Va(t)'}):
#     for span in div.findAll('span', recursive=False):
#         company_json['PRESENT_GROWTH'] = span.text.strip()
#
# for td in soup.findAll('td', attrs={'data-test': 'PREV_CLOSE-value'}):
#     for span in td.findAll('span', recursive=False):
#         other_details['PREV_CLOSE'] = span.text.strip()
#
# for td in soup.findAll('td', attrs={'data-test': 'OPEN-value'}):
#     for span in td.findAll('span', recursive=False):
#         other_details['OPEN'] = span.text.strip()

with open('output_file.html', 'wb') as file:
    file.write(html)

print ('----------Extraction of data is complete. Check json file.----------')
