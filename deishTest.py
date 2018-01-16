from deish import DeishDb

#debug ----------------------------------------------------
db = DeishDb()
db.new_colection('caio')
db.push('caio', 123, {'mensage': 'hello world'})
db.push('caio', 124, {'mensage': 'hello 2 world'})
y = db.get('caio', 123)
print(y)
db.update('caio', 123, {'mensage': 'hello', 'time': 22})
y = db.get('caio', 123)
print(y)
z = db.remove('caio', 123)
print(z)
k = db.get('caio')
print(k)