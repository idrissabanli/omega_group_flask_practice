from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


from app import app


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://idris:123456@localhost:5432/DAY_30_BASE'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)