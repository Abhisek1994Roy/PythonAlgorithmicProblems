import json
import ssl
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

# For ignoring SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter Quora Url that you want to scrape')
# url = "https://www.quora.com/Should-I-move-to-London"

# Hitting the Quora Url and extracting the HTML content
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

# Creating a BeautifulSoup object of the html page for easy extraction of data.
soup = BeautifulSoup(webpage, 'html.parser')

quora_json = dict()

# Extracting the question.
question = soup.find("title")
quora_json["question"] = question.text.replace(" - Quora", "")

# Extracting the answers.
quora_json["answers"] = []
answers = soup.find("script", {"type": "application/ld+json"})
ans_list = json.loads(answers.text)["mainEntity"]["suggestedAnswer"]
for answer in ans_list:
    answer_val = {"dateCreated": answer["dateCreated"],
                  "text": answer["text"],
                  "upvoteCount": answer["upvoteCount"]}
    quora_json["answers"].append(answer_val)

# Saving the json file
with open('quora_data.json', 'w') as outfile:
    json.dump(quora_json, outfile, indent=4)
