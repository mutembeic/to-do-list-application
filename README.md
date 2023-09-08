# Todo List CLI Application

![Todo List CLI](todo_list_cli.png)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Dependencies](#dependencies)
- [Installation](#installation)
  - [Clone the Repository](#clone-the-repository)
  - [Install Dependencies](#install-dependencies)
  - [Configure the Database](#configure-the-database)
- [Usage](#usage)
- [Commands](#commands)
  - [1. Add a New User](#1-add-a-new-user)
  - [2. Delete a User](#2-delete-a-user)
  - [3. List All Tasks](#3-list-all-tasks)
  - [4. Delete a Task](#4-delete-a-task)
  - [5. Add a New Task](#5-add-a-new-task)
  - [6. List All Users](#6-list-all-users)
  - [7. Exit](#7-exit)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Todo List CLI Application is a simple command-line tool developed in Python that allows you to manage tasks and users. It's a flexible and easy-to-use system that can help you keep track of your tasks, prioritize them, and organize them by category.

This application is designed for individuals or teams who prefer a text-based interface for managing their to-do lists. It offers essential features like adding and deleting tasks, creating users, and listing tasks for a specific user.

## Features

### User Management:

- Add new users with unique usernames and email addresses.
- Delete users by specifying their usernames.

### Task Management:

- Create tasks with various details:
  - Name (required)
  - Description (optional)
  - Due date (optional, format: YYYY-MM-DD HH:MM:SS)
  - Priority (optional)
- Delete tasks by their unique IDs.
- List all tasks for a specific user.

### Category Assignment:

- Optionally categorize tasks by associating them with a category.

## Dependencies

This project relies on the following Python packages:

- [SQLAlchemy](https://www.sqlalchemy.org/): SQLAlchemy is used for database management.
- [Click](https://click.palletsprojects.com/): Click is used for creating command-line interfaces.

You can install these dependencies by running the following command:

```bash
pip install -r requirements.txt
```

## Installation

Follow these steps to set up and run the Todo List CLI Application:

### Clone the Repository

Clone this repository to your local machine using Git:

```bash
git clone https://github.com/yourusername/todo-list-cli.git
```

### Install Dependencies

Navigate to the project directory:

```bash
cd todo-list-cli
```

Install the required Python packages mentioned in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### Configure the Database

The application uses a database to store user and task information. By default, it's configured to use SQLite as the database. You can customize the database URL by editing the `config.py` file:

```python
DATABASE_URL = "sqlite:///my_todo_app.db"
```

Replace the URL with your preferred database connection string.

Next, create the initial database and tables using Alembic (a SQLAlchemy migration tool):

```bash
alembic upgrade head
```

## Usage

To run the application, execute the following command in your terminal:

```bash
python run.py
```

This will start the interactive command-line interface (CLI) for managing your todo list.

## Commands

The CLI provides the following commands:

### 1. Add a New User

This command allows you to add a new user to the database. You'll be prompted to enter a username and email.

### 2. Delete a User

Use this command to delete a user by specifying their username.

### 3. List All Tasks

Lists all tasks for a specific user. You'll be prompted to enter the username.

### 4. Delete a Task

Allows you to delete a task by its unique ID.

### 5. Add a New Task

Create a new task and associate it with a user. You'll be prompted to enter various details like task name, description, due date, priority, and an optional category.

### 6. List All Users

Lists all users in the database.

### 7. Exit

Exits the application.

## Contributing

Contributions to this project are welcome! If you'd like to enhance this project, fix any issues, or add new features, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.
```