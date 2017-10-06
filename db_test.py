import sqlite3

db = sqlite3.connect("db.sqlite", check_same_thread=False)
db.execute("CREATE TABLE IF NOT EXISTS t1(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
name = "Cyan Tarek"
db.execute("INSERT INTO t1 (name) VALUES (?)", (name,))
db.commit()
