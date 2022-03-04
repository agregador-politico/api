import pymongo
import datetime


class Database:
    def __init__(
        self,
        host="localhost",
        port=27017,
        mongo_url="mongodb://mongodb:27017",
        database_name="agregador-database",
        username='root',
        password='agregador'
    ):
        self.client = pymongo.MongoClient(mongo_url, username=username, password=password)
        self.db = self.client[database_name]

    def insert_form(self, data=None):
        forms = self.db.forms
        data['time'] = datetime.datetime.utcnow()
        form_id = forms.insert_one(data).inserted_id
        return form_id

    def insert_question(self, data=None):
        questions = self.db.questions
        data['time'] = datetime.datetime.utcnow()
        question_id = questions.insert_one(data).inserted_id
        return question_id
