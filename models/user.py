from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, Mapped

from db import db


class User(db.Model):
    """
    User model
    """

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(80), unique=False, nullable=False)
    email: Mapped[str] = mapped_column(String)

    def __repr__(self):
        return f"{self.username} - {self.email}"
