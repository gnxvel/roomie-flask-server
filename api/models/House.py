from ..database.db import db

class House(db.Document):
    address1 = db.StringField(required=True,nullable=False, max_length=255)
    address2 =db.StringField(max_length=255)
    city = db.StringField(required=True)
    state= db.StringField(required=True)
    zip = db.StringField(required=True)
    sqft = db.DecimalField(required=True)
    room_num = db.IntField(required=True,max_value=4)
    #optional
    capacity = db.IntField(min_value=1, max_value=4)
    rent = db.IntField(min_value=1)
    kitchen= db.BooleanField(default=True)
    laundry= db.BooleanField(default=True)
    wifi= db.BooleanField(default=True)
    private_bath = db.BooleanField(default=False)
    # images = db.ListField(db.ImageField())
    description = db.StringField(max_length=5000)
