from sanic import Sanic
from sanic.log import logger
from sanic.response import json
import matcher


app = Sanic("agrepga-api")


def handle_match(data=None):
    converted_data = matcher.convert_input(data)
    db = matcher.load_database()
    logger.error(db)
    return data


@app.post("/match")
async def match(request):
    user_match = handle_match(request.json)
    return json(user_match)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
