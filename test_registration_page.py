from registration_page import *

def test_registration():
    db=show_registration_info("sapkota6","sapkota6")
    assert db=="Pass"
def test_registration1():
    db=show_registration_info("sapkota7","sapkota6")
    assert db=="Pass"
def test_registration2():
    db=show_registration_info("niraj","niraj")
    assert db=="Pass"
def test_registration3():
    db=show_registration(12346879)
    assert db=="Pass"

