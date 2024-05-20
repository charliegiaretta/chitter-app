from lib.user import User
from lib.user_repository import UserRepository
import pytest

def test_all(db_connection):
    db_connection.seed("seeds/chitter.sql")
    repository = UserRepository(db_connection)
    assert repository.all() == [
        User(1, 'charliegiaretta', 'charliegiaretta@outlook.com', 'password123')
    ]

def test_find_by_username(db_connection):
    db_connection.seed("seeds/chitter.sql")
    repository = UserRepository(db_connection)
    user = repository.find_by_username('charliegiaretta')
    assert user == User(1, 'charliegiaretta', 'charliegiaretta@outlook.com', 'password123')

def test_find_by_email(db_connection):
    db_connection.seed("seeds/chitter.sql")
    repository = UserRepository(db_connection)
    user = repository.find_by_email('charliegiaretta@outlook.com')
    assert user == User(1, 'charliegiaretta', 'charliegiaretta@outlook.com', 'password123')

def test_find_by_email_and_password(db_connection):
    db_connection.seed("seeds/chitter.sql")
    repository = UserRepository(db_connection)
    user = repository.find_by_email_and_password('charliegiaretta@outlook.com', 'password123')
    assert user == User(1, 'charliegiaretta', 'charliegiaretta@outlook.com', 'password123')

def test_create(db_connection):
    db_connection.seed("seeds/chitter.sql")
    repository = UserRepository(db_connection)
    user = User(None, "Test username", "user@email.com", "password123")
    repository.create(user)
    assert repository.all() == [
        User(1, 'charliegiaretta', 'charliegiaretta@outlook.com', 'password123'),
        User(2, "Test username", "user@email.com", "password123")
    ]

def test_create_if_username_already_exists(db_connection):
    db_connection.seed("seeds/chitter.sql")
    repository = UserRepository(db_connection)
    user = User(None, "charliegiaretta", "user@email.com", "password123")
    with pytest.raises(ValueError) as err:
        repository.create(user)
    assert str(err.value) == "Username already exists"

def test_create_if_email_already_exists(db_connection):
    db_connection.seed("seeds/chitter.sql")
    repository = UserRepository(db_connection)
    user = User(None, "user", "charliegiaretta@outlook.com", "password123")
    with pytest.raises(ValueError) as err:
        repository.create(user)
    assert str(err.value) == "Email already exists"