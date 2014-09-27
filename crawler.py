

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


        def run(self):
            '''
            Start the application. Check the keywords table, and do the searchs
            :return:
            '''
            pass


        def fileExists(self, file_url):
            '''
            Check if a file is already registered on the files table
            :param file_url: URL to download this file
            :return: boolean
            '''
            pass

        def fileDownload(self, file_url):
            '''
             Download the file given without proxy
            :param file_url: URL to download this file
            :return: True if download was successful, False if had some problem
            '''

            pass

        def getFolder(self, folder):
            '''
            Create a folder if it not exists.
            :param folder: Folder name to be created
            :return: True if folder was created or if it exists, False it ocorred some error
            '''
            pass
