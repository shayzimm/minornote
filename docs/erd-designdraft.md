# Entity Relationship Diagram

```plaintext
+-------------+       +-------------+       +-------------+       +-------------+
|    User     |       |    Post     |       |  Comment    |       |    Tag      |
+-------------+       +-------------+       +-------------+       +-------------+
| id (PK)     |---+   | id (PK)     |       | id (PK)     |       | id (PK)     |
| username    |   |   | title       |       | content     |       | name        |
| email       |   |   | content     |       | user_id (FK)|       +-------------+
| password    |   |   | user_id (FK)|       | post_id (FK)|           |       |
| role        |   |   | created_at  |       | created_at  |           |
+-------------+   |   +-------------+       +-------------+           |
                 |         |                                           |
                 |         |                                           |
                 |         +-------------------+                       |
                 |                             |                       |
                 |                             |                       |
                 +-----------------------------+-----------------------+
                                            |
                                            |
                                            |
                                      +-------------+
                                      |  post_tags  |
                                      +-------------+
                                      | post_id (FK)|
                                      | tag_id (FK) |
                                      +-------------+
```

User

- id (PK): Unique identifier for each user.
- username: The username of the user.
- first_name: The first name of the user
- last_name: The last name of the user
- email: The email address of the user.
- password: The hashed password of the user.
- role: The role of the user (e.g., admin, user).

Post

- id (PK): Unique identifier for each post.
- title: The title of the post.
- content: The content of the post.
- user_id (FK): Foreign key referencing the user who created the post.
- created_at: Timestamp when the post was created.

Comment

- id (PK): Unique identifier for each comment.
- content: The content of the comment.
- user_id (FK): Foreign key referencing the user who created the comment.
- post_id (FK): Foreign key referencing the post the comment is associated with.
- created_at: Timestamp when the comment was created.

Tag

- id (PK): Unique identifier for each tag.
- name: The name of the tag.
- post_tags
- post_id (FK): Foreign key referencing the post.
- tag_id (FK): Foreign key referencing the tag.

```sql
-- User table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(80) UNIQUE NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    password_hash VARCHAR(128) NOT NULL,
    role VARCHAR(50) DEFAULT 'user'
);

-- Post table
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title VARCHAR(120) NOT NULL,
    content TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (id)
);

-- Comment table
CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    content TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    post_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (post_id) REFERENCES posts (id)
);

-- Tag table
CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);

-- post_tags table (many-to-many relationship between posts and tags)
CREATE TABLE post_tags (
    post_id INTEGER NOT NULL,
    tag_id INTEGER NOT NULL,
    PRIMARY KEY (post_id, tag_id),
    FOREIGN KEY (post_id) REFERENCES posts (id) ON DELETE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES tags (id) ON DELETE CASCADE
);
```

User Table

- id: Unique identifier for each user (Primary Key).
- username: The username of the user (Unique, Not Null).
- email: The email address of the user (Unique, Not Null).
- password_hash: The hashed password of the user (Not Null).
- role: The role of the user (default is 'user').

Post Table

- id: Unique identifier for each post (Primary Key).
- title: The title of the post (Not Null).
- content: The content of the post (Not Null).
- user_id: Foreign key referencing the user who created the post (Not Null).
- created_at: Timestamp when the post was created (default is the current timestamp).

Comment Table

- id: Unique identifier for each comment (Primary Key).
- content: The content of the comment (Not Null).
- user_id: Foreign key referencing the user who created the comment (Not Null).
- post_id: Foreign key referencing the post the comment is associated with (Not Null).
- created_at: Timestamp when the comment was created (default is the current timestamp).

Tag Table

- id: Unique identifier for each tag (Primary Key).
- name: The name of the tag (Unique, Not Null).
- post_tags Table
- post_id: Foreign key referencing the post (Not Null).
- tag_id: Foreign key referencing the tag (Not Null).
- Primary Key: Combination of post_id and tag_id.
- Foreign Key Constraints: Ensures referential integrity by linking to the posts and tags tables, with cascading deletes to maintain consistency.
