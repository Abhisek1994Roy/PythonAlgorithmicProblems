#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import ssl
import urllib.error
import urllib.parse
import urllib.request

from bs4 import BeautifulSoup


class InstaInfoScraper:

    def getinfo(self, url):
        # Make a http call to the given url to get the HTML page
        html = urllib.request.urlopen(url, context=self.ctx).read()
        user_data = {}

        # Create a beautifulSoup object of the html page
        soup = BeautifulSoup(html, 'html.parser')

        # Extract data in meta tag
        meta_data = soup.find_all('meta', attrs={'property': 'og:description'})
        meta_data = meta_data[0].get('content').split()

        # Extract data in script tag
        script_data = soup.find_all('script', attrs={'type': 'application/ld+json'})
        script_data = (json.loads(script_data[0].text))

        # Extract all the values needed
        user_data["name"] = script_data["name"]
        user_data["insta_handle"] = script_data["alternateName"]
        user_data["description"] = script_data["description"]
        user_data["url"] = script_data["url"]
        user_data["image"] = script_data["image"]
        user_data["followers"] = meta_data[0]
        user_data["following"] = meta_data[2]
        user_data["posts"] = meta_data[4]
        return user_data

    def main(self):
        # For ignoring SSL certificate errors
        self.ctx = ssl.create_default_context()
        self.ctx.check_hostname = False
        self.ctx.verify_mode = ssl.CERT_NONE

        # List that will contain insta data for multiple users
        user_data_list = []

        # Opening the text file and looping over users
        with open('users.txt') as f:
            self.content = f.readlines()

        # Separating the urls and storing in an array
        self.content = [x.strip() for x in self.content]

        # Looping over the array, getting data for each and appending to the list created before
        for url in self.content:
            user_data = self.getinfo(url)
            user_data_list.append(user_data)

        # Storing the list in a json file
        with open('insta_data.json', 'w', encoding="utf-8") as outfile:
            json.dump(user_data_list, outfile, indent=4, sort_keys=True)


if __name__ == '__main__':
    obj = InstaInfoScraper()
    obj.main()
