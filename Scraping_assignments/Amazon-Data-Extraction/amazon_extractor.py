import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import json
import re
import sys
import warnings

if not sys.warnoptions:
    warnings.simplefilter("ignore")


#For ignoring SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter url - ' )
url=input("Enter Amazon Product Url- ")
# url="https://www.amazon.com/VivoBook-Lightweight-WideView-i5-8250U-Fingerprint/dp/B0795W86N3/ref=pd_sbs_147_3?_encoding=UTF8&pd_rd_i=B0795W86N3&pd_rd_r=8V90JTCPH5089W6PQ1R9&pd_rd_w=Ssao6&pd_rd_wg=kUHhj&psc=1&refRID=8V90JTCPH5089W6PQ1R9"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

html = soup.prettify("utf-8")
hotel_json = {}


print("-------------------------------------------------------")
for line in soup.findAll('span',attrs={"id" : "price_inside_buybox"}):
    details = line.text.strip()
    print(details)
print("-------------------------------------------------------")
for line in soup.findAll('span',attrs={"id" : "productTitle"}):
    details = line.text.strip()
    print(details)
print("-------------------------------------------------------")
for item in soup.findAll('ul', attrs={'class':'a-unordered-list a-vertical a-spacing-none'}):
     for in_item in item.findAll('li'):
         for in_in_item in in_item.findAll('span', attrs={'class':'a-list-item'},text=True, recursive=False) :
             print(in_in_item.text.strip())
print("-------------------------------------------------------")
for line in soup.findAll('a',attrs={"class" : "a-size-base a-link-normal review-title a-color-base a-text-bold"}):
    details = line.text.strip()
    print(details)
print("-------------------------------------------------------")
for line in soup.findAll('div',attrs={"class" : "a-expander-content a-expander-partial-collapse-content"}):
    details = line.text.strip()
    print(details)
print("-------------------------------------------------------")
for item_new in soup.findAll('i', attrs={'data-hook':'average-star-rating'}):
     for in_item_new in item_new.findAll('span', attrs={'class':'a-icon-alt'}):
             print(in_item_new.text.strip())
print("-------------------------------------------------------")
for line in soup.findAll('span',attrs={"id" : "acrCustomerReviewText"}):
    if (line.text):
        details = line.text.strip()
        print(details)
        break
print("-------------------------------------------------------")
for item_new in soup.findAll('div', attrs={'id':'rwImages_hidden'}):
     for in_item_new in item_new.findAll('img', attrs={'style':'display:none;'}):
             print(in_item_new['src'])
print("-------------------------------------------------------")
# <div class="a-box-group" data-asin="B079J3NWYZ" data-brand="Lenovo" data-product-group="pc_display_on_website" data-timeout="Sorry we encountered a problem." id="mbc">
for item_new in soup.findAll('div', attrs={'class':'a-box-group'}):
    try:
         print(item_new['data-brand'])
         break
    except:
        pass
print("--------------------------------------------------------")
with open("output0.html", "wb") as file:
    file.write(html)
