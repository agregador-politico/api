from sanic import Sanic
from sanic.log import logger
from sanic.response import json
from sanic_cors import CORS, cross_origin

import matcher
import database_connector


app = Sanic("agrega-api")
CORS(app)


def handle_match(data=None):
    converted_data = matcher.convert_input(data)
    database = matcher.load_database()
    data = matcher.do_match(converted_data, database)
    return data


@app.get("/")
@cross_origin(app)
async def match(request):
    return json({"status": "ok"})


@app.post("/match")
@cross_origin(app)
async def match(request):
    user_match = handle_match(request.json)
    db = database_connector.Database()
    form_id = db.insert_form(request.json)
    logger.info(f"Form {form_id} inserted in database")
    return json(user_match)


@app.post("/question")
@cross_origin(app)
async def question(request):
    db = database_connector.Database()
    question_id = db.insert_question(request.json)
    logger.info(f"Question {question_id} inserted in database")
    return json({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
