__author__ = "Keith O'Shea"
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
Base = declarative_base()

class Car(Base):
   __tablename__ = 'cars'

   chassis_no = Column(String(250),primary_key=True, nullable=False)
   make = Column(String(250), nullable=False)
   model = Column(String(250), nullable=False)
   year = Column(String(4), nullable=True)
   last_updated = Column(String(250))
   price = Column(Float(), nullable=True)
   id = Column(Integer(), nullable=False)

   @property
   def serialize(self):
      return {
         #'chassis_no': self.chassis_no, // Hidden from response
         'make': self.make,
         'model': self.model,
         'year': self.year,
         'last_updated': self.last_updated,
         'price' : self.price,
         'id' : self.id
      }
engine = create_engine('sqlite:///cars-collection.db')
Base.metadata.create_all(engine)