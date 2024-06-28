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
    - [Final ERD](#final-erd)
    - [References](#references)

### R1: Problem and Solution

Microblogging platforms are immensely popular due to their ability to provide quick and easy content sharing, community building, and user interaction. However, many of these platforms lack certain features that can significantly enhance user experience and content management. Common issues include:

1. Many microblogging platforms do not provide tagging systems that allow users to categorise their posts effectively. This makes content discovery and organisation difficult.
2. Secure and efficient user authentication is crucial, yet some platforms have outdated or insecure methods for managing user accounts and sessions.
3. User interaction through comments is often poorly managed, leading to a cluttered and unorganised user experience.
4. As user bases grow, platforms often struggle with scalability and performance issues due to inefficient database design and lack of sufficient backend infrastructure.

According to a 2021 study by Statista, there were over 3.6 billion social media users worldwide, and this number is expected to increase to nearly 4.41 billion by 2025. The sheer volume of users highlights the need for scalable and efficient microblogging platforms.
A report by DataReportal in 2022 indicated that 54.9% of internet users look for information on brands and products through social networks. This underscores the importance of effective content categorisation and user engagement.

**How MinorNote Addresses the Problem**:

1. **Robust Tagging System**:
   - MinorNote provides a powerful tagging system that allows users to categorise their posts with multiple tags. This enhances content discovery and organisation, making it easier for users to find posts of interest. MinorNote allows each post to be associated with multiple tags. This many-to-many relationship between posts and tags enables users to categorise their posts in multiple ways, making content more accessible and easier to discover. For instance, a user could tag a post with "Technology," "AI," and "Innovation," making it visible under all three categories.

2. **Secure User Authentication**:
   - The API uses JWT (JSON Web Tokens) for secure user authentication, ensuring that user sessions are managed securely and efficiently. This approach to authentication helps prevent unauthorised access and protects user data. The use of JWT for user authentication means that each user session is represented by a token, which includes user information and session validity. This approach not only secures user data but also enhances the scalability of the application by reducing the load on the server to maintain user sessions.

3. **Efficient Comment Management**:
   - MinorNote includes features for managing comments on posts, allowing users to add, edit, and delete comments. This ensures a clean and organised interaction space, enhancing user engagement and satisfaction. MinorNote provides endpoints for creating, reading, updating, and deleting comments on posts. This CRUD functionality ensures that comments can be managed effectively, preventing clutter and enhancing the user experience. Users can engage in meaningful discussions, knowing that their comments can be managed and moderated appropriately.

4. **Scalability and Performance**:
   - Built with Flask and SQLAlchemy, MinorNote is designed for scalability. The database is structured with normalised tables to handle large volumes of data efficiently. PostgreSQL, known for its reliability and performance, is used as the database system. The choice of PostgreSQL as the database ensures that the application can handle large volumes of data while maintaining high performance. PostgreSQL's advanced features, such as full-text search and JSONB support, provide additional capabilities that enhance the functionality of the API.

### R2: Task Allocation and Tracking

**Task Planning and Tracking**

In the MinorNote API project, tasks were planned and tracked using a Kanban board, a visual workflow management tool that provides clarity and structure to the project’s progress. The Kanban board was hosted on Trello, a widely used task management tool.

**Planning Process**:

1. **Initial Setup**:
   - The project started with a brainstorming session to identify all the tasks required to complete the project.
   - Tasks were broken down into smaller, manageable subtasks to ensure every aspect of the project was covered.

2. **Task Categorisation**:
   - Tasks were categorised into different columns on the Kanban board: To Do, In Progress, Review, and Done.
   - Each column represented a stage in the development process, allowing for easy tracking of task progress.

3. **Prioritisation**:
   - Tasks were prioritised based on their importance and urgency.
   - High-priority tasks, such as core features and security implementations, were addressed first to ensure the project's stability and functionality.

**Tracking Process**:

1. **Daily Check-ins**:
   - Daily check-ins were conducted to assess progress, identify roadblocks, and plan next steps.
   - This solo project approach ensured continuous progress and self-accountability.

2. **Kanban Board Updates**:
   - The Kanban board was updated in real-time as tasks moved from one stage to another.
   - Each task card included detailed descriptions and due dates to ensure clear understanding and effective time management.

3. **Review and Adjustments**:
   - Completed tasks were moved to the Review column for self-evaluation.
   - Any necessary changes or improvements were made before tasks were marked as Done.

**Proof of Usage**:
The usage of the Kanban board can be seen throughout the project. Every task, from initial setup, was tracked using Trello. The board provides a comprehensive view of the project’s workflow, showcasing the planning and tracking involved in the development of MinorNote.

You can view the Kanban board used for the project [here](https://trello.com/invite/b/5LMBpS52/ATTIe9d6d662e94ae1cba29b55fc075a77b1711AC91E/minornote).

### R3: Third-Party Services, Packages, and Dependencies

The MinorNote API utilises several third-party services, packages, and dependencies to ensure a robust, secure, and efficient development and runtime environment.

1. **Alembic** (`alembic==1.13.1`)
   - Alembic is a lightweight database migration tool for use with SQLAlchemy. It allows for efficient database schema changes and version control.

2. **bcrypt** (`bcrypt==4.1.3`)
   - Bcrypt is a password hashing function designed for secure password storage. It provides a hashing algorithm that is highly resistant to brute-force attacks.

3. **blinker** (`blinker==1.8.2`)
   - Blinker provides a fast dispatching system for creating signals in Python. It is used for event-driven programming within the Flask application.

4. **click** (`click==8.1.7`)
   - Click is a Python package for creating command-line interfaces (CLI) in a composable way. It is used by Flask for command-line operations.

5. **exceptiongroup** (`exceptiongroup==1.2.1`)
   - ExceptionGroup is a package that helps in handling and managing multiple exceptions in a more structured manner, especially useful for debugging complex applications.

6. **Flask** (`Flask==3.0.3`)
   - Flask is a lightweight WSGI web application framework in Python. It provides the core functionality for building the API, including routing, request handling, and more.

7. **Flask-Bcrypt** (`Flask-Bcrypt==1.0.1`)
   - Flask-Bcrypt is an extension that integrates bcrypt into Flask, providing utilities for password hashing.

8. **Flask-JWT-Extended** (`Flask-JWT-Extended==4.6.0`)
   - Flask-JWT-Extended is an extension for adding JSON Web Token (JWT) authentication to Flask applications. It is used for secure user authentication and session management.

9. **flask-marshmallow** (`flask-marshmallow==1.2.1`)
   - Flask-Marshmallow is an integration layer for Flask and Marshmallow, providing object serialization/deserialization and validation.

10. **Flask-Migrate** (`Flask-Migrate==4.0.7`)
    - Flask-Migrate is an extension that handles SQLAlchemy database migrations for Flask applications using Alembic.

11. **Flask-SQLAlchemy** (`Flask-SQLAlchemy==3.1.1`)
    - Flask-SQLAlchemy is an extension for Flask that adds support for SQLAlchemy, a SQL toolkit and ORM. It provides a high-level API for database interactions.

12. **greenlet** (`greenlet==3.0.3`)
    - Greenlet is a lightweight coroutine library that allows for concurrent execution of code. It is used internally by SQLAlchemy and other packages for asynchronous operations.

13. **iniconfig** (`iniconfig==2.0.0`)
    - Iniconfig is a simple package for reading and writing .ini files. It is often used in configuration management for Python projects.

14. **itsdangerous** (`itsdangerous==2.2.0`)
    - Itsdangerous provides safe data serialization and deserialization. It is used by Flask for securely signing data to ensure integrity.

15. **Jinja2** (`Jinja2==3.1.4`)
    - Jinja2 is a templating engine for Python. It is used by Flask for rendering HTML templates.

16. **Mako** (`Mako==1.3.5`)
    - Mako is another templating engine for Python, providing an alternative to Jinja2 with different syntax and features.

17. **MarkupSafe** (`MarkupSafe==2.1.5`)
    - MarkupSafe is a library for safe handling of HTML and XML in Python. It is used by Jinja2 and other templating engines to escape strings.

18. **marshmallow** (`marshmallow==3.21.3`)
    - Marshmallow is a library for object serialization/deserialization and validation. It simplifies the conversion between complex data types and native Python data types.

19. **marshmallow-sqlalchemy** (`marshmallow-sqlalchemy==1.0.0`)
    - Marshmallow-SQLAlchemy provides integration between Marshmallow and SQLAlchemy, allowing for easy serialization/deserialization of SQLAlchemy models.

20. **packaging** (`packaging==24.1`)
    - Packaging provides utilities for dealing with Python packages and versions, ensuring compatibility and proper dependency management.

21. **pluggy** (`pluggy==1.5.0`)
    - Pluggy is a plugin management framework used internally by various Python tools, including pytest.

22. **psycopg2-binary** (`psycopg2-binary==2.9.9`)
    - Psycopg2 is a PostgreSQL database adapter for Python, allowing for efficient interaction with PostgreSQL databases.

23. **PyJWT** (`PyJWT==2.8.0`)
    - PyJWT is a Python library for encoding and decoding JSON Web Tokens. It is used by Flask-JWT-Extended for JWT handling.

24. **pytest** (`pytest==8.2.2`)
    - Pytest is a testing framework for Python that makes it easy to write simple and scalable test cases.

25. **pytest-flask** (`pytest-flask==1.3.0`)
    - Pytest-Flask is a plugin for pytest that provides utilities for testing Flask applications.

26. **python-dotenv** (`python-dotenv==1.0.1`)
    - Python-dotenv reads key-value pairs from a .env file and can set them as environment variables. It is used for configuration management.

27. **python-env** (`python-env==1.0.0`)
    - Python-env is another package for managing environment variables in Python projects.

28. **SQLAlchemy** (`SQLAlchemy==2.0.30`)
    - SQLAlchemy is a SQL toolkit and Object-Relational Mapping (ORM) library for Python. It provides the core functionality for database interactions in the MinorNote API.

29. **tomli** (`tomli==2.0.1`)
    - Tomli is a TOML parser for Python, used for reading and writing TOML configuration files.

30. **typing_extensions** (`typing_extensions==4.12.2`)
    - Typing Extensions provides backports of new typing features introduced in newer Python versions, ensuring compatibility with older versions.

31. **Werkzeug** (`Werkzeug==3.0.3`)
    - Werkzeug is a comprehensive WSGI web application library. It is used by Flask for request handling and various other utilities.

### R4: Benefits and Drawbacks of PostgreSQL

**Benefits**:

1. **Reliability**:
   - **ACID Compliance**: PostgreSQL is fully ACID (Atomicity, Consistency, Isolation, Durability) compliant. This means that transactions are processed reliably and adhere to all the rules of a relational database, ensuring data integrity.
   - **Data Integrity**: PostgreSQL supports various data integrity constraints, such as primary keys, foreign keys, UNIQUE constraints, and CHECK constraints, which enforce rules on data to maintain accuracy and consistency.

2. **Advanced Features**:
   - **Full-Text Search**: PostgreSQL includes powerful full-text search capabilities, allowing for efficient search operations within text data.
   - **JSONB Support**: PostgreSQL provides advanced support for JSON data types, enabling efficient storage and querying of JSON data. This feature is especially beneficial for applications that require flexible schema or semi-structured data.
   - **Extensibility**: PostgreSQL's architecture allows users to define custom functions, operators, and data types, making it highly extensible. Users can also create extensions that add new functionalities, such as PostGIS for geographic information systems (GIS).

3. **Performance**:
   - **Query Optimization**: PostgreSQL includes a sophisticated query planner and optimizer that enhances the performance of complex queries.
   - **Concurrency**: PostgreSQL's MVCC (Multi-Version Concurrency Control) allows for high levels of concurrent transactions without locking issues, ensuring better performance in multi-user environments.

4. **Scalability**:
   - **Horizontal Scalability**: PostgreSQL supports various replication methods, such as streaming replication and logical replication, enabling horizontal scalability and high availability.
   - **Vertical Scalability**: PostgreSQL can handle large datasets and high transaction loads, making it suitable for applications that require vertical scalability.

5. **Security**:
   - **Robust Access Control**: PostgreSQL provides granular access control mechanisms, including role-based access control (RBAC), ensuring that users have appropriate permissions.
   - **Encryption**: PostgreSQL supports data encryption at various levels, including column-level encryption and SSL/TLS for secure data transmission.

6. **Open Source**:
   - **Cost-Effective**: Being an open-source database system, PostgreSQL is free to use, which significantly reduces the total cost of ownership compared to proprietary databases.
   - **Community Support**: PostgreSQL has a large and active community that contributes to its development and provides extensive support and resources.

**Drawbacks**:

1. **Complexity**:
   - **Steep Learning Curve**: PostgreSQL's extensive feature set and advanced capabilities can make it complex to learn and use, especially for beginners. This steep learning curve may require more time and resources for initial setup and ongoing maintenance.
   - **Configuration and Tuning**: Properly configuring and tuning PostgreSQL for optimal performance can be challenging and requires a deep understanding of its settings and parameters.

2. **Resource Intensive**:
   - **Higher Resource Requirements**: Compared to some other lightweight database systems, PostgreSQL can be more resource-intensive in terms of memory and CPU usage. This may not be ideal for applications with limited resources or for embedded systems.

3. **Hosting and Deployment**:
   - **Shared Hosting Limitations**: PostgreSQL is not as widely available on shared hosting services compared to other databases like MySQL. Users might need to opt for more expensive hosting solutions such as virtual private servers (VPS) or cloud hosting.
   - **Complex Deployment**: Deploying PostgreSQL in a highly available and scalable setup, such as setting up replication and failover, can be complex and may require advanced knowledge and experience.

4. **Tooling and Ecosystem**:
   - **Tool Compatibility**: While PostgreSQL has excellent tools and extensions, some tools and applications are more optimized or only available for other databases, particularly MySQL and Oracle. This can limit the choices of third-party tools and integrations.

PostgreSQL is a powerful, reliable, and feature-rich database system that offers numerous benefits, including advanced features, strong performance, scalability, and robust security. However, its complexity and resource requirements can be potential drawbacks for some applications. By carefully considering these factors, developers can leverage PostgreSQL's strengths while mitigating its challenges to build robust and efficient applications.

### R5: Features and Functionalities of SQLAlchemy

SQLAlchemy is a powerful and flexible ORM system for Python that provides tools to work with databases in an object-oriented way. It abstracts the database interactions into Python objects, making database operations easier and more intuitive.

**1. ORM and Declarative Mapping**:

SQLAlchemy's ORM allows you to define Python classes that are mapped to database tables. The `declarative_base` function provides a base class for declarative class definitions.

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
```

**2. Schema Definition:**

SQLAlchemy allows you to define the schema of your database using Python classes. You can specify data types, constraints, and relationships directly within the class definition.

```py
class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))

    user = relationship('User', back_populates='posts')

User.posts = relationship('Post', order_by=Post.id, back_populates='user')
```

**3. Query Construction and Execution:**

SQLAlchemy provides a powerful query API that allows you to construct and execute complex queries in an intuitive way. The ORM automatically translates these queries into SQL.

```py
# Querying the database
posts = session.query(Post).filter(Post.title.like('%Flask%')).all()
for post in posts:
    print(post.title)
```

**4. Relationship Handling:**

SQLAlchemy supports defining and managing relationships between tables, such as one-to-many, many-to-many, and one-to-one relationships. This is done using the `relationship` and `ForeignKey` constructs.

```py
class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
    post_id = Column(Integer, ForeignKey('posts.id', ondelete='CASCADE'))

    user = relationship('User')
    post = relationship('Post', back_populates='comments')

Post.comments = relationship('Comment', order_by=Comment.id, back_populates='post')
```

**5. Transaction Management:**

SQLAlchemy handles database transactions seamlessly. You can commit, rollback, and manage transactions using the session object.

```py
try:
    new_comment = Comment(content='Great post!', user_id=1, post_id=1)
    session.add(new_comment)
    session.commit()
except:
    session.rollback()
    raise
```

**6. Migrations:**

While not a part of SQLAlchemy itself, it integrates well with Alembic, a lightweight database migration tool. Alembic allows you to manage database schema changes over time.

```bash
# Initialize Alembic
alembic init alembic

# Create a migration script
alembic revision --autogenerate -m "Add comments table"

# Apply the migration
alembic upgrade head
```

**7. Extensibility and Custom Types:**

SQLAlchemy allows you to define custom data types and extend the functionality of the ORM. This is particularly useful for implementing domain-specific logic.

```py
from sqlalchemy.types import TypeDecorator, CHAR
import uuid

class GUID(TypeDecorator):
    """Platform-independent GUID type."""
    impl = CHAR

    def load_dialect_impl(self, dialect):
        return dialect.type_descriptor(CHAR(32))

    def process_bind_param(self, value, dialect):
        if value is None:
            return value
        elif isinstance(value, uuid.UUID):
            return value.hex
        else:
            return uuid.UUID(value).hex

    def process_result_value(self, value, dialect):
        if value is None:
            return value
        else:
            return uuid.UUID(value)

# Using the custom GUID type
class Example(Base):
    __tablename__ = 'examples'
    id = Column(GUID(), primary_key=True, default=uuid.uuid4)
```

### R6: Entity Relationship Diagram (ERD)

**Entity Relationship Diagram (ERD)**

Below is the Entity Relationship Diagram (ERD) for the MinorNote API project. This ERD illustrates the normalised database schema and the relationships between the entities.

```plaintext
+------------+          +-----------+          +----------+
|   User     |          |   Post    |          |   Tag    |
+------------+          +-----------+          +----------+
| id (PK)    |<-------1 | id (PK)   |  M-----M | id (PK)  |
| username   |          | title     |----------| name     |
| email      |          | content   |          +----------+
| password   |          | user_id (FK)         |  
| first_name |          +-----------+          +----------+
| last_name  |<--------1 |   Comment |  M-----M | post_tags|
+------------+          +-----------+----------+----------+
                       | id (PK)   |          | post_id (FK)|
                       | content   |          | tag_id (FK) |
                       | user_id (FK)         +------------+
                       | post_id (FK)         
                       +-----------+
```

**Legend/Key:**

- PK: Primary Key
- FK: Foreign Key
- 1: One-to-Many relationship
- M: Many-to-Many relationship

**Normalisation Explanation:**

First Normal Form (1NF):

- All attributes contain only atomic (indivisible) values. There are no repeating groups or arrays.
- In the ERD, each table has a primary key, and each field contains only single values.

Second Normal Form (2NF):

- All attributes are fully functionally dependent on the primary key.
- Non-key attributes are not dependent on any subset of a candidate key.
- For example, in the Post table, attributes like title, content, and user_id depend entirely on the primary key id.

Third Normal Form (3NF):

- There are no transitive dependencies; non-key attributes are not dependent on other non-key attributes.
- For example, in the User table, attributes like username, email, password, first_name, and last_name are only dependent on the primary key id.

**Entity Relationships:**

User to Post:

- One-to-Many: One user can create many posts. This relationship is represented by a foreign key user_id in the Post table that references the id in the User table.

Post to Comment:

- One-to-Many: One post can have many comments. This relationship is represented by a foreign key post_id in the Comment table that references the id in the Post table.
- One-to-Many: One user can make many comments. This relationship is represented by a foreign key user_id in the Comment table that references the id in the User table.

Post to Tag:

- Many-to-Many: One post can have many tags, and one tag can be associated with many posts. This relationship is represented by the post_tags association table, which contains foreign keys post_id and tag_id that reference the id in the Post and Tag tables, respectively.

**Comparison to Other Normalisation Levels:**

Unnormalised Form:

- An unnormalised database might have a single table with repeated groups, such as a Posts table containing multiple tags in a single field, separated by commas. This approach leads to data redundancy and anomalies.

First Normal Form (1NF):

- The database design would ensure that each field contains only atomic values. For example, the Tags field in the Posts table would be broken down into individual rows in a PostTags table to avoid repeating groups.

Second Normal Form (2NF):

- The database would remove partial dependencies. For instance, if the Posts table had fields that depended only on part of the composite key (if any), those fields would be moved to a separate table.

Third Normal Form (3NF):

- The database design would eliminate transitive dependencies. For example, if the Posts table had a field like author_email (dependent on user_id), this field would be removed since it introduces a transitive dependency.

### R7: Models and Their Relationships

MinorNote consists of models that represent the entities within the application. These models are interconnected through relationships, which allow for efficient data access and manipulation.

**Models**:

1. **User**:
   - Represents a user in the application.
   - Attributes: `id`, `username`, `email`, `password`, `first_name`, `last_name`, `is_admin`.
   - Relationships: One-to-Many with `Post` and `Comment`.

2. **Post**:
   - Represents a blog post created by a user.
   - Attributes: `id`, `title`, `content`, `user_id`, `date_created`.
   - Relationships: One-to-Many with `Comment`, Many-to-Many with `Tag`.

3. **Comment**:
   - Represents a comment on a post.
   - Attributes: `id`, `content`, `user_id`, `post_id`, `date_created`.
   - Relationships: Many-to-One with `User` and `Post`.

4. **Tag**:
   - Represents a tag associated with posts.
   - Attributes: `id`, `name`.
   - Relationships: Many-to-Many with `Post`.

5. **PostTags**:
   - Represents the many-to-many relationship between posts and tags.
   - Attributes: `post_id`, `tag_id`.

**Relationships**:

1. **User to Post**:
   - One user can create multiple posts.
   - This is represented by the `user_id` foreign key in the `Post` model.

     ```python
     class Post(Base):
         __tablename__ = 'posts'
         id = Column(Integer, primary_key=True)
         title = Column(String, nullable=False)
         content = Column(String)
         user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
         date_created = Column(Date)

         user = relationship('User', back_populates='posts')

     User.posts = relationship('Post', order_by=Post.id, back_populates='user')
     ```

2. **Post to Comment**:
   - One post can have multiple comments.
   - This is represented by the `post_id` foreign key in the `Comment` model.

     ```python
     class Comment(Base):
         __tablename__ = 'comments'
         id = Column(Integer, primary_key=True)
         content = Column(String, nullable=False)
         user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
         post_id = Column(Integer, ForeignKey('posts.id', ondelete='CASCADE'))
         date_created = Column(Date)

         user = relationship('User')
         post = relationship('Post', back_populates='comments')

     Post.comments = relationship('Comment', order_by=Comment.id, back_populates='post')
     ```

3. **Post to Tag**:
   - One post can have multiple tags, and one tag can be associated with multiple posts.
   - This is represented by the `post_tags` association table.

     ```python
     post_tags = Table(
         'post_tags',
         Base.metadata,
         Column('post_id', Integer, ForeignKey('posts.id', ondelete='CASCADE'), primary_key=True),
         Column('tag_id', Integer, ForeignKey('tags.id', ondelete='CASCADE'), primary_key=True)
     )

     class Tag(Base):
         __tablename__ = 'tags'
         id = Column(Integer, primary_key=True)
         name = Column(String, unique=True, nullable=False)

         posts = relationship('Post', secondary=post_tags, back_populates='tags')

     Post.tags = relationship('Tag', secondary=post_tags, back_populates='posts')
     ```

4. **User to Comment**:
   - One user can make multiple comments.
   - This is represented by the `user_id` foreign key in the `Comment` model.

     ```python
     class Comment(Base):
         __tablename__ = 'comments'
         id = Column(Integer, primary_key=True)
         content = Column(String, nullable=False)
         user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
         post_id = Column(Integer, ForeignKey('posts.id', ondelete='CASCADE'))
         date_created = Column(Date)

         user = relationship('User')
         post = relationship('Post', back_populates='comments')

     User.comments = relationship('Comment', order_by=Comment.id, back_populates='user')
     ```

**Queries Using Relationships**:

1. **Get all posts by a specific user**:
   - This query retrieves all posts created by a specific user.

     ```python
     user_id = 1
     user_posts = session.query(Post).filter(Post.user_id == user_id).all()
     ```

2. **Get all comments on a specific post**:
   - This query retrieves all comments associated with a specific post.

     ```python
     post_id = 1
     post_comments = session.query(Comment).filter(Comment.post_id == post_id).all()
     ```

3. **Get all posts with a specific tag**:
   - This query retrieves all posts that have a specific tag.

     ```python
     tag_id = 1
     posts_with_tag = session.query(Post).join(post_tags).filter(post_tags.c.tag_id == tag_id).all()
     ```

4. **Get all comments made by a specific user**:
   - This query retrieves all comments made by a specific user.

     ```python
     user_id = 1
     user_comments = session.query(Comment).filter(Comment.user_id == user_id).all()
     ```

The MinorNote API project models are designed with clear relationships that facilitate efficient data access and manipulation. These relationships, such as one-to-many between `User` and `Post`, one-to-many between `Post` and `Comment`, and many-to-many between `Post` and `Tag`, allow for comprehensive querying capabilities. The provided code examples demonstrate how these relationships can be utilised to retrieve related data, ensuring the integrity and consistency of the application's data.

### R8: API Endpoints

#### Users

1. **Register User**
   - **HTTP Verb**: POST
   - **Route Path**: `/users/register`
   - **Required Body Data**:

     ```json
     {
       "username": "string",
       "email": "string",
       "password": "string",
       "first_name": "string",
       "last_name": "string"
     }
     ```

   - **Success Response** (HTTP 201):

     ```json
     {
       "id": 1,
       "username": "string",
       "email": "string",
       "first_name": "string",
       "last_name": "string",
       "is_admin": false
     }
     ```

   - **Failure Response** (HTTP 400):

     ```json
     {
       "error": "User already exists"
     }
     ```

2. **Login User**
   - **HTTP Verb**: POST
   - **Route Path**: `/users/login`
   - **Required Body Data**:

     ```json
     {
       "email": "string",
       "password": "string"
     }
     ```

   - **Success Response** (HTTP 200):

     ```json
     {
       "token": "jwt_token"
     }
     ```

   - **Failure Response** (HTTP 401):

     ```json
     {
       "error": "Invalid email or password"
     }
     ```

3. **Get All Users**
   - **HTTP Verb**: GET
   - **Route Path**: `/users/`
   - **Required Header**:
  
     ```txt
     Authorization: Bearer <token>
     ```

   - **Success Response** (HTTP 200):

     ```json
     [
       {
         "id": 1,
         "username": "string",
         "email": "string",
         "first_name": "string",
         "last_name": "string",
         "is_admin": false
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

4. **Get One User**
   - **HTTP Verb**: GET
   - **Route Path**: `/users/<int:id>`
   - **Required Header**:

     ```txt
     Authorization: Bearer <token>
     ```

   - **Success Response** (HTTP 200):

     ```json
     {
       "id": 1,
       "username": "string",
       "email": "string",
       "first_name": "string",
       "last_name": "string",
       "is_admin": false
     }
     ```

   - **Failure Response** (HTTP 404):

     ```json
     {
       "error": "User not found"
     }
     ```

5. **Update User**
   - **HTTP Verb**: PUT/PATCH
   - **Route Path**: `/users/<int:id>`
   - **Required Header**:

     ```txt
     Authorization: Bearer <token>
     ```

   - **Required Body Data**:

     ```json
     {
       "username": "string",
       "email": "string",
       "password": "string",
       "first_name": "string",
       "last_name": "string",
       "is_admin": false
     }
     ```

   - **Success Response** (HTTP 200):

     ```json
     {
       "id": 1,
       "username": "string",
       "email": "string",
       "first_name": "string",
       "last_name": "string",
       "is_admin": false
     }
     ```

   - **Failure Response** (HTTP 403):

     ```json
     {
       "error": "Unauthorized"
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

### Final ERD

Can be found [here](docs/minornote_erd.pdf)

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
