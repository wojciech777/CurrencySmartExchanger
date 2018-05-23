import unittest
import re
from models.user import *
from datetime import datetime


class TestUM(unittest.TestCase):
    def setUp(self):
        pass

    def test_name(self):
        name = "name"
        user = User(name, "passwd", "em@ai.ll")
        self.assertEqual(name, user.get_name())

    def test_password(self):
        passwd = "pass"
        user = User("name", passwd, "em@ai.ll")
        self.assertNotEqual(passwd, user.get_password())

    def test_user_email(self):
        email = "em@ai.ll"
        user = User("name", "passwd", email)
        self.assertNotEqual(user, None)
        self.assertEqual(email, user.get_email())
        with self.assertRaises(ValueError):
            User("name", "passc", "zxcas")
        self.assertNotEqual(re.match(r'^\S+@\S+$', email), None)

    def test_user_join_date(self):
        user = User("name", "passwd", "email@sd.xc").get_join_date().timestamp()
        self.assertGreater(datetime.now().timestamp(), user)
        User("name", "passwd", "email@sd.xc", datetime.now(), datetime.now()).get_join_date().timestamp()
        self.assertGreater(datetime.now().timestamp(), user)

    def test_user_last_login(self):
        self.assertEqual(User("name", "passwd", "email@sd.xc").get_last_login(), None)
        self.assertNotEqual(User("name", "passwd", "email@sd.xc", datetime.now(), datetime.now()).get_last_login(),
                            None)


if __name__ == '__main__':
    unittest.main()
