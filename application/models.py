from application import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return f"User {self.id}: {self.username} <{self.email}>"
