from lib.user import User

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM users")
        return [
            User(row['id'], row['username'], row['email'], row['password'])
            for row in rows
        ]
    
    def create(self, user):
        rows = self._connection.execute(
            "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
            [user.username, user.email, user.password]
        )
        return None
        # user.id = rows[0]["id"]

    def find(self, id):
        rows = self._connection.execute("SELECT * FROM users WHERE id = %s", [id])
        row = rows[0]
        return User(
            row['id'], row['username'], row['email'], row['password'])