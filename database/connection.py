import sqlite3
import threading

def getDb():
    try:
        sqlite3_db = threading.local()
        sqlite3_db.connection = sqlite3.connect('food.db')
        return sqlite3_db.connection
    except Exception as e:
        print(e)
