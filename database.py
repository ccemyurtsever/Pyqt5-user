import sqlite3 as sql

def dbConnect():
    global connect
    connect = sql.connect("database.db")
    global cursor
    cursor = connect.cursor()

def dbOut():
    connect.commit()
    connect.close()

def create():
    dbConnect()
    cursor.execute("""CREATE TABLE IF NOT EXISTS USERS(
        id integer PRIMARY KEY NOT NULL,
        name varchar(75) NOT NULL,
        lastname varchar(75) NOT NULL,
        username text NOT NULL,
        password text NOT NULL
    )""")
    connect.commit()
    connect.close()
