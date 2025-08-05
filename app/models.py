import reflex as rx

from datetime import datetime


class User(rx.Model, table=True):
    __tablename__ = "users"

    name: str
    password: str
    created_at: datetime = rx.Field(default_factory=datetime.now())

    def __repr__(self):
        return f"User: {self.name}, {self.created_at}"
