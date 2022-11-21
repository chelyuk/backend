from flask import Blueprint, jsonify, request, Response
from sqlalchemy import insert, select
from werkzeug.security import generate_password_hash

from backend import db
from backend.dto.user import UserCreationSchema
from backend.models.user import User, UserSchema
from backend.routes import basic_auth, token_auth

users_bp = Blueprint("users", __name__, url_prefix="/users")
user_schema = UserSchema()
user_creation_schema = UserCreationSchema()


@users_bp.route("", methods=["GET"])
@basic_auth.login_required()
def get_all_users():
    # style 1.X
    # all_users = User.query.all()

    # style 2.0
    users = db.session.scalars(select(User)).all()
    return jsonify(user_schema.dump(users, many=True))


@users_bp.route("", methods=["POST"])
@token_auth.login_required
def create_user():
    d = request.json
    new_user = user_creation_schema.load(d)

    # style 1.X
    # u = User()
    # u.username = d["username"]
    # u.email = d["email"]
    # u.password = generate_password_hash(d["password"])
    # db.session.add(u)

    # style 2.0
    db.session.execute(insert(User).values(username=new_user.username, email=new_user.email,
                                           password=generate_password_hash(new_user.password)))
    db.session.commit()

    return Response(status=204)


@users_bp.route("/<user_id>")
@basic_auth.login_required
def get_user(user_id):
    # style 1.X
    # u = User.query.filter(User.id == user_id).one()

    # style 2.0
    user = db.session.scalars(select(User).where(User.id == user_id)).one()
    return jsonify(user_schema.dump(user))
