import json
import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.instagram.com/explore/tags/nature/')
soup = BeautifulSoup(r.text, 'lxml')

script = soup.find('script', text=lambda t: t.startswith('window._sharedData'))
page_json = script.text.split(' = ', 1)[1].rstrip(';')
data = json.loads(page_json)

for post in data['entry_data']['TagPage'][0]['graphql']['hashtag']['edge_hashtag_to_media']['edges']:
    image_src = post['node']['thumbnail_resources'][1]['src']
    print(image_src)
