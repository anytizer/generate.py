# generate.py
Generic purpose unit tests generator for Python.
This project assumes that you have prior skills in code generation and [unit testing](https://docs.python.org/3/library/unittest.html).

Usage:

  #!/bin/python
  python generate.py > units.py
  python -m unittest units.py

Convert to test cases for these statements

  cases = {
      "application": [
          "id exists",
          "id does not exist",
          "too old user cannot login"
      ],
  }

Then, build a list of Test Cases per class name. In this example, `application()` object to be tested aginst:

  test_id_exists()
  test_id_does_not_exist()
  test_too_old_user_cannot_login()

