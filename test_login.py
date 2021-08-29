from Login import *

def test_login():
    db = show_login_result("1", "1")
    assert db == "Pass"


def test_login1():
    db = show_login_result("123", "456")
    assert db == "Pass"


def test_login2():
    db = show_login_result("kjb2", "kj")
    assert db == "Pass"
