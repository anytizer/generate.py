#!/bin/python
# https://docs.python.org/3/library/unittest.html
#
# Usage:
#
# python generate.py > units.py
# python -m unittest units.py
#
# or,
#
# generate.bat
#

# Convert to test cases for these statements
cases = {
    "application": [
        "id exist",
        "id does not exist",
        "too old user cannot login"
    ],
}

# Process
# define classes
# define class methods
# create unit tests


def _testcase_body_template(case:str):
    fname = case.lower().replace(" ", "_")
    method = "something"
    body = f"""
    def test_{fname}(self):
        data = []
        result = self.application.{method}(data)
        self.assertTrue(result)
"""
    return body


for application, testcases in cases.items():
    head = f"""#!/bin/python
import unittest
from application import application


class TestGeneratedMethods(unittest.TestCase):
    application = None

    def setUp(self):
        self.application = {application}()

    def tearDown(self):
        self.application = None

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass
"""
    print(head)
    for tc in testcases:
        body = _testcase_body_template(tc)
        print(body)
