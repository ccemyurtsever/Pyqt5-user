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
    dbOut()

def instert(name,lastname,username,password):
    dbConnect()
    add_command = """INSERT INTO USERS(name,lastname,username,password) VALUES {} """
    add = (name,lastname,username,password)
    cursor.execute(add_command.format(add))
    dbOut()

def update_password(username,newPassword):
    dbConnect()
    upd_command = """UPDATE USERS SET password = '{}' WHERE username = '{}'"""
    cursor.execute(upd_command.format(username,newPassword))
    dbOut()