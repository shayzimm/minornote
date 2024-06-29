# MinorNote

## Introduction

**MinorNote** is a microblogging platform API that provides functionality for user authentication, blog post management, commenting, and tagging. It is built using Flask and SQLAlchemy, and it aims to offer a secure and scalable solution for microblogging needs.

## Table of Contents

- [MinorNote](#minornote)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
    - [R1: Problem and Solution](#r1-problem-and-solution)
    - [R2: Task Allocation and Tracking](#r2-task-allocation-and-tracking)
    - [R3: Third-Party Services, Packages, and Dependencies](#r3-third-party-services-packages-and-dependencies)
    - [R4: Benefits and Drawbacks of PostgreSQL](#r4-benefits-and-drawbacks-of-postgresql)
    - [R5: Features and Functionalities of SQLAlchemy](#r5-features-and-functionalities-of-sqlalchemy)
    - [R6: Entity Relationship Diagram (ERD)](#r6-entity-relationship-diagram-erd)
    - [R7: Models and Their Relationships](#r7-models-and-their-relationships)
    - [R8: API Endpoints](#r8-api-endpoints)
      - [Users](#users)
      - [Posts](#posts)
      - [Comments](#comments)
      - [Tags](#tags)
    - [Help Documentation](#help-documentation)
    - [References](#references)

### R1: Problem and Solution

Microblogging platforms are popular due to their ability to provide quick and easy content sharing, community building, and user interaction. However, many of these platforms lack certain features that can enhance user experience and content management. Common issues include:

1. Many microblogging platforms do not provide tagging systems that allow users to categorise their posts effectively. This makes content discovery and organisation difficult.
2. Secure and efficient user authentication is crucial, yet some platforms have outdated or insecure methods for managing user accounts and sessions.
3. User interaction through comments is often poorly managed, leading to a cluttered and unorganised user experience.
4. As user bases grow, platforms often struggle with scalability and performance issues due to inefficient database design and lack of sufficient backend infrastructure.

According to a 2021 study by Statista, there were over 3.6 billion social media users worldwide, and this number is expected to increase to nearly 4.41 billion by 2025. The sheer volume of users highlights the need for scalable and efficient microblogging platforms.
A report by DataReportal in 2022 indicated that 54.9% of internet users look for information on brands and products through social networks. This underscores the importance of effective content categorisation and user engagement.

**How MinorNote Addresses the Problem**:

1. **Tagging System**:
   - MinorNote provides a tagging system that allows users to categorise their posts with multiple tags. This many-to-many relationship between posts and tags enables users to categorise their posts in multiple ways, making content more accessible and easier to discover. For example, a user could tag a post with "Technology", "AI", and "Innovation", making it visible under all three categories.

2. **Secure User Authentication**:
   - JWT (JSON Web Tokens) has been implemented for secure user authentication. This means that each user session is represented by a token, which includes user information and session validity. This approach not only secures user data but also enhances the scalability of the application by reducing the load on the server to maintain user sessions.

3. **Comment Management**:
   - MinorNote provides endpoints for creating, reading, updating, and deleting comments on posts. This CRUD functionality ensures that comments can be managed effectively, preventing clutter and enhancing the user experience. Users can engage in meaningful discussions, knowing that their comments can be managed and moderated appropriately.

4. **Scalability and Performance**:
   - Built with Flask and SQLAlchemy, MinorNote is designed for scalability. The database is structured with normalised tables to handle large volumes of data efficiently. PostgreSQL, known for its reliability and performance, is used as the database system.

### R2: Task Allocation and Tracking

Tasks were planned and tracked using a Kanban board, a visual workflow management tool that provides clarity and structure to a project’s progress. The Kanban board was hosted on Trello, a widely used task management tool.

**Planning Process**:

1. **Initial Setup**:
   - The project started with a brainstorming session to identify all the tasks required to complete the project.
   - Tasks were broken down into smaller, manageable subtasks to ensure every aspect of the project was covered.

2. **Task Categorisation**:
   - Tasks were categorised into different columns on the Kanban board: Backlog, Design, To Do, Doing, Testing, and Done.
   - Each column represented a stage in the development process, allowing for easy tracking of task progress.

3. **Prioritisation**:
   - Tasks were prioritised based on their importance.
   - High-priority tasks, like core features and security implementations, were addressed first to ensure the project's stability and functionality.

**Tracking Process**:

1. **Daily Check-ins**:
   - Daily check-ins were conducted to assess progress, identify roadblocks, and plan next steps, and maintain accountability.

2. **Kanban Board Updates**:
   - My Kanban board was updated in real-time as tasks moved from one stage to another.
   - Each task card included descriptions, user stories, and due dates to prevent confusion and for effective time management.

3. **Review and Adjustments**:
   - Completed tasks were moved to the Testing column for self-evaluation.
   - Any necessary changes or improvements were made before tasks were marked as Done.

The usage of the Kanban board can be seen throughout the project. Every task, from initial setup, was tracked. The board provides a view of the project’s workflow, planning and tracking involved in development.

You can view the Kanban board used for the project [here](https://trello.com/invite/b/5LMBpS52/ATTIe9d6d662e94ae1cba29b55fc075a77b1711AC91E/minornote).

### R3: Third-Party Services, Packages, and Dependencies

The MinorNote API utilises several third-party services, packages, and dependencies to ensure a robust, secure, and efficient development and runtime environment.

1. **bcrypt** (`bcrypt==4.1.3`)
   - Password hashing function designed for secure password storage. It provides a hashing algorithm that is highly resistant to brute-force attacks.

2. **blinker** (`blinker==1.8.2`)
   - Provides a fast dispatching system for creating signals in Python. It is used for event-driven programming within the Flask application.

3. **click** (`click==8.1.7`)
   - A Python package for creating command-line interfaces in a composable way, and is used by Flask for command-line operations.

4. **exceptiongroup** (`exceptiongroup==1.2.1`)
   - Package that helps in handling and managing multiple exceptions in a more structured manner, especially useful for debugging complex applications.

5. **Flask** (`Flask==3.0.3`)
   - Flask is a lightweight WSGI web application framework in Python, and provides the core functionality for building MinorNote, including routing and request handling.

6. **Flask-Bcrypt** (`Flask-Bcrypt==1.0.1`)
   - An extension that integrates bcrypt into Flask, providing utilities for password hashing.

7. **Flask-JWT-Extended** (`Flask-JWT-Extended==4.6.0`)
   - Extension for adding JWT authentication to Flask applications, used for secure user authentication and session management.

8. **flask-marshmallow** (`flask-marshmallow==1.2.1`)
   - An integration layer for Flask and Marshmallow, providing object serialization/deserialization and validation.

9. **Flask-SQLAlchemy** (`Flask-SQLAlchemy==3.1.1`)
    - Extension for Flask that adds support for SQLAlchemy, a SQL toolkit and ORM, provides a high-level API for database interactions.

10. **greenlet** (`greenlet==3.0.3`)
    - A coroutine library that allows for concurrent execution of code, used internally by SQLAlchemy and other packages for asynchronous operations.

11. **itsdangerous** (`itsdangerous==2.2.0`)
    - Provides safe data serialisation and deserialisation, used by Flask for securely signing data to ensure integrity.

12. **Jinja2** (`Jinja2==3.1.4`)
    - A templating engine for Python, used by Flask for rendering HTML templates.

13. **Mako** (`Mako==1.3.5`)
    - Another templating engine for Python, similar to Jinja2 with different syntax and features.

14. **MarkupSafe** (`MarkupSafe==2.1.5`)
    - A library for safe handling of HTML and XML in Python.

15. **marshmallow** (`marshmallow==3.21.3`)
    - Marshmallow is a library for object serialization/deserialization and validation. It simplifies the conversion between complex data types and native Python data types.

16. **marshmallow-sqlalchemy** (`marshmallow-sqlalchemy==1.0.0`)
    - Provides integration between Marshmallow and SQLAlchemy, allowing for easy serialization/deserialization of SQLAlchemy models.

17. **packaging** (`packaging==24.1`)
    - Packaging provides utilities for dealing with Python packages and versions.

18. **pluggy** (`pluggy==1.5.0`)
    - Plugin management framework used internally by various Python tools.

19. **psycopg2-binary** (`psycopg2-binary==2.9.9`)
    - A PostgreSQL database adapter for Python, allowing for efficient interaction with PostgreSQL databases.

20. **PyJWT** (`PyJWT==2.8.0`)
    - Python library for encoding and decoding JSON Web Tokens, used by Flask-JWT-Extended for JWT handling.

21. **python-dotenv** (`python-dotenv==1.0.1`)
    - Python-dotenv reads key-value pairs from a .env file and can set them as environment variables for configuration management.

22. **SQLAlchemy** (`SQLAlchemy==2.0.30`)
    - An SQL toolkit and Object-Relational Mapping library for Python that provides the core functionality for database interactions in MinorNote.

23. **tomli** (`tomli==2.0.1`)
    - TOML parser for Python, used for reading and writing TOML configuration files (unused).

24. **typing_extensions** (`typing_extensions==4.12.2`)
    - Provides backports of new typing features introduced in newer Python versions.

25. **Werkzeug** (`Werkzeug==3.0.3`)
    - WSGI web application library used by Flask for request handling and various other utilities.

### R4: Benefits and Drawbacks of PostgreSQL

**Benefits**:

1. **Reliability**:
   - PostgreSQL is fully ACID - Atomicity, Consistency, Isolation, Durability - compliant. This means that transactions are processed reliably and adhere to all the rules of a relational database.
   - Supports various data integrity constraints, such as primary keys, foreign keys, `UNIQUE` constraints, and `CHECK` constraints, which enforce rules on data to maintain accuracy and consistency.

2. **Advanced Features**:
   - Includes full-text search capabilities, allowing for efficient search operations within text data.
   - Provides support for JSON data types, enabling efficient storage and querying of JSON data. This feature is beneficial for applications that require flexible schema or semi-structured data.
   - PostgreSQL's architecture allows users to define custom functions, operators, and data types, making it highly extensible. Users can also create extensions that add new functionalities.

3. **Performance**:
   - Includes a query planner and optimiser that enhances the performance of complex queries.
   - PostgreSQL's Multi-Version Concurrency Control allows for concurrent transactions without locking issues.

4. **Scalability**:
   - PostgreSQL supports replication methods, like streaming replication and logical replication, for horizontal scalability.
   - Handles large datasets and high transaction loads, making it suitable for applications that require vertical scalability.

5. **Security**:
   - PostgreSQL provides granular access control mechanisms, role-based access control, that ensures users have appropriate permissions.
   - Data encryption at various levels, including column-level encryption and SSL/TLS for secure data transmission.

6. **Open Source**:
   - Open-source and free to use.
   - Large community that contributes to its development, and provides support and resources.

**Drawbacks**:

1. **Complexity**:
   - PostgreSQL's complex features can be difficult for beginners to learn.
   - Properly configuring PostgreSQL for optimal performance can be challenging and requires understanding of its settings and parameters.

2. **Resource Intensive**:
   - Compared to some other lightweight database systems, PostgreSQL can be more resource-intensive in terms of memory and CPU usage. This may not be ideal for applications with limited resources.

3. **Hosting and Deployment**:
   - Not as widely available on shared hosting services compared to other databases like MySQL. Users might need to opt for more expensive hosting solutions such as virtual private servers or cloud hosting.
   - Deploying PostgreSQL can be complex and requires advanced knowledge and experience.

4. **Tooling and Ecosystem**:
   - While PostgreSQL has excellent tools and extensions, some tools and applications are more optimised or only available for other databases, like MySQL and Oracle. This can limit the choices of third-party tools and integrations.

### R5: Features and Functionalities of SQLAlchemy

SQLAlchemy is a powerful and flexible ORM system for Python that provides tools to work with databases in an object-oriented way. It abstracts the database interactions into Python objects, making database operations easier and more intuitive.

**1. ORM and Declarative Mapping**:

SQLAlchemy's ORM allows you to define Python classes that are mapped to database tables. The `declarative_base` function provides a base class for declarative class definitions.

```python
from sqlalchemy.orm import DeclarativeBase

# Define the base class for SQLAlchemy models
class Base(DeclarativeBase):
    pass
```

**2. Schema Definition:**

SQLAlchemy allows you to define the schema of your database using Python classes. You can specify data types, constraints, and relationships directly within the class definition.

```py
class Post(db.Model):
    __tablename__ = 'posts'

    # # Define columns with data types and constraints
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(120))
    content: Mapped[Optional[str]] = mapped_column(Text())
    # A user can create multiple posts, thanks to the user_id foreign key
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete="CASCADE"))
    date_created: Mapped[date]

    # Define relationships to other tables
    user: Mapped['User'] = relationship('User', back_populates='posts')
    # A post can have multiple comments
    comments: Mapped[List['Comment']] = relationship('Comment', back_populates='post', cascade="all, delete-orphan")
    # A post can have multiple tags and a tag can have multiple posts, defined by the tags attribute in Post and the post_tags association
    tags: Mapped[List['Tag']] = relationship('Tag', secondary='post_tags', back_populates='posts')
```

**3. Query Construction and Execution:**

SQLAlchemy provides a powerful query API that allows you to construct and execute complex queries in an intuitive way. The ORM automatically translates these queries into SQL.

```py
    # Create a SQLAlchemy query to select all posts
    # selects all records from the posts table
    stmt = db.select(Post)
    posts = db.session.scalars(stmt).all()
    # Serialize the list of posts and return as JSON
    return jsonify(PostSchema(many=True).dump(posts))
```

**4. Relationship Handling:**

SQLAlchemy supports defining and managing relationships between tables, such as one-to-many, many-to-many, and one-to-one relationships. This is done using the `relationship` and `ForeignKey` constructs.

```py
class Comment(db.Model):
    __tablename__ = "comments"

    # Define columns with data types and constraints
    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(Text())
    # A user can create multiple comments - defined by user_id FK
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete="CASCADE"))
    # A post can have multiple comments - defined by post_id FK
    # cascade="all, delete-orphan" argument ensures that all associated comments are deleted if the post is deleted
    post_id: Mapped[int] = mapped_column(ForeignKey('posts.id', ondelete="CASCADE"))
    date_created: Mapped[date]

    # Define relationships to other tables
    user: Mapped['User'] = relationship('User', back_populates='comments')
    post: Mapped['Post'] = relationship('Post', back_populates='comments')
```

**5. Transaction Management:**

SQLAlchemy handles database transactions seamlessly. You can commit, rollback, and manage transactions using the session object.

```py
@tags_bp.route('/tags', methods=['POST'])
@jwt_required()
def create_tag():
    try:
        # Validate and deserialize the request JSON data
        tag_info = TagSchema(only=['name']).load(request.json, unknown='exclude')
    except ValidationError as err:
        # Return validation errors as JSON with status 400
        return jsonify(err.messages), 400

    # Create a new Tag instance
    tag = Tag(
        name=tag_info.get('name')
    )
    # Add the new tag to the session and commit to the database
    db.session.add(tag)
    db.session.commit()
    # Serialize the new tag and return as JSON with status 201
    return jsonify(TagSchema().dump(tag)), 201
```

**6. Migrations:**

While not a part of SQLAlchemy itself, it integrates well with Alembic, a lightweight database migration tool that allows you to manage database schema changes over time.

**7. Extensibility and Custom Types:**

SQLAlchemy allows you to define custom data types and extend the functionality of the ORM, and can be useful for implementing domain-specific logic.

### R6: Entity Relationship Diagram (ERD)

**Entity Relationship Diagram (ERD)**

The MinorNote ERD can be found [here](docs/minornote_erd.pdf).

**Normalisation Explanation:**

First Normal Form:

- All attributes contain only atomic values. There are no repeating groups or arrays.
- In MinorNote ERD, each table has a primary key, each field contains only single values.

Second Normal Form:

- All attributes are fully functionally dependent on the primary key.
- Non-key attributes are not dependent on any subset of a candidate key.
- In the Posts table, attributes like title, content, and user_id depend entirely on the primary key id.

Third Normal Form:

- There are no transitive dependencies; non-key attributes are not dependent on other non-key attributes.
- In the Users table, username, email, password, first_name, and last_name are only dependent on the primary key id.

**Entity Relationships:**

Users to Posts:

- One-to-Many: One user can create many posts, represented by a foreign key user_id in the Posts table that references the id in the Users table.

Posts to Comments:

- One-to-Many: One post can have many comments - foreign key post_id in the Comments table that references the id in the Posts table.
- One-to-Many: One user can make many comments - a foreign key user_id in the Comments table that references the id in the Users table.

Posts to Tags:

- Many-to-Many: One post can have many tags, and one tag can be associated with many posts. The post_tags association table describes this relationship and contains foreign keys post_id and tag_id that reference the id in the Posts and Tags tables.

**Comparison to Other Normalisation Levels:**

Unnormalised Form:

- An unnormalised database might have a single table with repeated groups, such as a Posts table containing multiple tags in a single field, separated by commas. This approach leads to data redundancy and anomalies.

First Normal Form:

- The database design would ensure that each field contains only atomic values. For example, the Tags field in the Posts table would be broken down into individual rows in a PostTags table to avoid repeating groups.

Second Normal Form:

- The database would remove partial dependencies e.g. if the Posts table had fields that depended only on part of the composite key, those fields would be moved to a separate table.

Third Normal Form:

- Transitive dependencies would be eliminated ie. if the Posts table had a field like author_email (dependent on user_id), this field would be removed since it introduces a transitive dependency.

### R7: Models and Their Relationships

**Models**:

1. **User**:
   - A user in the application.
   - Attributes: `id`, `username`, `email`, `password`, `first_name`, `last_name`, `is_admin`.
   - Relationships: One-to-Many with `Post` and `Comment`.

2. **Post**:
   - A blog post created by a user.
   - Attributes: `id`, `title`, `content`, `user_id`, `date_created`.
   - Relationships: One-to-Many with `Comment`, Many-to-Many with `Tag`.

3. **Comment**:
   - A comment on a post.
   - Attributes: `id`, `content`, `user_id`, `post_id`, `date_created`.
   - Relationships: Many-to-One with `User` and `Post`.

4. **Tag**:
   - A tag associated with posts.
   - Attributes: `id`, `name`.
   - Relationships: Many-to-Many with `Post`.

5. **PostTags**:
   - many-to-many relationship between posts and tags
   - Attributes: `post_id`, `tag_id`.

**Relationships**:

1. **User to Post**:
   - One user can create multiple posts.
   - This is represented by the `user_id` foreign key in the `Post` model.

     ```python
     class Post(db.Model):
      __tablename__ = 'posts'

      # # Define columns with data types and constraints
      id: Mapped[int] = mapped_column(primary_key=True)
      title: Mapped[str] = mapped_column(String(120))
      content: Mapped[Optional[str]] = mapped_column(Text())
      # A user can create multiple posts, thanks to the user_id foreign key
      user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete="CASCADE"))
      date_created: Mapped[date]

      # Define relationships to other tables
      user: Mapped['User'] = relationship('User', back_populates='posts')
      # A post can have multiple comments
      comments: Mapped[List['Comment']] = relationship('Comment', back_populates='post', cascade="all, delete-orphan")
      # A post can have multiple tags and a tag can have multiple posts, defined by the tags attribute in Post and the post_tags association
      tags: Mapped[List['Tag']] = relationship('Tag', secondary='post_tags', back_populates='posts')
     ```

2. **Post to Comment**:
   - One post can have multiple comments.
   - This is represented by the `post_id` foreign key in the `Comment` model.

     ```python
     class Comment(db.Model):
        __tablename__ = 'comments'
        # Define columns with data types and constraints
        id: Mapped[int] = mapped_column(primary_key=True)
        content: Mapped[str] = mapped_column(Text())
        # A user can create multiple comments - defined by user_id FK
        user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete="CASCADE"))
        # A post can have multiple comments - defined by post_id FK
        # cascade="all, delete-orphan" argument ensures that all associated comments are deleted if the post is deleted
        post_id: Mapped[int] = mapped_column(ForeignKey('posts.id', ondelete="CASCADE"))
        date_created: Mapped[date]

        # Define relationships to other tables
        user: Mapped['User'] = relationship('User', back_populates='comments')
        post: Mapped['Post'] = relationship('Post', back_populates='comments')
     ```

3. **Post to Tag**:
   - One post can have multiple tags, and one tag can be associated with multiple posts.
   - This is represented by the `post_tags` association table.

     ```python
      # This association table is used to establish the many-to-many relationship between posts and tags, allowing a post to have multiple tags and a tag to be associated with multiple posts.
      post_tags = Table(
          'post_tags',
          db.metadata,
          Column('post_id', Integer, ForeignKey('posts.id', ondelete="CASCADE"), primary_key=True),
          Column('tag_id', Integer, ForeignKey('tags.id', ondelete="CASCADE"), primary_key=True)
      )
     ```

4. **User to Comment**:
   - One user can make multiple comments.
   - This is represented by the `user_id` foreign key in the `Comment` model.

     ```python
     class Comment(db.Model):
        __tablename__ = "comments"

        # Define columns with data types and constraints
        id: Mapped[int] = mapped_column(primary_key=True)
        content: Mapped[str] = mapped_column(Text())
        # A user can create multiple comments - defined by user_id FK
        user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete="CASCADE"))
     ```

**Queries Using Relationships**:

1. **Get all posts by a specific user**:
   - This query retrieves all posts created by a specific user.

     ```python
      # Retrieve all posts by a specific user
      # If the user does not exist, it raises a 404 error
      user = db.get_or_404(User, user_id)
      # Use the relationship to get all posts associated with the user
      posts = user.posts
      # Serialize the list of posts and return as JSON
      return jsonify(PostSchema(many=True).dump(posts))
     ```

2. **Get all comments on a specific post**:
   - This query retrieves all comments associated with a specific post.

     ```python
      # Create a SQLAlchemy query to filter comments by post_id
      comments = Comment.query.filter_by(post_id=post_id).all()
      # Serialize the list of comments and return as JSON
      return jsonify(CommentSchema(many=True).dump(comments)), 200
     ```

3. **Get all posts with a specific tag**:
   - This query retrieves all posts that have a specific tag.

     ```python
      # Retrieve the tag by ID
      tag = Tag.query.get_or_404(tag_id)
      # This attribute uses the relationship defined in the Tag model to get all posts associated with the tag
      # It leverages the many-to-many relationship between Post and Tag models
      posts = tag.posts  # Use the relationship to get all posts associated with the tag
      # Serialize the list of posts and return as JSON
      return jsonify(PostSchema(many=True).dump(posts)), 200
     ```

4. **Get all comments made by a specific user**:
   - This query retrieves all comments made by a specific user.

     ```python
      # Create a SQLAlchemy query to filter comments by user_id
      comments = Comment.query.filter_by(user_id=user_id).all()
      # Serialize the list of comments and return as JSON
      return jsonify(CommentSchema(many=True).dump(comments)), 200
     ```

### R8: API Endpoints

Please also see the [help documentation](docs/help.md) for more details on getting started.

#### Users

1. **Register User**
   - **HTTP Verb**: POST
   - **Route Path**: `/users/register`
   - **Required Body Data**:

     ```json
      {
        "username": "yourusername",
        "email": "youremail@example.com",
        "password": "yourpassword",
        "first_name": "YourFirstName",
        "last_name": "YourLastName"
      }
     ```

   - **Success Response** 201 OK:

     ```json
      {
        "id": 1,
        "username": "user1",
        "email": "user1@example.com",
        "first_name": "FirstName1",
        "last_name": "LastName1",
        "is_admin": false
      }
     ```

   - **Failure Response**:
   - 409 Conflict:

     ```json
      {
        "error": "User already exists"
      }
     ```

   - 400 Bad Request:

     ```json
      {
        "error": "Validation errors"
      }
     ```

2. **Login User**
   - **HTTP Verb**: POST
   - **Route Path**: `/users/login`
   - **Required Body Data**:

     ```json
      {
        "email": "youremail@example.com",
        "password": "yourpassword"
      }
     ```

   - **Success Response** 200 OK:

     ```json
      {
        "token": "<your_jwt_token>"
      }
     ```

   - **Failure Response**:
   - 401 Unauthorized:

     ```json
     {
       "error": "Invalid email or password"
     }
     ```

   - 400 Bad Request:

     ```json
     {
       "error": "Validation errors"
     }
     ```

3. **Get All Users**
   - **HTTP Verb**: GET
   - **Route Path**: `/users/`
   - **Required Header**: `Authorization: Bearer <your_jwt_token>` (Admin only)

   - **Success Response** 200 OK:

     ```json
     [
      {
        "id": 1,
        "username": "user1",
        "email": "user1@example.com",
        "first_name": "FirstName1",
        "last_name": "LastName1",
        "is_admin": false
      },
      ...
     ]
     ```

   - **Failure Response**: 
   - 403 Forbidden:

     ```json
     {
       "error": "You must be an admin to access this resource"
     }
     ```

   - 400 Unauthorized:

     ```json
     {
       "error": "Validation errors"
     }
     ```

4. **Get One User**
   - **HTTP Verb**: GET
   - **Route Path**: `/users/<int:id>`
   - **Required Header**: `Authorization: Bearer <token>`

   - **Success Response** 200 OK:

     ```json
      {
        "id": 1,
        "username": "user1",
        "email": "user1@example.com",
        "first_name": "FirstName1",
        "last_name": "LastName1",
        "is_admin": false
      }
     ```

   - **Failure Response**:
   - 404:

     ```json
     {
       "error": "User not found"
     }
     ```

   - 400 Unauthorized:

     ```json
     {
       "error": "Missing Authorization Header"
     }
     ```

5. **Update User**
   - **HTTP Verb**: PUT/PATCH
   - **Route Path**: `/users/<int:id>`
   - **Required Header**: `Authorization: Bearer <token>` (Owner only)

   - **Required Body Data**:

     ```json
      {
        "username": "newusername",
        "email": "newemail@example.com",
        "password": "newpassword",
        "first_name": "NewFirstName",
        "last_name": "NewLastName"
      }
     ```

   - **Success Response** 200 OK:

     ```json
      {
        "id": 1,
        "username": "newusername",
        "email": "newemail@example.com",
        "first_name": "NewFirstName",
        "last_name": "NewLastName",
        "is_admin": false
      }
     ```

   - **Failure Response**:
   - 403 Forbidden:

     ```json
     {
       "error": "You must be the owner of the resource to access this"
     }
     ```

   - 400 Unauthorized:

     ```json
     {
       "error": "Validation errors"
     }
     ```

   - 409 Conflict:

     ```json
     {
       "error": "Username already exists"
     }
     ```

6. **Delete User**
   - **HTTP Verb**: DELETE
   - **Route Path**: `/users/<int:id>`
   - **Required Header**:

     ```txt
     Authorization: Bearer <token>
     ```

   - **Success Response** (HTTP 204):

     ```json
     {}
     ```

   - **Failure Response** (HTTP 403):

     ```json
     {
       "error": "Unauthorized"
     }
     ```

#### Posts

1. **Get All Posts**
   - **HTTP Verb**: GET
   - **Route Path**: `/posts/`
   - **Required Header**:

     ```txt
     Authorization: Bearer <token>
     ```

   - **Success Response** (HTTP 200):

     ```json
     [
       {
         "id": 1,
         "title": "string",
         "content": "string",
         "user": {
           "id": 1,
           "username": "string"
         },
         "comments": [
           ...
         ],
         "tags": [
           ...
         ],
         "date_created": "date"
       },
       ...
     ]
     ```

   - **Failure Response** (HTTP 403):

     ```json
     {
       "error": "Unauthorized"
     }
     ```

2. **Get One Post**
   - **HTTP Verb**: GET
   - **Route Path**: `/posts/<int:id>`
   - **Required Header**:

     ```txt
     Authorization: Bearer <token>
     ```

   - **Success Response** (HTTP 200):

     ```json
     {
       "id": 1,
       "title": "string",
       "content": "string",
       "user": {
         "id": 1,
         "username": "string"
       },
       "comments": [
         ...
       ],
       "tags": [
         ...
       ],
       "date_created": "date"
     }
     ```

   - **Failure Response** (HTTP 404):

     ```json
     {
       "error": "Post not found"
     }
     ```

3. **Create Post**
   - **HTTP Verb**: POST
   - **Route Path**: `/posts/`
   - **Required Header**:

     ```txt
     Authorization: Bearer <token>
     ```

   - **Required Body Data**:

     ```json
     {
       "title": "string",
       "content": "string"
     }
     ```

   - **Success Response** (HTTP 201):

     ```json
     {
       "id": 1,
       "title": "string",
       "content": "string",
       "user_id": 1,
       "date_created": "date"
     }
     ```

   - **Failure Response** (HTTP 403):

     ```json
     {
       "error": "Unauthorized"
     }
     ```

   - **Failure Response** (HTTP 400):

     ```json
     {
       "error": "Validation errors"
     }
     ```

4. **Update Post**
   - **HTTP Verb**: PUT/PATCH
   - **Route Path**: `/posts/<int:id>`
   - **Required Header**:

     ```txt
     Authorization: Bearer <token>
     ```

   - **Required Body Data**:

     ```json
     {
       "title": "string",
       "content": "string"
     }
     ```

   - **Success Response** (HTTP 200):
  
     ```json
     {
       "id": 1,
       "title": "string",
       "content": "string",
       "user_id": 1,
       "date_created": "date"
     }
     ```

   - **Failure Response** (HTTP 403):

     ```json
     {
       "error": "Unauthorized"
     }
     ```

   - **Failure Response** (HTTP 400):

     ```json
     {
       "error": "Validation errors"
     }
     ```

5. **Delete Post**
   - **HTTP Verb**: DELETE
   - **Route Path**: `/posts/<int:id>`
   - **Required Header**:

     ```txt
     Authorization: Bearer <token>
     ```

   - **Success Response** (HTTP 204):

     ```json
     {}
     ```

   - **Failure Response** (HTTP 403):

     ```json
     {
       "error": "Unauthorized"
     }
     ```

#### Comments

1. **Create Comment**
   - **HTTP Verb**: POST
   - **Route Path**: `/posts/<int:post_id>/comments`
   - **Required Header**:

     ```txt
     Authorization: Bearer <token>
     ```

   - **Required Body Data**:

     ```json
     {
       "content": "string"
     }
     ```

   - **Success Response** (HTTP 201):

     ```json
     {
       "id": 1,
       "content": "string",
       "user_id": 1,
       "post_id": 1,
       "date_created": "date"
     }
     ```

   - **Failure Response** (HTTP 403):

     ```json
     {
       "error": "Unauthorized"
     }
     ```

   - **Failure Response** (HTTP 400):

     ```json
     {
       "error": "Validation errors"
     }
     ```

2. **Get All Comments on a Post**
   - **HTTP Verb**: GET
   - **Route Path**: `/posts/<int:post_id>/comments`
   - **Required Header**:

     ```txt
     Authorization: Bearer <token>
     ```

   - **Success Response** (HTTP 200):

     ```json
     [
       {
         "id": 1,
         "content": "string",
         "user": {
           "id": 1,
           "username": "string"
         },
         "date_created": "date"
       },
       ...
     ]
     ```

   - **Failure Response** (HTTP 403):

     ```json
     {
       "error": "Unauthorized"
     }
     ```

3. **Update Comment**
   - **HTTP Verb**: PUT/PATCH
   - **Route Path**: `/posts/<int:post_id>/comments/<int:comment_id>`
   - **Required Header**:

     ```txt
     Authorization: Bearer <token>
     ```

   - **Required Body Data**:

     ```json
     {
       "content": "string"
     }
     ```

   - **Success Response** (HTTP 200):

     ```json
     {
       "message": "Comment updated successfully"
     }
     ```

   - **Failure Response** (HTTP 403):

     ```json
     {
       "error": "Unauthorized"
     }
     ```

   - **Failure Response** (HTTP 400):

     ```json
     {
       "error": "Validation errors"
     }
     ```

4. **Delete Comment**
   - **HTTP Verb**: DELETE
   - **Route Path**: `/posts/<int:post_id>/comments/<int:comment_id>`
   - **Required Header**:

     ```txt
     Authorization: Bearer <token>
     ```

   - **Success Response** (HTTP 200):

     ```json
     {
       "message": "Comment deleted successfully"
     }
     ```

   - **Failure Response** (HTTP 403):

     ```json
     {
       "error": "Unauthorized"
     }
     ```

#### Tags

1. **Get All Tags**
   - **HTTP Verb**: GET
   - **Route Path**: `/tags`
   - **Required Header**:

     ```txt
     Authorization: Bearer <token>
     ```

   - **Success Response** (HTTP 200):

     ```json
     [
       {
         "id": 1,
         "name": "string"
       },
       ...
     ]
     ```

   - **Failure Response** (HTTP 403):

     ```json
     {
       "error": "Unauthorized"
     }
     ```

2. **Create Tag**
   - **HTTP Verb**: POST
   - **Route Path**: `/tags`
   - **Required Header**:

     ```txt
     Authorization: Bearer <token>
     ```

   - **Required Body Data**:

     ```json
     {
       "name": "string"
     }
     ```

   - **Success Response** (HTTP 201):

     ```json
     {
       "id": 1,
       "name": "string"
     }
     ```

   - **Failure Response** (HTTP 403):

     ```json
     {
       "error": "Unauthorized"
     }
     ```

3. **Update Tag**
   - **HTTP Verb**: PUT/PATCH
   - **Route Path**: `/tags/<int:tag_id>`
   - **Required Header**:

     ```txt
     Authorization: Bearer <token>
     ```

   - **Required Body Data**:

     ```json
     {
       "name": "string"
     }
     ```

   - **Success Response** (HTTP 200):

     ```json
     {
       "message": "Tag updated successfully"
     }
     ```

   - **Failure Response** (HTTP 403):

     ```json
     {
       "error": "Validation errors"
     }
     ```

4. **Delete Tag**
   - **HTTP Verb**: DELETE
   - **Route Path**: `/tags/<int:tag_id>`
   - **Required Header**:

     ```txt
     Authorization: Bearer <token>
     ```

   - **Success Response** (HTTP 200):

     ```json
     {
       "message": "Tag deleted successfully"
     }
     ```

   - **Failure Response** (HTTP 403):

     ```json
     {
       "error": "Unauthorized"
     }
     ```

5. **Get Posts by Tag**
   - **HTTP Verb**: GET
   - **Route Path**: `/tags/<int:tag_id>/posts`
   - **Required Header**:

     ```txt
     Authorization: Bearer <token>
     ```

   - **Success Response** (HTTP 200):

     ```json
     [
       {
         "id": 1,
         "title": "string",
         "content": "string",
         "user": {
           "id": 1,
           "username": "string"
         },
         "comments": [
           ...
         ],
         "tags": [
           ...
         ],
         "date_created": "date"
       },
       ...
     ]
     ```

   - **Failure Response** (HTTP 403):

     ```json
     {
       "error": "Unauthorized"
     }
     ```

### Help Documentation

Can be found [here](docs/help.md)

### References

1. Statista. (2021). Number of social media users worldwide from 2017 to 2025 (in billions). Retrieved from [Statista](https://www.statista.com/statistics/278414/number-of-worldwide-social-network-users/).
2. DataReportal. (2022). Digital 2022: Global Overview Report. Retrieved from [DataReportal](https://datareportal.com/reports/digital-2022-global-overview-report).
3. Flask. (n.d.). Flask Documentation. Retrieved from [Flask Documentation](https://flask.palletsprojects.com/en/3.0.x/).
4. SQLAlchemy. (n.d.). SQLAlchemy Documentation. Retrieved from [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/20/).
5. Flask-JWT-Extended. (n.d.). Flask-JWT-Extended Documentation. Retrieved from [Flask-JWT-Extended Documentation](https://flask-jwt-extended.readthedocs.io/en/stable/).
6. Marshmallow. (n.d.). Marshmallow Documentation. Retrieved from [Marshmallow Documentation](https://marshmallow.readthedocs.io/en/stable/).
7. PostgreSQL. (n.d.). PostgreSQL Documentation. Retrieved from [PostgreSQL Documentation](https://www.postgresql.org/docs/).
8. Bcrypt. (n.d.). Bcrypt Documentation. Retrieved from [Bcrypt Documentation](https://pypi.org/project/bcrypt/).
9.  Flask-Bcrypt. (n.d.). Flask-Bcrypt Documentation. Retrieved from [Flask-Bcrypt Documentation](https://flask-bcrypt.readthedocs.io/en/1.0.1/).
10. Flask-SQLAlchemy. (n.d.). Flask-SQLAlchemy Documentation. Retrieved from [Flask-SQLAlchemy Documentation](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/).
11. Atlassian. (n.d.). Kanban Board Overview. Retrieved from [Kanban Board Overview](https://www.atlassian.com/agile/kanban).
12. RESTful API. (n.d.). REST API Best Practices. Retrieved from [REST API Best Practices](https://restfulapi.net/).
13. Insomnia. (n.d.). Insomnia Documentation. Retrieved from [Insomnia Documentation](https://docs.insomnia.rest/).
14. Google Cloud. (n.d.). API Design Guide. Retrieved from [Google Cloud API Design Guide](https://cloud.google.com/apis/design).
15. Grinberg, M. (n.d.). Flasky. Retrieved from [Flasky](https://github.com/miguelgrinberg/flasky).
16. Python.org. (n.d.). PEP 8 – Style Guide for Python Code. Retrieved from PEP 8 – Style Guide for Python Code(https://peps.python.org/pep-0008/)
