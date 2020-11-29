# Convert to test cases for these requirements
# The objects MUST exist with something() method.

test_suites = {
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
