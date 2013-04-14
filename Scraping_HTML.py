"""
Using mechanize and BeautifulSoup
"""
import mechanize
from bs4 import BeautifulSoup
import re
from django.utils.encoding import smart_str

def scrape_info(base_url, data):
    soup = BeautifulSoup(data)
    for findInfo in soup.findAll('a', {"class": False, "href":re.compile("^/article/")}):
        print "Title : ", smart_str(findInfo.string)
        print "URL:", findInfo['href']

def getSourceCode(BASE_URL):
    br = mechanize.Browser()
    data = br.open(BASE_URL).get_data()
    scrape_info(BASE_URL, data)

    
if __name__ == "__main__":
    getSourceCode("http://www.packtpub.com/article-network")
