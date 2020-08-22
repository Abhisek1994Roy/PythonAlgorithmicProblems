#!/usr/bin/python
# -*- coding: utf-8 -*-
from w3lib.html import replace_entities
import urllib.request
import urllib.parse
import urllib.error
import urllib
from bs4 import BeautifulSoup
import ssl
import json
import ast
import unicodedata
import os
from urllib.request import Request, urlopen
import html

# For ignoring SSL certificate errors

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Input from user
x="https://www.yelp.com/biz/pizza-due-san-francisco"
url = x

# Making the website believe that you are accessing it using a mozilla browser

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

# Creating a BeautifulSoup object of the html page for easy extraction of data.

soup = BeautifulSoup(webpage, 'html.parser')
html_obj = soup.prettify('utf-8')
business_details = {}

for script in soup.findAll('script',attrs={'type': 'application/ld+json'}):
    json_data = json.loads(script.text)
    business_details["phone_number"] = json_data["telephone"]
    business_details["address"] = json_data["address"]
    business_details["rating"] = json_data["aggregateRating"]["ratingValue"]
    business_details["reviewCount"] = json_data["aggregateRating"]["reviewCount"]
    business_details["cuisine"] = json_data["servesCuisine"]
    break

for script in soup.findAll('script',attrs={'data-hypernova-key': 'yelp_main__02006bb1cd717585d09de8af0d3cb8c8190a0379__yelp_main__BizDetailsApp__dynamic'}):
    json_data = json.loads(script.text[4:-3])
    business_details["business_features"] = []
    business_details["reviews"] = []
    business_details["photo_urls"] = []
    business_details["timing"] = []
    business_details["business_name"] = json_data["bizDetailsPageProps"]["businessName"]
    for feature in json_data["bizDetailsPageProps"]["moreBusinessInfoProps"]["businessInfoItems"]:
        business_details["business_features"].append(feature["title"])
    for review in json_data["bizDetailsPageProps"]["reviewFeedQueryProps"]["reviews"]:
        review_json = {}
        review_json["comment"] = review["comment"]["text"]
        review_json["rating"] = review["rating"]
        business_details["reviews"].append(review_json)
    for photo in json_data["bizDetailsPageProps"]["photoHeaderProps"]["photoHeaderMedias"]:
        business_details["photo_urls"].append(photo["srcUrl"])
    for timing in json_data["bizDetailsPageProps"]["bizHoursProps"]["hoursInfoRows"]:
        timing_json = {}
        timing_json["hours"] = timing["hoursInfo"]["hours"]
        timing_json["day"] = timing["hoursInfo"]["day"]
        business_details["timing"].append(timing_json)


with open('business_details.json', 'w', encoding="utf-8") as outfile:
    json.dump(business_details, outfile, indent=4, sort_keys=True)

with open('output_file.html', 'wb') as file:
    file.write(html_obj)

print ('----------Extraction of data is complete. Check json file.----------')
