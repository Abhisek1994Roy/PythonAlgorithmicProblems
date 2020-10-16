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

# Take a Flipkart Product URL as Input from user
# url = input('Enter a Flipkart Product Page Url- ')
url = "https://www.flipkart.com/redmi-8-sapphire-blue-64-gb/p/itmd1c68a1a86f5e?pid=MOBFKPYDENDXZZ7U&lid=LSTMOBFKPYDENDXZZ7U9TT5NP&marketplace=FLIPKART&srno=b_1_1&otracker=nmenu_sub_Electronics_0_Mi&fm=organic&iid=be3beb56-8d5d-4357-9e58-0ccde76fb4f3.MOBFKPYDENDXZZ7U.SEARCH&ppt=browse&ppn=browse&ssid=c46q0kp6y80000001601039247247"

# Making the website believe that you are accessing it using a mozilla browser.
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

# Creating a BeautifulSoup object of the html page for easy extraction of data.
soup = BeautifulSoup(webpage, 'html.parser')
html_obj = soup.prettify('utf-8')

# Creating a dictionary to store the different data-points that we will extract.
product_details ={}
product_details["highlights"] = []
product_details["product_description"] = {}

# Extract average ratings, name, number of reviews, brand and image of product.
for script in soup.findAll('script', attrs={'id': 'jsonLD'}):
    json_data = json.loads(script.text)
    product_details["rating"] = json_data[0]["aggregateRating"]["ratingValue"]
    product_details["no_of_reviewers"] = json_data[0]["aggregateRating"]["reviewCount"]
    product_details["brand"] = json_data[0]["brand"]["name"]
    product_details["name"] = json_data[0]["name"]
    product_details["image"] = json_data[0]["image"]

# Extract top highlights of the product.
for li in soup.findAll('li', attrs={'class': '_2-riNZ'}):
    product_details["highlights"].append(li.text.strip())

# Extract the price of the product.
for div in soup.findAll('div', attrs={'class': '_1vC4OE _3qQ9m1'}):
    product_details["price_in_rupees"] = float(div.text.strip()[1:].replace(",",""))

# Extract key value pairs in description of the product.
description_headers = soup.findAll('div', attrs={'class': '_2THx53'})
descriptions = soup.findAll('div', attrs={'class': '_1aK10F'})

for i, description in enumerate(descriptions):
    product_details["product_description"][description_headers[i].text.strip()] \
    = description.text.strip()

# Save product dictionary to JSON file.
with open('product_details.json', 'w', encoding="utf-8") as outfile:
    json.dump(product_details, outfile, indent=4, sort_keys=True)

# Save product dictionary to JSON file.
with open('output_file.html', 'wb') as file:
    file.write(html_obj)

print('----------Extraction of data is complete. Check json file.----------')
