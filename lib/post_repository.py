from lib.post import Post

class PostRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM posts")
        return [
            Post(row['id'], row['content'], row['post_time'], row['user_id'])
            for row in rows
        ]
    
    def create(self, user):
        rows = self._connection.execute(
            "INSERT INTO posts (content, post_time, user_id) VALUES (%s, %s, %s)",
            [user.content, user.post_time, user.user_id]
        )
        return None
    
    def find(self, id):
        rows = self._connection.execute("SELECT * FROM posts WHERE id = %s", [id])
        row = rows[0]
        return Post(
            row['id'], row['content'], row['post_time'], row['user_id'])