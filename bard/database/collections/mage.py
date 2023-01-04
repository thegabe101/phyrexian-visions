from api.database.mongo.mongo import Mongo


class Mage(Mongo):
    def __init__(self):
        super().__init__()
        self.collection = 'mage'

    def fetch_listing(self):
        return self.find(query={}, collection=self.collection)

    def fetch_by_id(self, _id):
        return self.find_by_id
