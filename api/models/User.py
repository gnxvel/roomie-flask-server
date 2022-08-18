# from flask_login import UserMixin
# from app import dbuserRoutesuseruserRoutes
from ..database.db import db
from flask_bcrypt import generate_password_hash, check_password_hash
# # @loggin_manager.user_loader
# # def load_user(user_id):
#     # return


class Users(db.Document):
    username = db.StringField(required=True, unique=True,
                              nullable=False, min_length=2, max_length=30)

    email = db.EmailField(
        required=True, unique=True,  nullable=False, min_length=2, max_length=30)

    password = db.StringField(
        required=True, nullable=False, max_length=60)
    meta = {'strict': False}

    def hash_password(self):
        self.password = generate_password_hash(self.password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
