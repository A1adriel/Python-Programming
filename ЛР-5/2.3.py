from pymongo import MongoClient

class MongoDBConnectionContextManager(object):
    def __init__(self, host='localhost', port=27017, username='admin', password='admin'):
        self.host = host
        self.port = port
        self.username = username
        self.passwd = password
        self.connection = None

    def __enter__(self):
        self.connection = MongoClient(
            self.host, 
            self.port,
            username = self.username,
            password = self.passwd,
            authMechanism="SCRAM-SHA-1")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

with MongoDBConnectionContextManager(host='localhost', port=27017, username='myUserAdmin', password='abc123') as mcm:
    lst = mcm.connection['myshinynewdb']['user']
    user = lst.find({'age': 205})
    print(next(user))