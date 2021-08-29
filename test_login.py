from Login import *


def test_login():
    db = show_login_result("N", "N")
    assert db == "Pass"


def test_login1():
    db = show_login_result("123", "123")
    assert db == "Pass"


def test_login2():
    db = show_login_result("niraj2", "niraj")
    assert db == "Pass"
