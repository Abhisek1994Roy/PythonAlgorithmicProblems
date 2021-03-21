#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import ssl
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

# For ignoring SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Urls that need to be scraped
top_movies_url = "https://www.imdb.com/chart/top/"
top_tv_shows_url = "https://www.imdb.com/chart/toptv"


# Fetching the BeautifulSoup object of an HTML page by passing its URL
def get_web_page_content(url):
    # Making the website believe that you are accessing it using a mozilla browser
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()

    # Creating a BeautifulSoup object of the html page for easy extraction of data.
    soup = BeautifulSoup(webpage, 'html.parser')
    return soup


# Going into individual movie/tv show URL and extracting extra details
def get_extra_details(movie):
    inner_soup = get_web_page_content(movie["imdb_link"])
    div = inner_soup.find('div', attrs={'class': 'plot_summary'})
    div_summary = div.find('div', attrs={'class': 'summary_text'})
    movie["summary"] = div_summary.text.strip()
    for characters_div in div.findAll('div', attrs={'class': 'credit_summary_item'}):
        character_data = characters_div.text.strip().split("\n")
        movie[character_data[0][:-1]] = character_data[1].replace("|", "").strip()
    return (movie)


# Fetching details of n number of movie/tv shows from the IMDB lists
def get_top_rated_imdb_hits(url, file_name, nos):
    soup = get_web_page_content(url)

    divs = soup.find('tbody', attrs={'class': 'lister-list'})
    movies = []
    i = 1
    for tr in divs.findAll('tr'):
        movie = {}
        td = tr.find('td', attrs={'class': 'titleColumn'})
        a = td.find('a')
        ref = a["href"]
        movie["imdb_link"] = "https://www.imdb.com" + ref
        movie_data = td.text.strip().split("\n")
        movie["rank"], movie["name"], movie["year"] = movie_data[0].strip(), movie_data[1].strip(), \
                                                      movie_data[2].strip()
        strong = tr.find('strong')
        movie["ratings"] = strong['title'].strip()
        movie = get_extra_details(movie)
        movies.append(movie)
        i += 1
        if i > nos:
            break

    # Creates a json file with all the information that you extracted
    with open(file_name, 'w') as outfile:
        json.dump(movies, outfile, indent=4)


get_top_rated_imdb_hits(top_movies_url, 'movies.json', 10)
get_top_rated_imdb_hits(top_tv_shows_url, 'tv_shows.json', 10)

print('----------Extraction of data is complete. Check json file.----------')
