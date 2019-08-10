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

url = input('Enter Zillow House Listing Url- ')

# Making the website believe that you are accessing it using a mozilla browser

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

# Creating a BeautifulSoup object of the html page for easy extraction of data.

soup = BeautifulSoup(webpage, 'html.parser')
html = soup.prettify('utf-8')
company_json = {}
other_details = {}


  # <title>
  #  106 Hathaway Cir, Arlington, MA 02476 | MLS #72543381 | Zillow
  # </title>


  # <meta content="106 Hathaway Cir , Arlington, MA 02476-7251 is a single-family home listed for-sale at $669,000. The 1,520 sq. ft. home is a 3 bed, 3.0 bath property. Find 27 photos of the 106 Hathaway Cir home on Zillow. View more property details, sales history and Zestimate data on Zillow. MLS # 72543381" name="description"/>


  # <div class="character-count-truncated" style="white-space:pre-wrap;font-size:15px;line-height:1.5;max-height:180px">
  #  This spotless split-level ranch home built in 1959 has been so well maintained by the original owner who grew up there! Theres a reason this home hasnt changed hands for so long - tucked into a welcoming neighborhood close to the Dallin School, Route 2 &amp; Arlington Heights, this is a keeper for the long run. There are hardwood floors throughout the main level, including a dining room, a bright and sunny living room with a large picture window, cozy fireplace and cathedral-like ceilings. The adorable shiny kitchen is the perfect place to cook your favorite meals. The lower level has a mudroom plus a bonus den/office space and bathroom. The upper level has 3 good-sized bedroom, main bath &amp; an additional ½ bath. The immaculate basement offers plenty of storage with a new furnace, water heater and french drain. There is a one-car garage, and a large fenced-in backyard w/ sun &amp; shade for all of your gardening needs. This is a perfect place to call home and a chance to put down your roots!
  # </div>




company_json['OTHER_DETAILS'] = other_details

# with open('data1.json', 'w') as outfile:
#     json.dump(company_json, outfile, indent=4)
#
# print (company_json)

with open('output_file.html', 'wb') as file:
    file.write(html)

print ('----------Extraction of data is complete. Check json file.----------')
