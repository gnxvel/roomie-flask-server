import flask 
from flask_pymongo import PyMongo
from bson.json_util import dumps
import json

app = flask.Flask(__name__)
mongodb_client = PyMongo(app, uri="mongodb://localhost:27017/roomie")
db = mongodb_client.db

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

@app.route('/', methods=['GET'])
def show_all_houses():
    cursor = db.houses.find()
    list_cursor = list(cursor)
    json_data = dumps(list_cursor)
    response = app.response_class(
        response=json_data,
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == "__main__":
    app.run(debug=True)
