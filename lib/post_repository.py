from lib.post import Post

class PostRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT p.id, p.content, p.post_time, u.username FROM posts p JOIN users u ON p.user_id = u.id")
        return [
            Post(row['id'], row['content'], row['post_time'], row['username'])
            for row in rows
        ]
    
    def create(self, user):
        rows = self._connection.execute(
            "INSERT INTO posts (content, user_id) VALUES (%s, %s) RETURNING id, post_time;",
            [user.content, user.username]
        )
        return None
    
    def find(self, id):
        rows = self._connection.execute("SELECT * FROM posts WHERE id = %s", [id])
        row = rows[0]
        return Post(
            row['id'], row['content'], row['post_time'], row['username'])