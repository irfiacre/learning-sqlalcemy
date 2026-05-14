from sqlalchemy import create_engine, Integer, String, Float, Column, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine('sqlite:///mydatabase.db', echo=True)

Base = declarative_base()

class Person(Base):
    __tablename__='people'
    id=Column(Integer, primary_key=True)
    name=Column(Integer, nullable=False)
    age=Column(Integer)

    things = relationship('Thing', back_populates='person')  # Why don't we say that it backpopulates the "people" table?


class Thing(Base):
    __tablename__='things'
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    value = Column(Float)
    owner = Column(Integer, ForeignKey('people.id'))

    person = relationship('Person', back_populates='things')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

#new_person = Person(name='Blaise', age=80)
#session.add(new_person)
#session.flush() # This temporary writes the changes to the database but a commit is still needed to make the changes permanent.
# This is usefull because at some point we need for the initial object to be written in the database so that it can be for example referenced in another object.

#new_thing = Thing(description='Camera', value=500, owner=new_person.id) # In this case we need the new_person to be added to the DB before we can reference the ID. 
#session.add(new_thing)

#session.commit()


## Querying the tables

#result = session.query(Person).all()
#result = session.query(Person).filter(Person.age > 50).all() # Filtering
# --> This can be used for deletion
#result = session.query(Thing).fiter(Thing.value < 50).delete()
# session.commit()

# --> Can be used for Update
#result = session.query(Person).filter(Person.name == 'Blaise').update({'name': 'Charles'})
#session.commit()
#print([p.name for  p in result])

# Joins
#result = session.query(Person.name, Thing.description).join(Thing).all()


# GroupBY
from sqlalchemy import func

result = session.query(Thing.owner, func.sum(Thing.value)).group_by(Thing.owner).all()

print(result)

session.close()

