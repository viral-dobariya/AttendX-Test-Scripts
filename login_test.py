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


if __name__ == "__main__":
    test_valid_login()
    test_empty_login()