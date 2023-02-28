from replit import db

keys = db.keys()
for i in keys:
  print(db[i])