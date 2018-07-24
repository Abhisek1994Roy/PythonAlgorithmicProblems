import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import requests



URL = "http://py4e-data.dr-chuck.net/comments_104198.xml"
response = requests.get(URL)
xml_response=""
xml_response = response.content

data=(xml_response.decode("utf-8"))

tree = ET.fromstring(data)

results = tree.findall('comments/comment')
sum = 0
for result in results:
    sum = sum+int(result.find('count').text)
print('Sum = ',sum)
