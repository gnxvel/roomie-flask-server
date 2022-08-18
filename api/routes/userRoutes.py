from flask import request, jsonify, Blueprint

# !Note: MongoEngine save class Name of Model without 's'
from api.models.User import Users

# logging.basicConfig(level=logging.DEBUG)

userRoutes = Blueprint('api', __name__)


@userRoutes.route("/")
def home_page():
    return "HOMEPAGE"


@userRoutes.route('/user', methods=['GET'])
def get_user():
    users = Users.objects()
    return jsonify(users), 200


@userRoutes.route('user/<id>')
def get_user_by_id(id: str):
    find_user = Users.objects(id=id).first()
    return jsonify(find_user), 200


@userRoutes.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    # print(data)

    new_user = Users(
        # username=data.username,
        # email=data.email,
        # password=data.password
        username=data["username"],
        email=data["email"],
        password=data["password"]
    )
    new_user.save(force_insert=True)

    return jsonify(new_user), 201


