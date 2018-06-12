import unittest

from dal.DatabaseLayer import DatabaseLayer
from dal.database_manager import *


class MockDatabaseManager:
    lastMethod = ""

    def create(self):
        self.lastMethod = "create"

    def reset(self):
        self.lastMethod = "reset"

    def get_all_users(self):
        self.lastMethod = "get_all_users"

    def get_users(self, field, field_value):
        self.lastMethod = "get_users " + field + " " + field_value

    def delete_users(self, field, field_value):
        self.lastMethod = "delete_users " + field + " " + field_value

    def add_user(self, user):
        self.lastMethod = "add_user " + user.get_name()


class TestDBLayer(unittest.TestCase):
    def setUp(self):
        self.database_layer = DatabaseLayer()
        self.mockDB = MockDatabaseManager()
        self.database_layer.database_manager = self.mockDB

    def test_crud_layer(self):
        self.database_layer.get_all_users()
        self.assertEqual(self.mockDB.lastMethod, "get_all_users")

        self.database_layer.get_users_by_id("123")
        self.assertEqual(self.mockDB.lastMethod, "get_users ID 123")

        self.database_layer.get_users_by_name("testName")
        self.assertEqual(self.mockDB.lastMethod, "get_users NAME testName")

        self.database_layer.get_users_by_email("testNameMail")
        self.assertEqual(self.mockDB.lastMethod, "get_users EMAIL testNameMail")

        self.database_layer.delete_users_by_id("123")
        self.assertEqual(self.mockDB.lastMethod, "delete_users ID 123")

        self.database_layer.delete_users_by_name("123")
        self.assertEqual(self.mockDB.lastMethod, "delete_users NAME 123")

        self.database_layer.delete_users_by_email("123")
        self.assertEqual(self.mockDB.lastMethod, "delete_users EMAIL 123")

        self.database_layer.add_user(User("john", "qwe123", "john88@aa.com"))
        self.assertEqual(self.mockDB.lastMethod, "add_user john")


if __name__ == '__main__':
    unittest.main()
