from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, ForeignKey

engine = create_engine('sqlite:///mydatabase.db', echo=True)

meta = MetaData()

people = Table(
        "people",
        meta,
        Column("id", Integer, primary_key=True),
        Column("name", String, nullable=False),
        Column('age', Integer)
)

# Adding a new table with a relationship to people
things = Table(
        "things",
        meta,
        Column('id', Integer, primary_key=True),
        Column('description', String, nullable=False),
        Column('value', Float),
        Column('owner', Integer, ForeignKey('people.id'))
)

meta.create_all(engine)
conn = engine.connect()

# How to add an insert statement

# One way to do it
#insert_statement = people.insert().values(name="Mike", age=30)

# Or
#from sqlalchemy import insert

#insert_statement = insert(people).values(name="Kanyarwanda", age=40)

#result = conn.execute(insert_statement)

#conn.commit()


# SELECTING DATA
#select_statement = people.select()
#result = conn.execute(select_statement)

#for row in result.fetchall():
#    print("----", row)


## Updating Data
#update_statement = people.update().where(people.c.name == 'Mike').values(age=50)
#result = conn.execute(update_statement)

#conn.commit()


## Delete statement
#delete_statement = people.delete().where(people.c.name == 'Mike')
#result = conn.execute(delete_statement)

#conn.commit()

# Relationships
#people_insert = people.insert().values([
#    {"name": "Mike", "age": 50},
#    {"name": "Aline", "age": 32}
#    ])

#thing_insert = things.insert().values([
#    {"description":"Laptop", "value":100.10, "owner":2},
#    {"description":"Book", "value":10.10, "owner":3},
#])

#conn.execute(people_insert)
#conn.commit()

#conn.execute(thing_insert)
#conn.commit()

## Using Joins

#join_statement = people.join(things, people.c.id == things.c.owner) # Inner join, provides entries with relationships only.
#join_statement= people.outerjoin(things, people.c.id == things.c.owner)  # Outerjoin, provides all entries, even those without a relationship.
#select_statement = people.select().with_only_columns(people.c.name, things.c.description).select_from(join_statement)

#result = conn.execute(select_statement)

## Using Group By
from sqlalchemy import func

group_by_statement = things.select().with_only_columns(things.c.owner, func.sum(things.c.value)).group_by(things.c.owner).having(func.sum(things.c.value) > 50)
result = conn.execute(group_by_statement)

for row in result.fetchall():
    print("----", row)













