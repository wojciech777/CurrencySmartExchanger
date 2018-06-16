import unittest
from unittest import TestSuite

modules = [
    "tests"
]


def load_tests(loader, tests, pattern):
    suite = TestSuite()
    for module in modules:
        for all_test_suite in unittest.defaultTestLoader.discover(module, 'test*.py'):
            for test_suite in all_test_suite:
                suite.addTests(test_suite)

    return suite


if __name__ == '__main__':
    unittest.main()
