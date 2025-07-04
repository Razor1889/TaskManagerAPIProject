```markdown
# Task Manager API

[![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg?logo=python)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A secure, fully-featured RESTful API built with FastAPI and SQLAlchemy. It allows users to register, log in, and manage personal tasks with proper authentication and authorization using JSON Web Tokens (JWT).

---

## Features

- User registration and login with hashed passwords
- JWT authentication for secure access
- Full CRUD operations for tasks
- Per-user task access (authorization)
- Built-in interactive API docs via Swagger (`/docs`)

---

## Tech Stack

- **Python 3.11+**
- **FastAPI**
- **SQLAlchemy**
- **SQLite** (easily swappable for PostgreSQL or MySQL)
- **JWT** via `python-jose`
- **Password hashing** via `passlib`

---

## Directory Structure

```

TaskManagerAPIProject/
├── app/
│   ├── auth.py              # JWT creation and password hashing
│   ├── crud.py              # DB operations (CRUD)
│   ├── database.py          # DB engine/session config
│   ├── dependencies.py      # JWT token decoding
│   ├── main.py              # FastAPI app initialization
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic models
│   └── routers/
│       ├── task.py          # Task endpoints
│       └── user.py          # User endpoints (register/login)
└── requirements.txt

````

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Razor1889/task-manager-api.git
cd task-manager-api
````

### 2. Set Up the Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the API Server

```bash
uvicorn app.main:app --reload
```

Then go to: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## API Endpoints

### Auth

| Method | Endpoint          | Description         |
| ------ | ----------------- | ------------------- |
| POST   | `/users/register` | Register a new user |
| POST   | `/users/login`    | Log in and get JWT  |

### Tasks (JWT Required)

| Method | Endpoint      | Description         |
| ------ | ------------- | ------------------- |
| GET    | `/tasks/`     | List all your tasks |
| POST   | `/tasks/`     | Create a new task   |
| GET    | `/tasks/{id}` | Get a task by ID    |
| PUT    | `/tasks/{id}` | Update a task       |
| DELETE | `/tasks/{id}` | Delete a task       |

---

## Authentication

To access protected routes, use the JWT token returned by `/users/login`. Include it in the `Authorization` header like this:

```
Authorization: Bearer <your_token_here>
```

You can also authorize inside the `/docs` UI by clicking the **Authorize** button.

---

## License

This project is licensed under the [MIT License](LICENSE).


