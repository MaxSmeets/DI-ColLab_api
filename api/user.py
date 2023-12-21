from flask import Blueprint

from db import db
from models.user import User

bp = Blueprint("user", __name__, url_prefix="/users")


@bp.route("/", methods=["GET"])
def get_users():
    """
    Get all users
    :return: List of users
    """
    users: [User] = db.session.execute(db.select(User)).all()
    return str(users)


@bp.route("/", methods=["POST"])
def create_user():
    """
    Create a user with given username and email from request body
    """
    user = User(username="test", email="")
    db.session.add(user)
    db.session.commit()
    return "User created"


@bp.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    """
    Get a user by id
    :param user_id:
    :return: user
    """
    user: User = db.session.execute(db.select(User).where(User.id == user_id)).first()
    return str(user)
