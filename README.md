# Task Management API

This project provides a task management API that allows users to create, retrieve, update, and delete tasks. It supports JWT-based authentication, filtering, searching, and pagination.

## Features
- JWT Authentication
- Task creation, retrieval, updating, and deletion
- Task assignment to users
- Searching and filtering tasks
- Pagination for task listing

## Setup Instructions
1.Clone Repository
 - git clone https://github.com/your-username/task-management-api.git
 - navigate to the project directory
2.Create Virtual Environment
 - python -m venv venv
 - activate - venv\Scripts\activate
3.Install Dependencies
 - pip install -r requirements.txt
4.Database Setup
 - CREATE DATABASE task_management_db;
 - Update the DATABASES section in your settings.py file with your database credentials.
5.Run Migrations
 - python manage.py migrate
6.Create Superuser
 - python manage.py createsuperuser

Run Server
 - python manage.py runserver

### Prerequisites
- Python 3
- PostgreSQL (or other supported databases)

Base URL - http://localhost:8000/api/
Authentication  - JWT
obtain a token by sending a post request to /api/auth/login - with usernamea and password

Endpoints
- Register a User: POST /api/register/
- Create a Task: POST /api/tasks/
- List Tasks: GET /api/tasks/
- Retrieve a Task: GET /api/tasks/{task_id}/
- Update a Task: PUT /api/tasks/{task_id}/
- Delete a Task: DELETE /api/tasks/{task_id}/

Query Parameters
Search: You can search tasks by title or description using ?search=your-query.
Pagination: Use ?page=1 to paginate results.
Ordering: Use ?ordering=due_date to order tasks by a field.

