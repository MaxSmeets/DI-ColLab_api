from flask_sqlalchemy import SQLAlchemy
from database.models.base import Base

db = SQLAlchemy(model_class=Base)
