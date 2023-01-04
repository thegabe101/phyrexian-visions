import logging
import pymongo
from flask import current_app

log = logging.getLogger('werkzeug')
class MongoDBConn:

    DATABASE = None
    CLIENT = None
    CONNECTION_TIMEOUT = 5000

    @staticmethod
    def initialize():
        CONNSTRING = "mongodb://{}:{}@{}:{}".format(
            'bard',
            'bard',
            'mongo',
            27017
        )

        MongoDBConn.CLIENT = pymongo.MongoClient(CONNSTRING,
                                                 serverSelectionTimeoutMS=MongoDBConn.CONNECTION_TIMEOUT
                                                 )
        MongoDBConn.DATABASE = MongoDBConn.CLIENT['bard_db']

    @staticmethod
    def get_db():
        if MongoDBConn.DATABASE is None:
            MongoDBConn.initialize()
        return MongoDBConn.DATABASE

    @staticmethod
    def get_client():
        if MongoDBConn.CLIENT is None:
            MongoDBConn.initialize()
        return MongoDBConn.CLIENT
