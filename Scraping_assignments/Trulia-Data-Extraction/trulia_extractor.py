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

url=input("Enter Trulia Product Url- ")



req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')
html = soup.prettify('utf-8')
product_json = {}

for meta in soup.findAll('meta', attrs={'name': 'description'}):
    try:
        product_json['description'] = meta['content']
        break
    except:
        pass

for link in soup.findAll('link', attrs={'rel': 'canonical'}):
    try:
        product_json['link'] = link['href']
        break
    except:
        pass
for scripts in soup.findAll('script', attrs={'type': 'application/ld+json'}):
    details_json = ast.literal_eval(scripts.text.strip())
product_json["price"]={}
product_json["price"]["amount"]=details_json["offers"]["price"]
product_json["price"]["currency"]=details_json["offers"]["priceCurrency"]

for paragraph in soup.findAll('p', attrs={'id': 'propertyDescription'}):
    product_json["broad-description"] = paragraph.text.strip()
product_json["overview"]=[]
for divs in soup.findAll('div', attrs={'data-auto-test-id':'home-details-overview'}):
    for divs_second in divs.findAll('div'):
        for uls in divs_second.findAll('ul'):
            for lis in uls.findAll('li', text=True, recursive=False):
                product_json["overview"].append(lis.text.strip())



with open('house_details.json', 'w') as outfile:
    json.dump(product_json, outfile, indent=4)


with open('output_file.html', 'wb') as file:
    file.write(html)


print ('----------Extraction of data is complete. Check json file.----------')
