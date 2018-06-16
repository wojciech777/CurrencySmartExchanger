import unittest

from models.user_forms import UserForms


class TestUserForms(unittest.TestCase):
    def setUp(self):
        pass

    def test_name(self):
        name = "name"
        user_forms = UserForms(name, "passwd", "em@ai.ll")
        self.assertNotEqual(user_forms, None)
        self.assertEqual(name, user_forms.get_name())

    def test_password(self):
        passwd = "pass"
        user_forms = UserForms("name", passwd, "em@ai.ll")
        self.assertNotEqual(user_forms, None)
        self.assertEqual(passwd, user_forms.get_password())

    def test_user_email(self):
        email = "em@ai.ll"
        user_forms = UserForms("name", "passwd", email)
        self.assertNotEqual(user_forms, None)
        self.assertEqual(email, user_forms.get_email())


if __name__ == '__main__':
    unittest.main()
