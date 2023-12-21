from flask import Flask

from api import user
from db import db

app = Flask(__name__)
app.register_blueprint(user.bp)


@app.route("/")
def hello_world():
    """
    Placeholder route
    :return:
    """
    return "<p>Hello, World!</p>"


def prepare_environment():
    """
    Prepare environment for running the app
    :return:
    """
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
    db.init_app(app)

    with app.app_context():
        db.create_all()


if __name__ == "__main__":
    prepare_environment()
    app.run(port=8000, debug=True)
