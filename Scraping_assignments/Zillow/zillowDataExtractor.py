import json
import ssl
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

# Ignore SSL Certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Take the Zillow listing URL as input
url = input('Enter Zillow House Listing Url- ')

# Making the website believe that you are accessing it using a mozilla browser
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

# Creating a BeautifulSoup object of the html page for easy extraction of data.
soup = BeautifulSoup(webpage, 'html.parser')
html = soup.prettify('utf-8')
property_details = {'details_long': {}, 'address': {}}

# Extract Title of the zillow property listing
for title in soup.findAll('title'):
    property_details['Title'] = title.text.strip()
    break

for meta in soup.findAll('meta', attrs={'name': 'description'}):
    property_details['details_short'] = meta['content'].strip()

for div in soup.findAll('div', attrs={'class': 'character-count-truncated'}):
    property_details['details_long']['Description'] = div.text.strip()

for (i, script) in enumerate(soup.findAll('script',
                                          attrs={'type': 'application/ld+json'})):
    if i == 0:
        json_data = json.loads(script.text)
        property_details['details_long']['no_of_rooms'] = json_data['numberOfRooms']
        property_details['details_long']['floor_size_in_sqrft'] = json_data['floorSize']['value']
        property_details['address']['street'] = json_data['address']['streetAddress']
        property_details['address']['locality'] = json_data['address']['addressLocality']
        property_details['address']['region'] = json_data['address']['addressRegion']
        property_details['address']['postal_code'] = json_data['address']['postalCode']
    if i == 1:
        json_data = json.loads(script.text)
        property_details['price_in_dollars'] = json_data['offers']['price']
        property_details['inage'] = json_data['image']
        break

with open('house_listing_data.json', 'w') as outfile:
    json.dump(property_details, outfile, indent=4)

with open('house_listing_data.html', 'wb') as file:
    file.write(html)

print('----------Extraction of data is complete. Check json file.----------')
