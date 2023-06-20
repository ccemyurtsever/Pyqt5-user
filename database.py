import sqlite3 as sql
import time
import os

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
    time.sleep(1)

create()

def insert(name,lastname,username,password):
    dbConnect()
    add_command = """INSERT INTO USERS(name,lastname,username,password) VALUES {} """
    add = (name,lastname,username,password)
    cursor.execute(add_command.format(add))
    dbOut()
    time.sleep(1)

def update_password(username,newPassword):
    dbConnect()
    upd_command = """UPDATE USERS SET password = '{}' WHERE username = '{}'"""
    cursor.execute(upd_command.format(username,newPassword))
    dbOut()
    time.sleep(1)

def search_username(username):
    dbConnect()
    add_search = """SELECT * FROM USERS WHERE username = '{}' """
    add = username
    cursor.execute(add_search.format(add))
    dbOut()

def delete_account(username):
    dbConnect()
    dlt_command = """DELETE FROM USERS WHERE username = '{}' """
    cursor.execute(dlt_command.format(username))
    dbOut()
    time.sleep(1)

def urgently_drop():
    database_file = "database.db"
    os.path.exists(database_file)
    os.remove(database_file)
    dbConnect()
    dbOut()
    time.sleep(4)

