#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import sqlite3
from classes.database import Database
# import Database

database = Database()


data = {"name" : "olivier", "age" : 30}
database.insert( data )
database.read_data()

database.connection.close()

