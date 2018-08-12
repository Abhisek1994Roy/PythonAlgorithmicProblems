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
asin = asin_array[0]


url="https://www.amazon.com/dp/"+asin
# url = "https://www.amazon.com/gp/product/B07B7VFTN9/ref=s9_acss_bw_cg_PCLTMC_2c1_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-2&pf_rd_r=SSDYAYT34YR4C031K772&pf_rd_t=101&pf_rd_p=72bc8b37-11a2-462e-8b84-7e8ad1988c7f&pf_rd_i=565108"
# print(url)
hdr = {
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
req = urllib.request.Request(url, headers=hdr)
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, 'html.parser')
html = soup.prettify("utf-8")
for line in soup.find_all('span',attrs={"class" : "a-size-medium a-color-price"}):
    print (line.text.strip())
print("--------------------------------------------------------------------------------------------------")
for line in soup.find_all('script',attrs={"data-a-state" : '{"key":"vas-common-vm"}'}):
    print (line.text.strip())
print("--------------------------------------------------------------------------------------------------")
for line in soup.find_all('script',attrs={"data-a-state" : '{"key":"turbo-checkout-page-state"}'}):
    print (line.text.strip())
print("--------------------------------------------------------------------------------------------------")
for line in soup.find_all('span',attrs={"class" : "arp-rating-out-of-text"}):
    print (line.text.strip())
print("--------------------------------------------------------------------------------------------------")
for line in soup.find_all('span',attrs={"class" : "a-list-item"}):
    print (line.text.strip())
print("--------------------------------------------------------------------------------------------------")
for line in soup.find_all('span',attrs={"class" : "a-size-base a-color-secondary header-price a-text-normal"}):
    print (line.text.strip())
print("--------------------------------------------------------------------------------------------------")
with open("output0.html", "wb") as file:
    file.write(html)
