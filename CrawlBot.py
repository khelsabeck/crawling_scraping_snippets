from bs4 import BeautifulSoup
import requests
import csv
import lxml
import time
import random
import csv
import os
'''
This is from a scraper script. The particulars have been largely removed
'''
class CrawlBot:
    prefix = "http..."                  # prefix for the pages below

    def __init__(self, extension):
        try:
            self.mainfile = self.get_mainpage(self.prefix, extension)
            self.soup = self.get_soup(self.mainfile)
            self.complete_urls = self.url_completer(self.prefix, self.text_urls)
            self.write_csv(self.prefix, self.text_urls) #if this writes, you have some urls for textfiles
            self.write_textfiles(self.prefix, self.text_urls, self.county)
        except:
            time.sleep(60)
            cb = CrawlBot(filename)


    @staticmethod
    def get_mainpage(prefix, filename):
        s = prefix + filename
        headers = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
            'referer': 'https ...',
            "Accept-Encoding":"gzip, deflate", 
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
            "DNT":"1",
            "Connection":"close", 
            "Upgrade-Insecure-Requests":"1"
        }
        time.sleep(3)

        first_get = requests.get('http ...', headers=headers, timeout=60).text

        time.sleep(3)
        print("let's try another")  
        headers = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
            'referer': 'http ...',
            "Accept-Encoding":"gzip, deflate", 
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
            "DNT":"1",
            "Connection":"close", 
            "Upgrade-Insecure-Requests":"1"
        }

        big_get = requests.get(s, headers=headers, timeout=60).text
        return big_get

    '''This should get and return a soup object of the main page with all the text ready to parse'''
    def get_soup(self, mainfile):
        return BeautifulSoup(mainfile, features="lxml") 

    '''This should return ALL the hrefs (including ones you don't want)'''
    def get_all_urls(self, soup):
        return [ link.get('href') for link in soup.find_all('a') ]

    '''This should take a url from the url list and splice it to make a full url path'''
    @staticmethod
    def url_completer(prefix, l_urls):
        return [ f"{prefix}{url}" for url in l_urls ]

    '''Creates bot objects and delegates further parsing to those bots'''
    @staticmethod
    def text_ref_getter(l_urls, soup):
        # if so-and-so is valid:
        bot = MyBot(l_urls)
        return crim.l_complete_urls
        # else:
        #     raise ValueError("Data error from CrawlBot in text_url_getter. Check urls above.")


# '''
# Bot for parsing out details.
# '''
# class MyBot:
#     def __init__(self, l_urls):
#         self.l_complete_urls = self.text_url_getter(l_urls)
#         self.napster()

#     '''If one of the url links ends in txt, return it in a list. Else, ditch it.'''
#     @staticmethod
#     def text_url_getter(l_urls):
#         try:
#             l_out = [ url for url in l_urls if url[-4:] == ".txt" ]   
#             l_unique = []
#             for url in l_out:
#                 if url not in l_unique:
#                     l_unique.append(url) 
#             return l_unique
#         except:
#             pass

#     '''This just gives it a short nap'''
#     @staticmethod
#     def napster():
#         r = random.uniform(2.5, 4)
#         time.sleep(r)