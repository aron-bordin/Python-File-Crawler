from db import db
import settings as s
from googler import  Googler
from urllib.request import urlretrieve
import os

class Crawler():
    '''
        Class to manage the File Crawler.
        Check proxies, keywords, search and download the files.
    '''

    def __init__(self, extension = "pdf", limit = 100, download = True):
        '''
        Initialize the Crawler with some settings.
        :param extension: extension used by google to filter files
        :param limit: the max of files to be found
        :param download:  If True, search and download files. Otherwise, just save the file url at files table
        :return: None
        '''
        self.extension = extension
        self.limit = limit
        self.download = download
        self.d = db(s.host, s.username, s.password, s.database)
        self.d.connect()
        self.g = Googler();


    def run(self):
        '''
        Start the application. Check the keywords table, and do the searchs
        :return:None
        '''
        print("->Starting the application...")
        keywords = self.d.getKeywords()
        for k in keywords:
            # not downloaded yet
            print("\tSearching for %s..." %(k[2]))
            if(k[3] == 0):
                self.g.setKeyword(k[2])
                self.g.setExtension(self.extension)
                self.g.setMax(k[1])
                urls = self.g.getUrls()
                for u in urls:
                    self.fileExists(u, k)
        print('->Search complete!')
        print('->Downloading files...(Downloaded/Total - File Name)')
        files = self.d.getFiles()
        total = len(files)
        i = 0
        for f in files:
            i += 1
            print('\tDownloading -> %d/%d - %s' %(i, total, f[2]))
            k = self.d.getKeywordByID(f[1])
            self.fileDownload(f, k[0])

        print('Done!')


    def fileExists(self, file_url, keyword):
        '''
        Check if a file is already registered on the files table. If it's not, register it.
        :param file_url: URL to download this file
        :return: boolean
        '''
        file_url = file_url.replace("'", "")
        file_url = file_url.replace('"', "")
        file = self.d.getFileByURL(file_url)
        if(len(file) == 0):
            self.d.addFile(file_url, keyword)

    def fileDownload(self, file, keyword):
        '''
        Download the file given without proxy
        :param file: URL to download this file
        :return: True if download was successful, False if had some problem
        '''
        self.getFolder(keyword[2])
        try:
        	urlretrieve(file[3], 'Downloads/%s/%s' %(keyword[2], file[2]))
        	self.d.fileDownloaded(file[0])
        except Exception as e:
        	print("Failed to download")        	
        


    def getFolder(self, folder):
        '''
        Create a folder if it not exists.
        :param folder: Folder name to be created
        :return: None
        '''
        if(os.path.isdir('Downloads') is False):
            os.mkdir("Downloads")
        if(os.path.isdir('Downloads/' + folder) is False):
            os.mkdir('Downloads/' + folder)