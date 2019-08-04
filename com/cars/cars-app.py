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

def get_cars():
    cars = session.query(Car).all()
    return jsonify(cars=[c.serialize for c in cars])

if __name__ == '__main__':
   app.debug = True
   app.run(host='0.0.0.0', port='6446')
