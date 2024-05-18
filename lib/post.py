class Post:
    def __init__(self, id, content, post_time, user_id):
        self.id = id
        self.content = content
        self.post_time = post_time
        self.user_id = user_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f'Post({self.id}, {self.content}, {self.post_time}, {self.user_id})'
