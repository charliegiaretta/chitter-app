from lib.user import User
from lib.user_repository import UserRepository

def test_all(db_connection):
    db_connection.seed("seeds/chitter.sql")
    repository = UserRepository(db_connection)
    assert repository.all() == [
        User(1, 'charliegiaretta', 'charliegiaretta@outlook.com', 'password123')
    ]

def test_create(db_connection):
    db_connection.seed("seeds/chitter.sql")
    repository = UserRepository(db_connection)
    user = User(None, "Test username", "user@email.com", "password123")
    repository.create(user)
    assert repository.all() == [
        User(1, 'charliegiaretta', 'charliegiaretta@outlook.com', 'password123'),
        User(2, "Test username", "user@email.com", "password123")
    ]

def test_find(db_connection):
    db_connection.seed("seeds/chitter.sql")
    repository = UserRepository(db_connection)
    album = repository.find(1)
    assert album == User(1, 'charliegiaretta', 'charliegiaretta@outlook.com', 'password123')

    