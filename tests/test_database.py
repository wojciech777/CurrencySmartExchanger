import unittest

from dal.database_manager import *


class TestDB(unittest.TestCase):
    def setUp(self):
        self.database_manager = DatabaseManager("test.sqlite3")

    def test_crud(self):
        self.database_manager.create()
        self.database_manager.reset()
        self.assertEqual(len(self.database_manager.get_all_users()), 0)
        self.database_manager.add_user(User("john", "qwe123", "john88@aa.com"))
        self.database_manager.add_user(User("asd", "eee", "rrr@aa.com"))
        self.assertEqual(len(self.database_manager.get_all_users()), 2)
        self.database_manager.add_user(User("qwe", "xcv", "tyu@aa.com"))
        self.assertEqual(len(self.database_manager.get_all_users()), 3)
        self.assertEqual(len(self.database_manager.get_users("NAME", "john")), 1)
        self.database_manager.delete_users("NAME", "john")
        self.assertEqual(len(self.database_manager.get_users("NAME", "john")), 0)
        self.assertEqual(len(self.database_manager.get_all_users()), 2)
        self.database_manager.reset()
        self.assertEqual(len(self.database_manager.get_all_users()), 0)

    def test_add_user(self):
        self.database_manager.create()
        self.database_manager.reset()
        self.database_manager.add_user(User('name', 'passd', 'name@gmail.com'))
        user = self.database_manager.get_user_by('NAME', 'name')
        assert user


if __name__ == '__main__':
    unittest.main()
