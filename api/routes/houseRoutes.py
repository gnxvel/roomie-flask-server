from crypt import methods
from operator import methodcaller
from flask import request, jsonify, Blueprint
from mongoengine.queryset.visitor import Q

from api.models.House import House


houseRoutes = Blueprint('api_house', __name__)

#get list of houses
@houseRoutes.route("/houses", methods=["GET"])
def get_all_houses():
    houses = House.objects()
    return jsonify(houses), 200

#create house
@houseRoutes.route('/houses', methods=["POST"])
def create_house():
    data = request.get_json()

    new_house = House(
        address1 = data["address1"],
        address2 =data["address2"],
        city = data["city"],
        state= data["state"],
        zip = data["zip"],
        sqft = int(data["sqft"]),
        room_num = int(data["room_num"]),
        capacity = int(data["capacity"]),
        rent = int(data["rent"]),
        kitchen= data["kitchen"],
        laundry= data["laundry"],
        wifi= data["wifi"],
        private_bath = data["private_bath"],
        description = data["description"],
    )
    new_house.save(force_insert=True)

    return jsonify(new_house), 201

@houseRoutes.route('/houses/<id>', methods=["GET","DELETE", "PUT"])
def house_by_id(id: str):
    if request.method == "GET":
        house = House.objects(id=id)
        return jsonify(house), 200

    if request.method == "DELETE":
        house = House.objects(id=id)
        house.delete()
        return {},204

    if request.method =="PUT":
        data = request.get_json()
        house = House.objects(id=id)
        updated_fields = {
        "address1" : data["address1"],
        "address2" :data["address2"],
        "city" : data["city"],
        "state": data["state"],
        "zip" : data["zip"],
        "sqft" : int(data["sqft"]),
        "room_num" : int(data["room_num"]),
        "capacity" : int(data["capacity"]),
        "rent" : int(data["rent"]),
        "kitchen": data["kitchen"],
        "laundry": data["laundry"],
        "wifi": data["wifi"],
        "private_bath" : data["private_bath"],
        "description" : data["description"],
    }
        house.update( **updated_fields)

        return jsonify(house), 200



#get filtered houses: state, city, num_bed, sqft
# @houseRoutes.route("/houses/<state>/<city>/<num_bed>/<sqft>")
# def get_filtered_house(state,city,num_bed,sqft):
#     state = state if state != "null" else None
#     city = city if city != "null" else None

    # try:
    #     num_bed = int(num_bed)
    # except ValueError:
    #     num_bed = None
    # try:
    #     sqft = int(num_bed)
    # except ValueError:
    #     sqft = None

    #filter not-None conditions
    # houses = House.objects().filter(Q(state=state)& Q(city=city)& Q(room_num__lte=num_bed) &Q(sqft__gte=sqft))

    # return f'Houses for: {state}, {city}, with max {num_bed} bedrooms, min sqft of {sqft}'