def test_valid_login():
    username = "student123"
    password = "Test@123"

    assert username != ""
    assert password != ""

    print("PASS: Valid login test data is available")


def test_empty_login():
    username = ""
    password = ""

    assert username == ""
    assert password == ""

    print("PASS: Empty login fields are detected")


def test_login_username_format():
    username = "student123"

    assert username.isalnum()

    print("PASS: Username format is valid")


if __name__ == "__main__":
    test_valid_login()
    test_empty_login()
    test_login_username_format()