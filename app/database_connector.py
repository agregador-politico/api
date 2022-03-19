import pymongo
import datetime

import matcher


class Database:
    def __init__(
        self,
        host="localhost",
        port=27017,
        mongo_url="mongodb://mongodb:27017",
        database_name="agregador-database",
        username="root",
        password="agregador",
    ):
        self.client = pymongo.MongoClient(
            mongo_url, username=username, password=password
        )
        self.db = self.client[database_name]

    def insert_form(self, data=None):
        forms = self.db.forms
        data["time"] = datetime.datetime.utcnow()
        form_id = forms.insert_one(data).inserted_id
        return form_id

    def insert_question(self, data=None):
        questions = self.db.questions
        data["time"] = datetime.datetime.utcnow()
        question_id = questions.insert_one(data).inserted_id
        return question_id

    def get_collection_data(self, collection_name=None):
        collection = self.db[collection_name]
        collection_data = list(collection.find({}))
        return collection_data

    def calculate_collection_data(self, collection_data=None):
        total_number = len(collection_data)
        collection_dict = dict()
        for document in collection_data:
            key = self._get_date(document["time"])
            if key in collection_dict.keys():
                collection_dict[key] += 1
            else:
                collection_dict[key] = 1
        return total_number, collection_dict

    def _get_date(self, date=None):
        return f"{date.month}-{date.day}"


if __name__ == "__main__":
    db = Database(mongo_url="agregadorpolitico.com:27017")
    collection_data = db.get_collection_data("ACCESS")
    data = db.calculate_collection_data(collection_data)
    print(data)
    collection_data = db.get_collection_data("questions")
    data = db.calculate_collection_data(collection_data)
    print(data)
    collection_data = db.get_collection_data("forms")
    data = db.calculate_collection_data(collection_data)
    print(data)
