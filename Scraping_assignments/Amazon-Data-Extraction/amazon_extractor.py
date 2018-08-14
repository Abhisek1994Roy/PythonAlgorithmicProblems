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
for line in soup.find_all('span',attrs={"id" : "price_inside_buybox"}):
    details = line.text.strip()
    print(details)
print("-------------------------------------------------------")
for line in soup.find_all('span',attrs={"id" : "productTitle"}):
    details = line.text.strip()
    print(details)
print("-------------------------------------------------------")
# div_container = soup.findall("li")
# for container in div_container:
#     print(container.text.strip())
#
# >>> BeautifulSoup.BeautifulSoup("""<html><td width="50%">
# ...     <strong class="sans"><a href="http:/website">Site</a></strong> <br />
# ... </html>""" )
# <html><td width="50%">
# <strong class="sans"><a href="http:/website">Site</a></strong> <br />
# </td></html>
for item in soup.findAll('ul', attrs={'class':'a-unordered-list a-vertical a-spacing-none'}):
     for in_item in item.findAll('li'):
         for in_in_item in in_item.findAll('span', attrs={'class':'a-list-item'},text=True, recursive=False) :
             print(in_in_item.text.strip())
# print([ span for span in li.findall("span", attrs={"class" : "a-list-item"})
#             for li in ul.findall("li")
#             for ul in soup.findall("ul", attrs={"class" : "a-unordered-list a-vertical a-spacing-none"})])
# for line in soup.find_all('ul',attrs={"class" : "a-unordered-list a-vertical a-spacing-none"}):
#     for inner_lines in soup.findChildren('li'):
#         for inner_inner_lines in soup.findChildren('span',attrs={"class" : "a-list-item"}):
#             print(inner_inner_lines.text.split())

# for ptag in div_container.findall('span',attrs={"class" : "a-list-item"}):
#     details = line.text.strip()
#     print(details)
# print(''.join(i.text.strip() for i in soup.select('ul[class="a-unordered-list a-vertical a-spacing-none"] > li > span[class="a-list-item"]')))
with open("output0.html", "wb") as file:
    file.write(html)
