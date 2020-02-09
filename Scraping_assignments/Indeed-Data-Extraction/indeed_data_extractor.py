#!/usr/bin/python
import json
import re
import ssl
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

BASE_URL = "https://www.indeed.com/"

# For ignoring SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def main():
    """
    This is the main function where different inputs are taken and the first url through which we go in is constructed
    Also, the final JSON is saved here using the data scraped
    """
    name_of_city = input('Enter the name of the city in which you want to search for jobs- ')
    keywords = input('Enter the keywords by which you want to search for jobs- ')
    number_of_pages = input('Enter the number of web pages of search results that you want to scrape for provided '
                            'keywords- ')
    name_of_city = '+'.join(name_of_city.split(' '))
    keywords = '+'.join(keywords.split(' '))
    url_to_scrape = BASE_URL + "/jobs?q=" + keywords + "&l=" + name_of_city
    number_of_pages_nos = int(number_of_pages)
    data_collected = scrape_data(url_to_scrape, number_of_pages_nos)
    with open('data.json', 'w') as fp:
        json.dump(data_collected, fp, sort_keys=True, indent=4, ensure_ascii=False)


def scrape_data(url_to_scrape, number_of_pages_nos):
    """
    This function loops through the number of pages of search results that need to be scraped and passes the data into
    another function to extract particular data points for each of the individual job post in a single page of job
    post results
    """
    data_collected = []
    for i in range(0, number_of_pages_nos):
        extension = ""
        if i is not 0:
            extension = "&start=" + str(i * 10)
        url = url_to_scrape + extension
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        web_page = urlopen(req).read()
        soup = BeautifulSoup(web_page, 'html.parser')
        html = soup.prettify('utf-8')
        name_of_html_file = "indeed" + ":" + url.split('//')[-1]
        with open(name_of_html_file + '.html', 'wb') as file:
            file.write(html)
        file.close()
        data_collected = get_data_from_webpage(data_collected, soup)
    return data_collected


def extract_data_points(job, div):
    """
    This function helps extract specific data points such as title, companyName, rating and more for each job post
    in a search result page
    """
    for a in div.findAll('a', attrs={'class': 'jobtitle turnstileLink'}):
        job['title'] = a['title']
    for a1 in div.findAll('a', attrs={'data-tn-element': 'companyName'}):
        job['companyName'] = a1.text.strip()
    for span in div.findAll('span', attrs={'class': 'ratingsContent'}):
        job['rating'] = span.text.strip()
    for span1 in div.findAll('span', attrs={'class': 'location accessible-contrast-color-location'}):
        job['location'] = span1.text.strip()
    for div1 in div.findAll('div', attrs={'class': 'summary'}):
        summary = div1.text.strip()
        job['summary'] = re.sub(' +', ' ', summary.replace("\n", ""))
    for span2 in div.findAll('span', attrs={'class': 'date'}):
        job['date'] = span2.text.strip()
    return job


def get_data_from_webpage(data_collected, soup):
    """
    This function loops through the different job posts in a single page of search results and extracts information for
    each individual job post
    """
    job_posts = []
    for div in soup.findAll('div', attrs={'class': 'jobsearch-SerpJobCard unifiedRow row result'}):
        job = dict()
        job = extract_data_points(job, div)
        job_posts.append(div['data-jk'])
        single_job_post_extension_url = "https://www.indeed.com/viewjob?jk=" + div['data-jk']
        job['url'] = single_job_post_extension_url
        req = Request(single_job_post_extension_url, headers={'User-Agent': 'Mozilla/5.0'})
        web_page = urlopen(req).read()
        job_soup = BeautifulSoup(web_page, 'html.parser')
        html = job_soup.prettify('utf-8')
        name_of_html_file = ("indeed" + ":" + single_job_post_extension_url.split('//')[-1]).split('/')[-1]
        with open(name_of_html_file + '.html', 'wb') as file:
            file.write(html)
        file.close()
        for inside_div in job_soup.findAll('div', attrs={'class': 'jobsearch-jobDescriptionText'}):
            details = inside_div.text.strip()[:100] + "..."
            job['details'] = re.sub(' +', ' ', details.replace("\n", " "))
        data_collected.append(job)
    return data_collected


if __name__ == "__main__":
    main()
    print('----------Extraction of data is complete. Check json file.----------')
