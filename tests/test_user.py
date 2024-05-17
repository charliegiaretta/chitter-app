from lib.user import User

def test_constructs():
    user = User(1, "Test username", "user@email.com", "password123")
    assert user.id == 1
    assert user.username == "Test username"
    assert user.email == "user@email.com"
    assert user.password == "password123"

def test_compares():
    user_1 = User(1, "Test username", "user@email.com", "password123")
    user_2 = User(1, "Test username", "user@email.com", "password123")
    assert user_1 == user_2

def test_stringifying():
    user = User(1, "Test username", "user@email.com", "password123")
    assert str(user) == 'User(1, Test username, user@email.com, password123)'