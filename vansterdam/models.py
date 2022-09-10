from vansterdam.extensions import db
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False, nullable=False)
    update_on_new_post = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self) -> str:
        return f"User {self.id}: {self.username} <{self.email}>"

    def _set_password(self, password: str) -> None:
        """
        Set password in the db for the user associated with the User object. Will be set to hashed string, not the string itself.
        :param password: Password to be hashed.
        :return: None
        """
        self.password = generate_password_hash(password)

    def _check_password(self, candidate: str) -> bool:
        """
        Checks if password is correct.
        :param candidate: Potential password to be checked against saved password.
        :return: True if password matches, else False.
        """

        if self.password is None:
            return False

        return check_password_hash(self.password, candidate)
