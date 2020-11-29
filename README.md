# generate.py
Generic purpose unit tests generator. This project assumes that you have prior skills in code generation and unit testing.

  
    #!/bin/python
    # https://docs.python.org/3/library/unittest.html

Usage:

    python generate.py > units.py
    python -m unittest units.py


Convert to test cases for these statements

    cases = {
        "application": [
            "id exist",
            "id does not exist",
            "too old user cannot login"
        ],
    }

Build a list of cases per class name. In this example, application() will be tested aginst:

    test_id_exist()
    test_id_does_not_exist()
    test_too_old_user_cannot_login()

