# API Endpoints

## Users

- **Register a new user**
  - **URL:** `/register`
  - **Method:** `POST`
  - **Request Body:**

    ```json
    {
      "username": "string",
      "email": "string",
      "password": "string"
    }
    ```

  - **Response:**
    - **201 Created**

      ```json
      {
        "message": "User registered successfully"
      }
      ```

    - **400 Bad Request**

      ```json
      {
        "message": "Validation error message"
      }
      ```

- **User login**
  - **URL:** `/login`
  - **Method:** `POST`
  - **Request Body:**

    ```json
    {
      "username": "string",
      "password": "string"
    }
    ```

  - **Response:**
    - **200 OK**

      ```json
      {
        "access_token": "jwt_token"
      }
      ```

    - **401 Unauthorized**

      ```json
      {
        "message": "Invalid credentials"
      }
      ```

- **Retrieve All Users**
  - **URL:** `/admin/users`
  - **Method:** `GET`
  - **Description:** Retrieve a list of all users.
  - **Request Headers:**
    - `Authorization: Bearer jwt_token`
  - **Response:**
    - **200 OK**

      ```json
      [
        {
          "id": "integer",
          "username": "string",
          "email": "string",
          "created_at": "datetime"
        }
      ]
      ```

    - **401 Unauthorized**

      ```json
      {
        "message": "Unauthorized access"
      }
      ```

- **Retrieve a Specific User by ID**
  - **URL:** `/admin/users/{id}`
  - **Method:** `GET`
  - **Description:** Retrieve details of a specific user by ID.
  - **Request Headers:**
    - `Authorization: Bearer jwt_token`
  - **Response:**
    - **200 OK**

      ```json
      {
        "id": "integer",
        "username": "string",
        "email": "string",
        "created_at": "datetime"
      }
      ```

    - **401 Unauthorized**

      ```json
      {
        "message": "Unauthorized access"
      }
      ```

    - **404 Not Found**

      ```json
      {
        "message": "User not found"
      }
      ```

- **Delete a User by ID**
  - **URL:** `/admin/users/{id}`
  - **Method:** `DELETE`
  - **Description:** Delete a specific user by ID.
  - **Request Headers:**
    - `Authorization: Bearer jwt_token`
  - **Response:**
    - **204 No Content**
    - **401 Unauthorized**

      ```json
      {
        "message": "Unauthorized access"
      }
      ```

    - **404 Not Found**

      ```json
      {
        "message": "User not found"
      }
      ```

## Posts

- **Create a new blog post**
  - **URL:** `/posts`
  - **Method:** `POST`
  - **Request Headers:**
    - `Authorization: Bearer jwt_token`
  - **Request Body:**

    ```json
    {
      "title": "string",
      "content": "string"
    }
    ```

  - **Response:**
    - **201 Created**

      ```json
      {
        "id": "integer",
        "title": "string",
        "content": "string",
        "user_id": "integer",
        "created_at": "datetime"
      }
      ```

    - **400 Bad Request**

      ```json
      {
        "message": "Validation error message"
      }
      ```

- **Retrieve a list of blog posts**
  - **URL:** `/posts`
  - **Method:** `GET`
  - **Response:**
    - **200 OK**

      ```json
      [
        {
          "id": "integer",
          "title": "string",
          "content": "string",
          "user_id": "integer",
          "created_at": "datetime"
        }
      ]
      ```

- **Retrieve a specific blog post by ID**
  - **URL:** `/posts/{id}`
  - **Method:** `GET`
  - **Response:**
    - **200 OK**

      ```json
      {
        "id": "integer",
        "title": "string",
        "content": "string",
        "user_id": "integer",
        "created_at": "datetime"
      }
      ```

    - **404 Not Found**

      ```json
      {
        "message": "Resource not found"
      }
      ```

- **Update a specific blog post by ID**
  - **URL:** `/posts/{id}`
  - **Method:** `PUT`
  - **Request Headers:**
    - `Authorization: Bearer jwt_token`
  - **Request Body:**

    ```json
    {
      "title": "string",
      "content": "string"
    }
    ```

  - **Response:**
    - **200 OK**

      ```json
      {
        "id": "integer",
        "title": "string",
        "content": "string",
        "user_id": "integer",
        "created_at": "datetime"
      }
      ```

    - **400 Bad Request**

      ```json
      {
        "message": "Validation error message"
      }
      ```

    - **404 Not Found**

      ```json
      {
        "message": "Resource not found"
      }
      ```

- **Delete a specific blog post by ID**
  - **URL:** `/posts/{id}`
  - **Method:** `DELETE`
  - **Request Headers:**
    - `Authorization: Bearer jwt_token`
  - **Response:**
    - **204 No Content**
    - **404 Not Found**

      ```json
      {
        "message": "Resource not found"
      }
      ```

## Comments

- **Add a comment to a post**
  - **URL:** `/posts/{id}/comments`
  - **Method:** `POST`
  - **Request Headers:**
    - `Authorization: Bearer jwt_token`
  - **Request Body:**

    ```json
    {
      "content": "string"
    }
    ```

  - **Response:**
    - **201 Created**

      ```json
      {
        "id": "integer",
        "content": "string",
        "user_id": "integer",
        "post_id": "integer",
        "created_at": "datetime"
      }
      ```

    - **400 Bad Request**

      ```json
      {
        "message": "Validation error message"
      }
      ```

    - **404 Not Found**

      ```json
      {
        "message": "Post not found"
      }
      ```

## Tags

- **Retrieve posts by tag**
  - **URL:** `/tags/{tag}/posts`
  - **Method:** `GET`
  - **Response:**
    - **200 OK**

      ```json
      [
        {
          "id": "integer",
          "title": "string",
          "content": "string",
          "user_id": "integer",
          "created_at": "datetime"
        }
      ]
      ```

    - **404 Not Found**

      ```json
      {
        "message": "Tag not found"
      }
      ```

## Error Handling

- **404 Not Found**
  - **Response:**
    - **404 Not Found**

      ```json
      {
        "message": "Resource not found"
      }
      ```

- **400 Bad Request**
  - **Response:**
    - **400 Bad Request**

      ```json
      {
        "message": "Bad request"
      }
      ```

- **500 Internal Server Error**
  - **Response:**
    - **500 Internal Server Error**

      ```json
      {
        "message": "An internal error occurred"
      }
      ```
