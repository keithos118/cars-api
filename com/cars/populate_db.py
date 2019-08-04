__author__ = "Keith O'Shea"
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from com.cars.database_setup import Car, Base

engine = create_engine('sqlite:///cars-collection.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# carOne = Car(chassis_no= "12345A", make="Nissan", model="Micra", year="1999", last_updated="2017-02-01 00:00:00", price=500.00, id=1)
# session.add(carOne)
# session.commit()

import csv
with open('cars.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    buffer = []
    for row in csv_reader:
        if row[6] == "":
            row[6]+=0
        buffer.append({
            'make': row[0],
            'model': row[1],
            'year': row[2],
            'chassis_no': row[3],
            'id': row[4],
            'last_updated': row[5],
            'price': row[6]
        })
        if len(buffer) % 10000 == 0:
            session.bulk_insert_mappings(Car,buffer)
            buffer = []

    session.bulk_insert_mappings(Car,buffer)
    session.commit()