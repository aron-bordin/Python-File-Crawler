import pymysql

class db():
    '''
        Class to manage all connections with the database.
        Get and add files/keywords
    '''
    def __init__(self, host=None, user=None, password=None, database=None):
        '''
        Initialize the database object with this settings
        :param host: MySQL/MariaDB hostname
        :param user: MySQL/MariaDB username
        :param password: MySQL/MariaDB password
        :param database: MySQL/MariaDB database
        :return:None
        '''

        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.con = None
        self.cursor = None;


    def connect(self):
        '''
        Try to connect to the database
        :return: None
        '''
        if(self.host is None):
            raise Exception("No MySQL/MariaDB hostname found!")
        if(self.user is None):
            raise Exception("No MySQL/MariaDB username found!")
        if(self.password is None):
            raise Exception("No MySQL/MariaDB password found!")
        if(self.database is None):
            raise Exception("No MySQL/MariaDB database name found!")
        try:
            self.con = pymysql.connect(host=self.host, user=self.user, passwd=self.password, db=self.database, charset='utf8')
            self.cursor = self.con.cursor()
        except Exception as e:
            raise e


    def select(self, sql):
        '''
        Run select query
        :param sql: select query
        :return: list of results
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def executeQuery(self, sql):
        '''
        Execute a query with no result
        :param sql: query
        :return:None
        '''
        self.cursor.execute(sql)
        self.con.commit()

    def getKeywords(self):
        '''
        Get the list of keywords
        :return: keywords
        '''
        keywords = self.select("select * from keywords")
        return  keywords

    def getFileByURL(self, url):
        '''
        Select file by url
        :param url: file download page
        :return: file row
        '''
        file = self.select("select * from files where fil_url='" + url + "'")
        return file

    def addFile(self, url, keyword):
        '''
        Add a file to files table
        :param url: file url
        :param keyword: search keyword
        :return:None
        '''
        sql = "insert into files(fil_key_id, fil_name, fil_url) values (%d, '%s', '%s')"
        file_name = url.split('/')[-1]
        self.executeQuery(sql %(keyword[0], file_name, url))

    def getFiles(self):
        '''
        Get a list of all files registered and not downloaded
        :return: List of file rows
        '''
        sql = 'select * from files where fil_downloaded = 0'
        return self.select(sql)

    def getKeywordByID(self, id):
        '''
        Get the keyword row by ID
        :param id: key_id
        :return: Keyword row
        '''
        sql = 'select * from keywords where key_id = ' + str(id)
        return self.select(sql)

    def fileDownloaded(self, fil_id):
        '''
        Set a file as downloaded
        :param fil_id: file id
        :return:None
        '''
        sql = 'update files set fil_downloaded = 1 where fil_id = ' + str(fil_id)
        self.executeQuery(sql)