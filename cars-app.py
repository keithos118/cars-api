__author__ = "Keith O'Shea"
from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Car
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Python Flask API"
    }
)

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


@app.route("/cars/average/<name>/<model>/<year>", methods = ['GET'])
def make_model_year_average(name, model, year):
    if request.method == 'GET':
        return average_price_make_model_year(name, model, year)


def get_cars():
    cars = session.query(Car).all()
    return jsonify(cars=[c.serialize for c in cars])


def get_car_by_id(id):
    cars = session.query(Car).filter_by(id=id).all()
    return jsonify(cars=[c.serialize for c in cars])


def get_average_price(entry):
    cars = session.query(Car).filter_by(make=entry).all() \
        or session.query(Car).filter_by(model=entry).all() \
        or session.query(Car).filter_by(year=entry).all()
    cars_list = (c.serialize for c in cars)

    price_list = []
    for value in cars_list:
        price_list.append(value['price'])
    average_price = (average(price_list))
    return jsonify(cars=average_price)


def average_price_make_model_year(make, model,year):
    cars = session.query(Car).filter_by(make=make, model=model, year=year).all()
    li = (c.serialize for c in cars)
    l = []
    for p in li:
        l.append(p['price'])
    average_price = (average(l))
    return jsonify(cars=average_price)


def average(data):
    result = sum(data) / len(data)
    return round(result,2)


if __name__ == '__main__':
    app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
    app.run()
   #app.run(debug=True, host='0.0.0.0', port='6446')
