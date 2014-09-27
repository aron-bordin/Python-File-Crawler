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