# MinorNote API Documentation

Welcome to the MinorNote API documentation. This guide will help you understand how to interact with the API endpoints, including creating, reading, updating, and deleting users, blog posts, comments, and tags.

## Introduction

MinorNote is a microblogging platform API that provides functionality for user authentication, blog post management, commenting, and tagging. It is built using Flask and SQLAlchemy, and it aims to offer a secure and scalable solution for microblogging needs.

## Table of Contents

- [MinorNote API Documentation](#minornote-api-documentation)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
    - [Base URL/port](#base-urlport)
    - [Required Headers](#required-headers)
  - [Authentication](#authentication)
    - [Register](#register)
    - [Login](#login)
  - [Users](#users)
    - [Get All Users (Admin Only)](#get-all-users-admin-only)
    - [Get User by ID](#get-user-by-id)
    - [Update User](#update-user)
    - [Delete User](#delete-user)
  - [Posts](#posts)
    - [Get All Posts](#get-all-posts)
    - [Get Post by ID](#get-post-by-id)
    - [Create Post](#create-post)
    - [Update Post](#update-post)
    - [Delete Post](#delete-post)
  - [Comments](#comments)
    - [Get Comments for a Post](#get-comments-for-a-post)
    - [Create Comment](#create-comment)
    - [Update Comment](#update-comment)
    - [Delete Comment](#delete-comment)
  - [Tags](#tags)
    - [Get Posts by Tag](#get-posts-by-tag)
    - [Create Tag](#create-tag)
    - [Get All Tags](#get-all-tags)
    - [Update Tag](#update-tag)
    - [Delete Tag](#delete-tag)
  - [Error Handling](#error-handling)
  - [Environment Setup](#environment-setup)
    - [Required Environment Variables](#required-environment-variables)
    - [Installing Dependencies](#installing-dependencies)
    - [Running the Application](#running-the-application)
    - [Populating the Database with Sample Data](#populating-the-database-with-sample-data)

## Getting Started

### Base URL/port

All API endpoints are relative to the base URL:

[http://127.0.0.1:5000](http://127.0.0.1:5000)

### Required Headers

Ensure you include the following headers in your requests:

- `Content-Type: application/json`
- `Authorization: Bearer <your_jwt_token>` (for authenticated routes)

## Authentication

### Register

**Endpoint**: `/users/register`

**Method**: `POST`

**Body**:

```json
{
  "username": "yourusername",
  "email": "youremail@example.com",
  "password": "yourpassword",
  "first_name": "YourFirstName",
  "last_name": "YourLastName"
}
```

**Response**:

- `201 Created` on success
- `400 Bad Request` on validation failure

### Login

**Endpoint**: `/users/login`

**Method**: `POST`

**Body**:

```json
{
  "email": "youremail@example.com",
  "password": "yourpassword"
}
```

**Response**:

- `200 OK` on success with JWT token
- `401 Unauthorized` on failure

## Users

### Get All Users (Admin Only)

**Endpoint**: `/users`

**Method**: `GET`

**Response**:

- `200 OK` with user list
- `403 Forbidden` if not an admin

### Get User by ID

**Endpoint**: `/users/<id>`

**Method**: `GET`

**Response**:

- `200 OK` with user data
- `404 Not Found` if user does not exist

### Update User

**Endpoint**: `/users/<id>`

**Method**: `PUT` or `PATCH`

**Body**:

```json
{
  "username": "newusername",
  "email": "newemail@example.com",
  "password": "newpassword",
  "first_name": "NewFirstName",
  "last_name": "NewLastName"
}
```

**Response**:

- `200 OK` on success
- `403 Forbidden` if not the owner
- `404 Not Found` if user does not exist

### Delete User

**Endpoint**: `/users/<id>`

**Method**: `DELETE`

**Response**:

- `204 No Content` on success
- `403 Forbidden` if not the owner or admin
- `404 Not Found` if user does not exist

## Posts

### Get All Posts

**Endpoint**: `/posts`

**Method**: `GET`

**Response**:

- `200 OK` with post list

### Get Post by ID

**Endpoint**: `/posts/<id>`

**Method**: `GET`

**Response**:

- `200 OK` with post data
- `404 Not Found` if post does not exist

### Create Post

**Endpoint**: `/posts`

**Method**: `POST`

**Body**:

```json
{
  "title": "Post Title",
  "content": "Post Content"
}
```

**Response**:

- `201 Created` on success
- `400 Bad Request` on validation failure

### Update Post

**Endpoint**: `/posts/<id>`

**Method**: `PUT` or `PATCH`

**Body**:

```json
{
  "title": "Updated Title",
  "content": "Updated Content"
}
```

**Response**:

- `200 OK` on success
- `403 Forbidden` if not the owner or admin
- `404 Not Found` if post does not exist

### Delete Post

**Endpoint**: `/posts/<id>`

**Method**: `DELETE`

**Response**:

- `204 No Content` on success
- `403 Forbidden` if not the owner or admin
- `404 Not Found` if post does not exist

## Comments

### Get Comments for a Post

**Endpoint**: `/posts/<post_id>/comments`

**Method**: `GET`

**Response**:

- `200 OK` with comment list
- `404 Not Found` if post does not exist

### Create Comment

**Endpoint**: `/posts/<post_id>/comments`

**Method**: `POST`

**Body**:

```json
{
  "content": "Comment Content"
}
```

**Response**:

- `201 Created` on success
- `400 Bad Request` on validation failure

### Update Comment

**Endpoint**: `/posts/<post_id>/comments/<comment_id>`

**Method**: `PUT` or `PATCH`

**Body**:

```json
{
  "content": "Updated Comment Content"
}
```

**Response**:

- `200 OK` on success
- `403 Forbidden` if not the owner or admin
- `404 Not Found` if comment does not exist

### Delete Comment

**Endpoint**: `/posts/<post_id>/comments/<comment_id>`

**Method**: `DELETE`

**Response**:

- `204 No Content` on success
- `403 Forbidden` if not the owner or admin
- `404 Not Found` if comment does not exist

## Tags

### Get Posts by Tag

**Endpoint**: `/tags/<int:tag_id>/posts`

**Method**: `GET`

**Response**:

- `200 OK` with posts associated with the tag
- `404 Not Found` if tag does not exist

### Create Tag

**Endpoint**: `/tags`

**Method**: `POST`

**Body**:

```json
{
  "name": "Tag Name"
}
```

**Response**:

- `201 Created` on success
- `400 Bad Request` on validation failure

### Get All Tags

**Endpoint**: `/tags`

**Method**: `GET`

**Response**:

- `200 OK` with tag list

### Update Tag

**Endpoint**: `/tags/<int:tag_id>`

**Method**: `PUT` or `PATCH`

**Body**:

```json
{
  "name": "Updated Tag Name"
}
```

**Response**:

- `200 OK` on success
- `403 Forbidden` if not an admin
- `404 Not Found` if tag does not exist

### Delete Tag

**Endpoint**: `/tags/<int:tag_id>`

**Method**: `DELETE`

**Response**:

- `204 No Content` on success
- `403 Forbidden` if not an admin
- `404 Not Found` if tag does not exist

## Error Handling

- `400 Bad Request`: The request was invalid or cannot be otherwise served. The exact error should be explained in the error payload.
- `401 Unauthorized`: Authentication is required and has failed or has not yet been provided.
- `403 Forbidden`: The request is valid, but the user does not have the necessary permissions for the resource.
- `404 Not Found`: The requested resource could not be found.
- `500 Internal Server Error`: An error occurred on the server.

## Environment Setup

### Required Environment Variables

- `JWT_KEY`: The secret key used for JWT token signing.
- `SQLALCHEMY_KEY`: The URI for the SQLAlchemy database connection.

### Installing Dependencies

```sh
pip install -r src/requirements.txt
```

### Running the Application

```sh
flask run
```

### Populating the Database with Sample Data

```sh
flask db create
```
