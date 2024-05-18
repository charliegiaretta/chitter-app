from lib.post import Post

def test_constructs(current_timestamp):
    user = Post(1, "Test content", current_timestamp, 1)
    assert user.id == 1
    assert user.content == "Test content"
    assert user.post_time == current_timestamp
    assert user.user_id == 1

def test_compares(current_timestamp):
    post_1 = Post(1, "Test content", current_timestamp, 1)
    post_2 = Post(1, "Test content", current_timestamp, 1)

def test_stringifying(current_timestamp):
    post = Post(1, "Test content", current_timestamp, 1)
    assert str(post) == f'Post(1, Test content, {current_timestamp}, 1)'