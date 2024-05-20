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
    
    def find(self, id):
        rows = self._connection.execute("SELECT * FROM users WHERE id = %s", [id])
        row = rows[0]
        return User(
            row['id'], row['username'], row['email'], row['password'])
    
    def find_by_username(self, username):
        rows = self._connection.execute("SELECT * FROM users WHERE username = %s", (username,))
        row = rows[0] if rows else None
        return User(row['id'], row['username'], row['email'], row['password']) if row else None

    def find_by_email(self, email):
        rows = self._connection.execute("SELECT * FROM users WHERE email = %s", (email,))
        row = rows[0] if rows else None
        return User(row['id'], row['username'], row['email'], row['password']) if row else None

    def find_by_email_and_password(self, email, password):
        rows = self._connection.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
        if rows:
            row = rows[0]
            return User(row['id'], row['username'], row['email'], row['password'])
        return None    
    
    def create(self, user):
        if self.find_by_username(user.username):
            raise ValueError("Username already exists")
        if self.find_by_email(user.email):
            raise ValueError("Email already exists")
        rows = self._connection.execute(
            "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
            [user.username, user.email, user.password]
        )
        return None

