from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


# Load extensions
login_manager = LoginManager()
migrate = Migrate()
db = SQLAlchemy()
