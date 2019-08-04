__author__ = "Keith O'Shea"
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from com.cars.database_setup import Car, Base

engine = create_engine('sqlite:///cars-collection.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

carOne = Car(chassis_no= "12345A", make="Nissan", model="Micra", year="1999", last_updated="2017-02-01 00:00:00", price=500.00, id=1)
session.add(carOne)
session.commit()

