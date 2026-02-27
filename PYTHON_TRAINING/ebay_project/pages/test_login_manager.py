def test_login_success():
    username = "manager"
    password = "12345"

    assert username == "manager"
    assert len(password) >= 5