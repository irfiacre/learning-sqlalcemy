from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine('sqlite:///mydatabase.db', echo=True)

meta = MetaData()

people = Table(
        "people",
        meta,
        Column("id", Integer, primary_key=True),
        Column("name", String, nullable=False),
        Column('age', Integer)
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

## SELECTING DATA
select_statement = people.select().where(people.c.age > 30)
result = conn.execute(select_statement)

for row in result.fetchall():
    print("----", row)

