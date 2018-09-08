#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import json
from urllib.request import Request, urlopen
# For ignoring SSL certificate errors

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=input("Enter Trulia Product Url- ")



req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')
html = soup.prettify('utf-8')
product_json = {}


with open('output_file.html', 'wb') as file:
    file.write(html)

print ('----------Extraction of data is complete. Check json file.----------')
