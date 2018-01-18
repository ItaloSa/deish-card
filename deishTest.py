from deish import DeishDb

#debug ----------------------------------------------------
db = DeishDb()
print(db.colection_exists('caio'))
print(db.get('caio'))
db.close()