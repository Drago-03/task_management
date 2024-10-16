# Task Management System API

## Overview

This project is a RESTful API for a Task Management System built with Flask. It provides endpoints for user authentication, task management, and project organization. The API uses JWT for authentication and SQLAlchemy for database operations.

## Features

- User registration and login
- JWT-based authentication
- CRUD operations for tasks
- CRUD operations for projects
- Association of tasks with users and projects

## Technologies Used

- Python 3.8+
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-JWT-Extended
- Flask-RESTful
- Marshmallow

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/task-management-system.git
   cd task-management-system
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

5. Create a `.env` file in the project root and add the following:
   ```
   FLASK_APP=app.py
   FLASK_ENV=development
   SECRET_KEY=your_secret_key
   JWT_SECRET_KEY=your_jwt_secret_key
   ```

6. Initialize the database:
   ```
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

## Running the Application

To run the application, use the following command:

```
flask run
```

The API will be available at `http://127.0.0.1:5000/`.

## API Endpoints

### Authentication

- POST /register - Register a new user
- POST /login - Login and receive an access token

### Tasks

- GET /tasks - Retrieve all tasks
- POST /tasks - Create a new task
- GET /tasks/<task_id> - Retrieve a specific task
- PUT /tasks/<task_id> - Update a specific task
- DELETE /tasks/<task_id> - Delete a specific task

### Projects

- GET /projects - Retrieve all projects
- POST /projects - Create a new project
- GET /projects/<project_id> - Retrieve a specific project
- PUT /projects/<project_id> - Update a specific project
- DELETE /projects/<project_id> - Delete a specific project

## Usage

1. Register a new user:
   ```
   curl -X POST -H "Content-Type: application/json" -d '{"username":"testuser","email":"test@example.com","password":"testpassword"}' http://127.0.0.1:5000/register
   ```

2. Login to receive an access token:
   ```
   curl -X POST -H "Content-Type: application/json" -d '{"username":"testuser","password":"testpassword"}' http://127.0.0.1:5000/login
   ```

3. Use the access token to make authenticated requests:
   ```
   curl -X GET -H "Authorization: Bearer <your_access_token>" http://127.0.0.1:5000/tasks
   ```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
