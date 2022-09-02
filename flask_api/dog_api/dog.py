from flask_api import db
from datetime import datetime 

class Dog(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    color = db.Column(db.String(255), unique=False, nullable=False)
    size = db.Column(db.String(255), unique=False, nullable=False)
    age = db.Column(db.String(255), unique=False, nullable=False)
    gender = db.Column(db.String(255), unique=False, nullable=False)
    breed = db.Column(db.String(255), unique=False, nullable=False)
    adopted = db.Column(db.Boolean, unique=False, default=False)
    date_adopted = db.Column(db.DateTime, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, onupdate=datetime.utcnow)


    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'color': self.color,
            'size': self.size,
            'age': self.age,
            'gender': self.gender,
            'breed': self.breed,
            'adopted': self.adopted
        }
