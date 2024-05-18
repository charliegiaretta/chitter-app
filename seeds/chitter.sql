-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;


-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username text NOT NULL,
    email text NOT NULL,
    password text NOT NULL
);

CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    content text NOT NULL,
    post_time timestamp DEFAULT CURRENT_TIMESTAMP,
    user_id int,
    constraint fk_user foreign key(user_id)
    references users(id)
    on delete cascade
);
-- Finally, we add any records that are needed for the tests to run
INSERT INTO users (username, email, password) VALUES ('charliegiaretta', 'charliegiaretta@outlook.com', 'password123');

INSERT INTO posts (content, user_id) VALUES ('Hello World', 1)
