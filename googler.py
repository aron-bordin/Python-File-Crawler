from bs4 import  BeautifulSoup
from urllib.request import Request, urlopen
from urllib.parse import quote_plus, parse_qs, urlparse

class Googler():
    '''
    Class to search and extract urls from google
    '''

    def __init__(self, keyword = "", extension = "pdf" , max = 100):
        '''
        Initializer
        :param keyword: search keyword
        :param extension: file extension
        :param max: max results
        :return: None
        '''
        self.keyword = keyword
        self.max = max
        self.extension = extension
        self.downloaded = 0
        self.urls = []
        self.index = 0

    def getUrls(self):
        '''
        Search at Google and returns a list of URLs
        :return: URL list
        '''
        self.urls = []
        self.downloaded = 0
        self.index = 0
        while(self.index < self.max):
            self.doSearch()
        return self.urls

    def setMax(self, max):
        '''
        Set the maximum results
        :param max: int max
        :return:None
        '''
        self.max = max

    def setKeyword(self, keyword):
        '''
        Set the search keyword
        :param keyword: search keyword
        :return: None
        '''
        self.keyword = keyword

    def setExtension(self, extension):
        '''
        Set the file extension
        :param extension: extension
        :return: None
        '''
        self.extension = extension

    def doSearch(self):
        '''
        Open a google page and extract the urls
        :return: URL list
        '''
        html_call = Request("https://www.google.com/search?q=" + quote_plus(self.keyword) + "+filetype%3A" + self.extension + "&ie=utf-8&oe=utf-8&aq=t&rls=org.mozilla:en-US:official&client=firefox-a&channel=sb&gfe_rd=cr&ei=If4nVMz0G4aX8Qfby4DYCQ&num=100&start=" + str(self.index))
        html_call.add_header("Refer", 'http://www.google.com')
        html_call.add_header('Accept-Charset', 'utf-8')
        html_call.add_header('Cache-Control', 'no-cache')
        html_call.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/21.0')

        html_output = urlopen(html_call)
        soap = BeautifulSoup(html_output.read())
        for a in soap.select('.r a'):
            self.urls.append(a['href'])
            self.index += 1
            if self.index > self.max:
                break