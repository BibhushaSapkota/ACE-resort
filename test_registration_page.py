from registration_page import *
from Login import *
from room import *

def test_registration():
    db=show_registration_info("sapkota6","sapkota6")
    assert db=="Pass"

def test_registration3():
    db=show_registration(123468790)
    assert db=="Pass"

def test_login():
    db=show_login_result("bibhu","sapkota6")
    assert db == "Pass"

def test_room():
    db=show_insert("Room:1")
    assert db == "Pass"


def test_room2():
    db = show_insert("Hall:17")
    assert db == "Pass"



