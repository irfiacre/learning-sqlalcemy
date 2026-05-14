import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite:///mydatabase.db', echo=True)

df = pd.read_sql("SELECT * FROM people", con=engine)

print(df)
# new_data = pd.DataFrame({'name': ['erik', 'moon'], 'age':[26, 40]})
# new_data.to_sql('people', con=engine, if_exists='append', index=False)

