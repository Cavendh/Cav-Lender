from flask import Flask, render_template, url_for
from config import Config
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)


from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

class Event(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	start_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	end_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	


# Attempting to set up Migrations

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
	manager.run()

