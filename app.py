import os
import bcrypt

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_mongoengine import MongoEngine

from config import mongoEngineConfig
from api.routes.userRoutes import userRoutes
from api.routes.houseRoutes import houseRoutes
from api.database.db import init_database

app = Flask(__name__)

app.config.from_pyfile('config.py')
app.config['MONGODB_SETTINGS'] = mongoEngineConfig
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

CORS(app)
bcrypt = Bcrypt(app)
init_database(app)

app.register_blueprint(userRoutes, url_prefix='/api/v1')
app.register_blueprint(houseRoutes, url_prefix='/api/v1')
if __name__ == "__main__":
    app.run()
