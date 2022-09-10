from config import Config, DatabaseConfig
from flask import Flask
from typing import Optional
from vansterdam.extensions import login_manager, migrate, db
from vansterdam.models import User


app = Flask(__name__)
app.config.from_object(Config)
app.config.from_object(DatabaseConfig)

# SQLAlchemy
db.init_app(app)

# Migrate
migrate.init_app(app, db)

# Login
login_manager.init_app(app)


@login_manager.user_loader
def load_user(id: int) -> Optional[User]:
    return User.query.filter_by(id=int(id)).first()


from vansterdam import routes, models
