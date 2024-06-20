from connection import getDb
import csv

def createUserTable():
    conn=getDb()
    cur = conn.cursor()
    try:
        cur.execute('''
            CREATE TABLE IF NOT EXISTS User (
                id INTEGER PRIMARY KEY autoincrement,
                name varchar(100) NOT NULL,
                email varchar(100) unique NOT NULL,
                password TEXT  NOT NULL
            );
            ''')
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(e)


def createFoodTable():
    conn=getDb()
    cur = conn.cursor()
    try:
        cur.execute('''
            CREATE TABLE IF NOT EXISTS Foods (
                id INTEGER PRIMARY KEY autoincrement,
                recipe TEXT NOT NULL,
                ingredients TEXT NOT NULL,
                cuisine TEXT NOT NULL,
                course TEXT NOT NULL,
                diet TEXT NOT NULL,
                instructions TEXT NOT NULL
            );
            ''')
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(e)

def showTables():
    conn=getDb()
    cur = conn.cursor()
    try:
        cur.execute("""
            SELECT name FROM sqlite_master WHERE type='table';
        """)
        tables = cur.fetchall()
        if tables:
            print("Tables in the database:")
            for table in tables:
                print(table[0])
                cur.execute(f"PRAGMA table_info({table[0]});")
                columns = cur.fetchall()
                print(F"DESC OF {table[0]}")
                for column in columns:
                    print(column,end=" ")
                print()
    except Exception as e:
        print(e)

def insertFoodData():
    conn=getDb()
    try:
        cur = conn.cursor()
        with open('IndianFoodDatasetCSV.csv', mode='r') as file:
            csv_reader = csv.reader(file)

            # Skip the header row if your CSV has one
            next(csv_reader)

            # Read the CSV file
            for row in csv_reader:
                try:
                    q='INSERT INTO Foods(recipe,ingredients,cuisine,course,diet,instructions) VALUES("%s","%s","%s","%s","%s","%s")'%(row[2],row[4],row[9],row[10],row[11],row[13])
                    cur.execute(q)
                    conn.commit()
                except Exception as e:
                    print(e)
                    conn.rollback()
    except Exception as e:
        print(e)

def dropTable(table):
    conn=getDb()
    cur=conn.cursor()
    try:
        q="drop table '%s'"%(table,)
        cur.execute(q)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()

def dataCount(table):
    conn=getDb()
    cur=conn.cursor()
    try:
        q="select count(*) from '%s'"%(table,)
        res=cur.execute(q)
        print(res.fetchall())
    except Exception as e:
        print(e)

def getData(table):
    conn=getDb()
    cur=conn.cursor()
    try:
        q="select * from '%s'"%(table,)
        res=cur.execute(q)
        print(res.fetchall())
    except Exception as e:
        print(e)

if __name__=="__main__":
    # createUserTable()
    # createFoodTable()
    # showTables()
    # insertFoodData()
    # dropTable('Foods')
    # dataCount('Foods')
    getData('User')