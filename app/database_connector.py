import pymongo
import datetime
import constants


class Database:
    def __init__(
        self,
        mongo_url=constants.DATABASE_URL,
        database_name=constants.DATABASE_NAME,
        username=constants.DATABASE_USER,
        password=constants.DATABASE_PASS
    ):
        self.client = pymongo.MongoClient(mongo_url, username=username, password=password)
        self.db = self.client[database_name]

    def insert_data(self, collection=None, content=None):
        collection = self.db[collection]
        data = content.copy()
        data['time'] = datetime.datetime.utcnow()
        row_id = collection.insert_one(data).inserted_id
        return row_id
