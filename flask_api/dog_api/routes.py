from . import dog_api_bp
from flask_api import db
from .dog import Dog
from flask import jsonify, request
import logging

@dog_api_bp.route('/api/dog', methods=['GET'])
def show_dogs():
    dogs = []
    print(type(Dog))
    for row in Dog.query.all():
        dogs.append(row.to_json())

    response = jsonify({'results': dogs})
    return response


@dog_api_bp.route('/api/dog', methods=['POST'])
def add_dog():
    name = request.form['name']
    color = request.form['color']
    size = request.form['size']
    age = request.form['age']
    gender = request.form['gender']
    breed = request.form['breed']

    dog = Dog()
    dog.name = name
    dog.color = color
    dog.size = size
    dog.age = age
    dog.gender = gender
    dog.breed = breed

    db.session.add(dog)
    db.session.commit()
    
    response = jsonify({'message': 'Dog added', 'dog': dog.to_json()})
    logging.info('Dog added')
    return response

@dog_api_bp.route('/api/dog/<int:id>', methods=['PUT'])
def update_dog(id=None):
    dog = Dog.query.filter_by(id=id).first()
    dog.name = request.form['name']
    dog.color = request.form['color']
    dog.size = request.form['size']
    dog.age = request.form['age']
    dog.gender = request.form['gender']
    dog.breed = request.form['breed']

    db.session.commit()

    response = jsonify({'message': 'Dog updated', 'dog': dog.to_json()})
    return response


@dog_api_bp.route('/api/dog/<id>', methods=['DELETE'])
def delete_dog(id=None):
     dog = Dog.query.filter_by(id=id).first()
     if not dog:
         return jsonify({'message': f'Doesn\'t exist a dog with id {id}' })
     db.session.delete(dog)
     db.session.commit()
     response = jsonify({'message': 'Dog deleted'})
     return response


