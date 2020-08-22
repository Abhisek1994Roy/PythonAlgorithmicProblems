#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import json


class Insta_Info_Scraper:

    def getinfo(self, url):
        html = urllib.request.urlopen(url, context=self.ctx).read()
        user_data = {}
        soup = BeautifulSoup(html, 'html.parser')
        data = soup.find_all('meta', attrs={'property': 'og:description'})

        script_data = soup.find_all('script', attrs={'type': 'application/ld+json'})

        script_data = (json.loads(script_data[0].text))


        text = data[0].get('content').split()

        user = '%s %s %s' % (text[-3], text[-2], text[-1])
        followers = text[0]
        following = text[2]
        posts = text[4]
        user_data["name"] = script_data["name"]
        user_data["insta_handle"] = script_data["alternateName"]
        user_data["description"] = script_data["description"]
        user_data["url"] = script_data["url"]
        user_data["image"] = script_data["image"]
        user_data["followers"] = followers
        user_data["following"] = following
        user_data["posts"] = posts
        return user_data
        print ('---------------------------')


    def main(self):
        self.ctx = ssl.create_default_context()
        self.ctx.check_hostname = False
        self.ctx.verify_mode = ssl.CERT_NONE
        user_data_list = []
        with open('users.txt') as f:
            self.content = f.readlines()
        self.content = [x.strip() for x in self.content]
        for url in self.content:
            user_data = self.getinfo(url)
            print(user_data)
            user_data_list.append(user_data)


        with open('insta_data.json', 'w', encoding="utf-8") as outfile:
            json.dump(user_data_list, outfile, indent=4, sort_keys=True)



if __name__ == '__main__':
    obj = Insta_Info_Scraper()
    obj.main()
