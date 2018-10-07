import requests
from bs4 import BeautifulSoup

html = requests.get('https://www.instagram.com/cristiano/') # input URL here
soup = BeautifulSoup(html.text, 'lxml')

data = soup.find_all('meta', attrs={'property':'og:description'})
text = data[0].get('content').split()

user = '%s %s %s' % (text[-3], text[-2], text[-1])
followers = text[0]
following = text[2]

print('User:', user)
print('Followers:', followers)
print('Following:', following)
