__author__ = "Keith O'Shea"
from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from com.cars.database_setup import Base, Car

app = Flask(__name__)
#Connect to Database and create database session
engine = create_engine('sqlite:///cars-collection.db',connect_args={'check_same_thread': False})
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route("/")
@app.route("/cars/", methods = ['GET'])
def all_cars():
   if request.method == 'GET':
       return get_cars()

@app.route("/cars/<id>", methods = ['GET'])
def cars_by_id(id):
   if request.method == 'GET':
       return get_car_by_id(id)

@app.route("/cars/average/<name>", methods = ['GET', 'POST'])
def cars_average(name):
   if request.method == 'GET':
       return get_average_price(name)

def get_cars():
    cars = session.query(Car).all()
    return jsonify(cars=[c.serialize for c in cars])

def get_car_by_id():
    cars = session.query(Car).filter_by(id=id).all()
    return jsonify(cars=[c.serialize for c in cars])


def get_average_price(entry):
    cars = session.query(Car).filter_by(make=entry).all()
    cars_list = (c.serialize for c in cars)

    price_list = []
    for value in cars_list:
        price_list.append(value['price'])
    average_price = (average(price_list))
    return jsonify(cars=average_price)


def average(data):
    result = sum(data) / len(data)
    return round(result,2)


if __name__ == '__main__':
   app.debug = True
   app.run(host='0.0.0.0', port='6446')
