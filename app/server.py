from sanic import Sanic
from sanic.log import logger
from sanic.response import json
from sanic_cors import CORS, cross_origin

import matcher


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
    return json({"status":"ok"})

@app.post("/match")
@cross_origin(app)
async def match(request):
    print(request.json)
    user_match = handle_match(request.json)
    print(user_match)
    return json(user_match)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
