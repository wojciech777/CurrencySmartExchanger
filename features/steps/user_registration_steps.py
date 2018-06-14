# -- FILE: features/steps/user_registration_steps.py

from behave import given, when, then

from dal.database_manager import DatabaseManager
from models.user import User


@given('No existing account with given details')
def step_impl(context):
    context.manager = DatabaseManager('test')


@when('user registers in the application')
def step_impl(context):
    user = User('John Smith', 'passwd123', 'john.smith@gmail.com')
    context.manager.add_user(user)


@then('new account should be created and saved in the database')
def step_impl(context):
    user = context.manager.get_user_by('NAME', 'John Smith')
    assert user
