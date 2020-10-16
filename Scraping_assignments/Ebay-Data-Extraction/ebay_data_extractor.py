#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import ssl
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

# For ignoring SSL certificate errors

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Input from user
url = input("Enter Ebay prodcut listing URL- ")

# Making the website believe that you are accessing it using a mozilla browser
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

# Creating a BeautifulSoup object of the html page for easy extraction of data.
soup = BeautifulSoup(webpage, 'html.parser')
html = soup.prettify('utf-8')
product_json = {}

# Get product title
title = soup.find('title')
product_json["title"] = title.text.strip()

# Get product price
price_span = soup.find('span', attrs={'itemprop': 'price'})
product_json["price"] = price_span.text.strip()

# Get shipping charges
shipping_cost_span = soup.find('span', attrs={'id': 'fshippingCost'})
shipping_cost_span_in = shipping_cost_span.find('span')
product_json["shipping_cost"] = shipping_cost_span_in.text.strip()

# Get product price
price_span = soup.find('span', attrs={'itemprop': 'price'})
product_json["price"] = price_span.text.strip()

# Get delivery date range
date_range_span = soup.find('span', attrs={'class': 'vi-acc-del-range'})
product_json["date_range"] = date_range_span.text.strip()

# Get reviews
product_json["reviews"] = []
for review in soup.findAll('p', attrs={'itemprop': 'reviewBody'}):
    product_json["reviews"].append(review.text.strip())

# Get data points in description
product_json["description"] = []
description_table = soup.find('table', attrs={'border': '0', 'cellspacing': '0', 'cellpadding': '0', 'width': '100%'})
td_keys = description_table.findAll('td', attrs={'valign': 'top', 'width': '35%'})
td_values = description_table.findAll('td', attrs={'valign': 'top', 'width': '65%'})
len_keys = len(td_keys)
for i in range(0, len_keys):
    product_json["description"].append({td_keys[i].text.strip(): td_values[i].text.strip()})

# Creates a json file with all the information that you extracted
with open('product_details.json', 'w') as outfile:
    json.dump(product_json, outfile, indent=4)

# Creates an html file in your local with the html content of the page you parsed.
with open('output_file.html', 'wb') as file:
    file.write(html)

print('----------Extraction of data is complete. Check json file.----------')
