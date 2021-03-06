from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Cake(Base):
    __tablename__ = 'cake'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250))
    picture = Column(String(250))
    price_for_kg = Column(String(10))
    diameter = Column(String(10))
    weight = Column(String(10))
    price_total = Column(String(10))
    client = Column(String(250))
    sell_date = Column(String(10))
    costs = Column(String(10))
    proceeds = Column(String(10))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'description': self.description,
            'picture' = self.picture,
            'price_for_kg' = self.price_for_kg,
            'diameter' = self.diameter,
            'weight' = self.weight,
            'price_total' = self.price_total,
            'client' = self.client,
            'sell_date' = self.sell_date,
            'costs' = self.costs,
            'proceeds' = self.proceeds,
        }


class Element(Base):
    __tablename__ = 'elements'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    price_per_kg = Column(String(8))
    weight = Column(String(8))
    price_element = Column(String(8))
    cake_id = Column(Integer, ForeignKey('cake.id'))
    cake = relationship(Cake)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'price_per_kg' = self.price_per_kg,
            'weight' = self.weight,
            'price_element' = self.price_element,
            }


engine = create_engine('sqlite:///cakeswithusers.db')


Base.metadata.create_all(engine)
