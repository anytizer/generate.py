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

# Convert to test cases for these requirements
cases = {
    "application": [
        "id exists",
        "id does not exist",
        "too old user cannot login",
    ],
    "password": [
        "do not accept weak password()",
        "change password(oldpassword, newpassword, confirmpassword)",
    ],
}

import re


# Process
# define classes
# define class methods
# handle input parameters
# create unit tests

class generator():

    # do not accept => do_not_accept
    def function_name(self, test_case: str):
        function_name = test_case.lower().replace(" ", "_")
        function_name = re.sub(r"\(.*?$", "", function_name, 0)
        return function_name

    # "", "get", "()", "get()", "get(a)", "get(a, b)"
    # split parameters within ()
    # insert "self" in the beginning
    # get parameters
    def variables(self, test_case: str):
        parameters = ["self"]
        parameter_string = ""

        lpos = test_case.find("(")
        rpos = test_case.find(")")

        if lpos >= 0 and rpos >= 0:
            parameter_string = case[lpos + 1:rpos]

        parameters.extend(parameter_string.split(","))
        variables = ", ".join([param for param in parameters if param])
        return variables


def _testcase_body_template(case: str):
    function_name = generator().function_name(case)
    variables = generator().variables(case)

    default_method = "something"
    body = f"""
    def test_{function_name}({variables}):
        data = []
        result = self.application.{default_method}(data)
        self.assertTrue(result)"""
    return body


initials = f"""#!/bin/python
# Warning: Auto generated code

import unittest
from .applications import application
from .applications import password
"""

print(initials)
for application, testcases in cases.items():
    head = f"""
class TestGeneratedMethods{application.title()}(unittest.TestCase):
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
        pass"""
    print(head)
    for case in testcases:
        body = _testcase_body_template(case)
        print(body)
