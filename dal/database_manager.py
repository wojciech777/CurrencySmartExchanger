import logging
import sqlite3

from models.user import *


class DatabaseManager:
    def __init__(self, name):
        self.__name = name
        self.create()

    def create(self):
        conn = sqlite3.connect(self.__name)
        logging.info("Opened database successfully")
        conn.execute('''CREATE TABLE IF NOT EXISTS USER
         (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME CHAR(50) NOT NULL,
         PASSWORD TEXT, EMAIL TEXT, JOIN_DATE TEXT, LAST_LOGIN TEXT);''')
        logging.info("Table created successfully")
        conn.close()

    def reset(self):
        conn = sqlite3.connect(self.__name)
        conn.execute('''DELETE FROM USER''')
        conn.commit()
        conn.close()

    def get_user_by(self, criteria, value):
        return self.get_users(criteria, value)[0]

    def get_all_users(self):
        return self.__get_usersFor("SELECT * from USER")

    def get_users(self, field, field_value):
        return self.__get_usersFor("SELECT * from USER WHERE " + str(field) + "='" + str(field_value) + "'")

    def __get_usersFor(self, requestString):
        conn = sqlite3.connect(self.__name)
        cursor = conn.execute(requestString)
        users = []
        for row in cursor:
            user = User(row[1], row[2], row[3], row[4], row[5])
            users.append(user)
        conn.close()
        return users

    def delete_users(self, field, field_value):
        conn = sqlite3.connect(self.__name)
        conn.execute("DELETE from USER WHERE " + str(field) + "='" + str(field_value) + "'")
        conn.commit()
        conn.close()

    def add_user(self, user):
        if not isinstance(user, User):
            raise ValueError("add_user: argument has to be instance of class User")
        conn = sqlite3.connect(self.__name)
        name = user.get_name()
        passwd = user.get_password()
        email = user.get_email()
        join_date = str(user.get_join_date().timestamp())
        last_login = user.get_last_login()
        if last_login is not None:
            last_login = str(last_login.timestamp())
        else:
            last_login = "NULL"
        conn.execute("INSERT INTO USER VALUES (NULL, ?, ?, ?, ?, ?)", (name, passwd, email, join_date, last_login))
        conn.commit()
        conn.close()
