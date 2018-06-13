from dal.database_manager import DatabaseManager


class DatabaseLayer:

    def __init__(self):
        self.database_manager = DatabaseManager("prod.sqlite3")

    def add_user(self, user):
        self.database_manager.add_user(user)

    def get_all_users(self):
        return self.database_manager.get_all_users()

    def get_users_by_id(self, identifier):
        return self.database_manager.get_users("ID", identifier)

    def get_users_by_name(self, name):
        return self.database_manager.get_users("NAME", name)

    def get_users_by_email(self, email):
        return self.database_manager.get_users("EMAIL", email)

    def delete_users_by_id(self, identifier):
        return self.database_manager.delete_users("ID", identifier)

    def delete_users_by_name(self, name):
        return self.database_manager.delete_users("NAME", name)

    def delete_users_by_email(self, email):
        return self.database_manager.delete_users("EMAIL", email)
