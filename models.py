from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """db model for the pet class"""
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(25), nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, default='https://t3.ftcdn.net/jpg/05/38/52/48/360_F_538524834_KTWCegIa69mIWDLVx6Sc6tdkW6beiMBR.jpg')
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)
