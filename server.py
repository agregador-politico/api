from sanic import Sanic
from sanic.log import logger
from sanic.response import json
import matcher


app = Sanic("agrega-api")


def handle_match(data=None):
    converted_data = matcher.convert_input(data)
    database = matcher.load_database()
    matcher.do_match(converted_data, database)
    return data


@app.post("/match")
async def match(request):
    user_match = handle_match(request.json)
    logger.info(request.json)
    return json(user_match)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
