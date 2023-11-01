import sqlalchemy as db

engine = db.create_engine('sqlite:///census.sqlite')
connection = engine.connect()
metadata = db.MetaData()
census = db.Table('census', metadata, autoload=True, autoload_with=engine)

# Equivalent to 'SELECT * FROM census'
query = db.select([census])

proxy = connection.execute(query)
print(proxy)

result = proxy.fetchall()

print(result[:10])
