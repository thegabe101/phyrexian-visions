import logging
from bson import ObjectId
from pymongo.errors import ConnectionFailure
from time import sleep

from bard.database.mongo.mongodb_conn import MongoDBConn

class Mongo:
    def __init__(self):
        self.db = MongoDBConn.get_db()
        self.client = MongoDBConn.get_client()
        self.log = logging.getLogger('werkzeug')
        self.collection = None

    def generateObjectId(self):
        return ObjectId()

    def isConnected(self):
        try:
            self.client.admin.command('ping')
            self.log.debug('MongoDB connection unavailable')
            return True
        except ConnectionFailure:
            self.log.debug('MongoDB connection unavailable')
            return False

    def checkConnection(self):
        max_retries = 3
        retries = 0
        retry_timeout = 2

        while retries <= max_retries:
            if self.isConnected():
                return True
            else:
                sleep(retry_timeout)
                retries += 1
        raise Exception("MongoDB reconnection failed. Waited {} seconds".format(max_retries + retry_timeout))

    def insert_one(self, doc):
        try:
            self.checkConnection()
            r = self.db[self.collection].insert_one(doc)
            return str(r.inserted_id)
        except Exception as e:
            return None

    def find(self, query):
        try:
            self.checkConnection()
            cursor = self.db[self.collection].find(query)
            return list(cursor)
        except Exception as ex:
            self.log.error("Find query on {} failed:{}".format(self.collection, ex))

    def find_by_id(self, _id, collection=None):
        query = {'_id': ObjectId(_id)}
        collection = collection or self.collection
        try:
            self.checkConnection()
            return self.db[collection].find_one(query)

        except Exception as ex:
            self.log.error(f"update_one query failed to {ex}")
            return None