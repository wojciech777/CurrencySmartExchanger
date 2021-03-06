import hashlib, re
from datetime import datetime


def hash_password(password):
    return hashlib.sha512(password.encode()).hexdigest()


def validate_email(email):
    match = re.match(r'^\S+@\S+$', email)
    return match is not None


class User:
    # used when user is created(skip optional arguments)
    # or when user data is read from database(provide all arguments)
    def __init__(self, name, password, email, join_date=datetime.now(), last_login=None):
        if not validate_email(email):
            raise ValueError("invalid email")
        self.__name = name
        self.__password = hash_password(password)
        self.__email = email
        self.__join_date = join_date
        self.__last_login = last_login

    def get_name(self):
        return self.__name

    def get_password(self):
        return self.__password

    def get_email(self):
        return self.__email

    def get_join_date(self):
        return self.__join_date

    def get_last_login(self):
        return self.__last_login

    # should be called everytime user logges in
    def mark_login(self):
        self.__last_login = datetime.now()

    def __str__(self):
        return "user " + self.__name + ", email: " + self.__email + ", last login: " + str(
            self.__last_login) + ", joined: " + str(self.__join_date)
