import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter url: ')
if len(url) < 1:
    exit()
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
try:
    js = json.loads(data)
except:
    js = None
if not js:
    exit()
else:
    json_data = js
print(json_data)

comments = json_data["comments"]
sum=0

for comment in comments:
    sum = sum + comment["count"]
print("sum= ",sum)
