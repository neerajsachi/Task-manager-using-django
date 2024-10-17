# Task Manager API

## Setup and Run

### Requirements

- Python 
- Django
- Django Rest Framework
- MySQL

### Installation

1. Setup project using django-admin startproject task_manager

2. Setup app using django-admin startapp tasks

3. Install mysqlclient 

4. Install Django Rest Framework

5. Install django-filter

6. Set up the MySQL database in `task_manager/settings.py`.

7. Add Rest framework, tasks, and django_filter to installed apps in `task_manager/settings.py`

8. Add page size in Rest framework configuration

6. Run migrations:
    python manage.py migration

7. Run the server:
    python manage.py runserver

### API Endpoints

- `GET /api/tasks/` - List all tasks
- `POST /api/tasks/` - Create a new task
- `GET /api/tasks/{id}/` - Retrieve a specific task
- `PUT/PATCH /api/tasks/{id}/` - Update a task
- `DELETE /api/tasks/{id}/` - Delete a task
