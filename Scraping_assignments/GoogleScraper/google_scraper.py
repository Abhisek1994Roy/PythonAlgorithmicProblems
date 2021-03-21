#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import json
import re
import ast
import os
import urllib
from urllib.request import Request, urlopen

# For ignoring SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Input from user
search_term = input('Enter search term- ')
number_of_results = input('Enter number of results you are looking for- ')

# Creating the URL we need to scrape
query = urllib.parse.quote_plus(search_term) # Format into URL encoding
url = "https://www.google.com/search?q=" + query + "&num=" + str(number_of_results)

# Making the website believe that you are accessing it using a mozilla browser
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

# Creating a BeautifulSoup object of the html page for easy extraction of data.
soup = BeautifulSoup(webpage, 'html.parser')
html = soup.prettify('utf-8')


# Extracting the required data points into an array
res_arr = []
result_div = soup.find_all('div', attrs = {'class': 'ZINbbc'})
for r in result_div:
    # Checks if each element is present, else, raise exception
    try:
        link = r.find('a', href = True)
        title = r.find('div', attrs={'class':'vvjwJb'}).get_text()
        description = r.find('div', attrs={'class':'s3v9rd'}).get_text()

        # Check to make sure everything is present before appending
        if link != '' and title != '' and description != '':
            res = {}
            res["title"] = title
            url = re.search("(?P<url>https?://[^\s]+)", link['href']).group("url")
            url = url[:url.index("&")]
            res["link"] = url
            res["description"] = description
            res_arr.append(res)
    # Next loop if one element is not present
    except:
        continue

# Saving the results JSON
with open('google_results.json', 'w') as outfile:
    json.dump(res_arr, outfile, indent=4)

# Creates an html file in your local with the html content of the page you parsed.
with open('output_file.html', 'wb') as file:
    file.write(html)
