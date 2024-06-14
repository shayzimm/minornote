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