#!/usr/bin/python
import ssl
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

BASE_URL = "https://www.indeed.com/"

# For ignoring SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def main():
    # Input from user
    # name_of_city = input('Enter the name of the city in which you want to search for jobs- ')
    # keywords = input('Enter the keywords by which you want to search for jobs- ')
    # number_of_pages = input('Enter the number of web pages of search results that you want to scrape for provided keywords- ')
    name_of_city = "New York"
    keywords = "Data Science"
    number_of_pages = "3"
    name_of_city = '+'.join(name_of_city.split(' '))
    keywords = '+'.join(keywords.split(' '))
    url_to_scrape = BASE_URL + "/jobs?q=" + keywords + "&l=" + name_of_city
    number_of_pages_nos = int(number_of_pages)
    data_collected = scrape_data(url_to_scrape, number_of_pages_nos)


def scrape_data(url_to_scrape, number_of_pages_nos):
    data_collected = dict()
    for i in range(0, number_of_pages_nos):
        extension = ""
        if i is not 0:
            extension = "&start=" + str(i * 10)

        url = url_to_scrape + extension
        print("Scraping page - " + url)
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        web_page = urlopen(req).read()
        soup = BeautifulSoup(web_page, 'html.parser')
        html = soup.prettify('utf-8')
        name_of_html_file = "indeed" + ":" + url.split('//')[-1]
        with open(name_of_html_file + '.html', 'wb') as file:
            file.write(html)
        file.close()
        get_data_from_webpage(url, data_collected, soup)


def get_data_from_webpage(url, data_collected, soup):
    single_job_post_extension = "&vjk="
    print("Scraping data from web page-")
    job_posts = []
    # <div class="jobsearch-SerpJobCard unifiedRow row result" data-jk="918213ce5d43f350" data-tn-component="organicJob" id="p_918213ce5d43f350">
    for div in soup.findAll('div', attrs={'class': 'jobsearch-SerpJobCard unifiedRow row result'}):
        job_posts.append(div['data-jk'])
        print(job_posts)
        single_job_post_extension_url = "https://www.indeed.com/viewjob?jk="+div['data-jk']
        print(single_job_post_extension_url)
        req = Request(single_job_post_extension_url, headers={'User-Agent': 'Mozilla/5.0'})
        web_page = urlopen(req).read()
        job_soup = BeautifulSoup(web_page, 'html.parser')
        html = job_soup.prettify('utf-8')
        with open("abc" + '.html', 'wb') as file:
            file.write(html)
        file.close()
        for inside_div in job_soup.findAll('div', attrs={'class': 'jobsearch-jobDescriptionText'}):
            print("Came here")
            print(inside_div.text.strip())
        exit()


if __name__ == "__main__":
    main()
    print('----------Extraction of data is complete. Check json file.----------')
