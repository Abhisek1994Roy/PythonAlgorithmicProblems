import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import sys
import warnings


if not sys.warnoptions:
    warnings.simplefilter("ignore")

url_array=[]
asin_array=[]
with open('asin_list.csv', 'r') as csvfile:
    asin_reader = csv.reader(csvfile)
    for row in asin_reader:
        url_array.append(row[0]) #This url list is an array containing all the urls from the excel sheet

#The ASIN Number will be between the dp/ and another /
start = 'dp/'
end = '/'
for url in url_array:
    asin_array.append(url[url.find(start)+len(start):url.rfind(end)])
#Now the array asin_array has the asin numbers of the urls

#For ignoring SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
asin_array = [asin_array[0]]

for i,asin in enumerate(asin_array):
    url="https://www.amazon.com/dp/"+asin
    print(url)
    # html = urllib.request.urlopen(url, context=ctx).read()
    # soup = BeautifulSoup(html, 'html.parser')
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    html = soup.prettify("utf-8")
    # for line in soup.find_all('span',attrs={"class" : "a-size-medium a-color-price"}):
    #     print (line.text.strip())
    # for line in soup.find_all('span',attrs={"id" : "productTitle"}):
    #     print (line.text.strip())
    # for line in soup.find_all('span',attrs={"class" : "a-list-item"}):
    #     print (line.text.strip())
    with open("output"+str(i)+".html", "wb") as file:
        file.write(html)
