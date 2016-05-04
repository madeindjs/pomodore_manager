#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3

try:
	conn = sqlite3.connect('databases.sqlite')
except:
	print("error in database creation")



cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users( id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,name TEXT,age INTERGER ) ")

data = {"name" : "olivier", "age" : 30}
cursor.execute("INSERT INTO users(name, age) VALUES(:name, :age)", data)

cursor.execute("""SELECT * FROM users""")

for row in cursor:
	print( 'id:{0} | nom:{1} | age:{2}'.format(row[0], row[1], row[2]))

conn.commit()
conn.close()