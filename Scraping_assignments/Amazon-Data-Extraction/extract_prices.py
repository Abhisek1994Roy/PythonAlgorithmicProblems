import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import sys
import warnings
from requests_html import HTMLSession
session = HTMLSession()
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
headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'
    }
#Next step is creating the urls by appending https://www.amazon.com/dp/ to the asin number and then accessing the price
#from the html

for asin in asin_array:
    amazon_url="https://www.amazon.com/dp/"+asin
    # print(amazon_url)
    # page = urlopen(amazon_url)
    # soup = BeautifulSoup(page, 'html.parser')
    # price_box = soup.find('span', attrs={'id':'priceblock_ourprice'})
    # price = price_box.text
    # print (price)
    response = requests.get(amazon_url, headers=headers, verify=False)
    html_file=str(response.text)
    print(type(response.text))
    # html_file=response.text
    # print(html_file)
    print ('a-color-price' in html_file)
    index = html_file.find('a-color-price')
    print("index", index)
    price=""
    print("FOUND")
    print(html_file[index:index+100])
    for i in range(index, index+1000):
        flag=False
        if html_file[i]=="$":

            exit()
            for j in range(i+1,i+10):
                if html_file[j]=="<":
                    flag=True
                    break
                else:
                    price=price+html_file[j]
            if flag==True:
                break
    print("price",price)
    break


    exit()
