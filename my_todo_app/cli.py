import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base, User, Task, Category  # Replace 'your_models_file' with the actual filename where your models are defined
from datetime import datetime
from .config import DATABASE_URL

# Configure the database connection
DATABASE_URL = "sqlite:///my_todo_app.db"  # Replace with your database URL
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def print_menu():
    """Print the menu with options."""
    print("Menu:")
    print("1. Add a new user")
    print("2. Delete a user")
    print("3. List all tasks")
    print("4. Delete a task")
    print("5. Add a new task")
    print("6. List all users")
    print("7. Exit")

 
def cli():
    """Todo List App"""
    while True:
        print_menu()
        choice = input("Select an option (1-6): ")

        if choice == '1':
            username = input("Enter username: ")
            email = input("Enter email: ")
            add_user(username, email)
        elif choice == '2':
            username = input("Enter username to delete: ")
            delete_user(username)
        elif choice == '3':
            list_tasks()
        elif choice == '4':
            task_id = input("Enter task ID to delete: ")
            delete_task(task_id)
        elif choice == '5':
            user_id = input("Enter user ID for the new task: ")
            name = input("Enter task name: ")
            description = input("Enter task description (optional): ")
            due_date = input("Enter due date (optional, YYYY-MM-DD HH:MM:SS): ")
            priority = input("Enter task priority (optional): ")
            category_id = input("Enter category ID (optional): ")
            add_task(user_id, name, description, due_date, priority, category_id)
        elif choice == '6':
            list_users()
        elif choice == '7':
            print("Exiting Todo List App. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1-7).")


 
@click.argument('username')
@click.argument('email')
def add_user(username, email):
    """Add a new user to the database."""
    user = User(username=username, email=email)
    session.add(user)
    session.commit()
    print(f"User '{username}' added successfully!")

 
@click.argument('username')
def delete_user(username):
    """Delete a user from the database."""
    user = session.query(User).filter_by(username=username).first()
    if user:
        session.delete(user)
        session.commit()
        print(f"User '{username}' deleted successfully!")
    else:
        print(f"User '{username}' not found.")

 
# def list_tasks():
#     """List all tasks in the database."""
#     tasks = session.query(Task).all()
#     if tasks:
#         for task in tasks:
#             print(f"Task ID: {task.id}, Name: {task.name}, Description: {task.description}, Due Date: {task.due_date}, Priority: {task.priority}")
#     else:
#         print("No tasks found.")
def list_tasks():
    """List tasks for a specific user."""
    username = input("Enter username to list tasks: ")
    user = session.query(User).filter_by(username=username).first()
    if user:
        tasks = session.query(Task).filter_by(user_id=user.id).all()
        if tasks:
            for task in tasks:
                print(f"Task ID: {task.id}, Name: {task.name}, Description: {task.description}, Due Date: {task.due_date}, Priority: {task.priority}")
        else:
            print(f"No tasks found for user '{username}'.")
    else:
        print(f"User '{username}' not found.")

 
@click.argument('task_id', type=int)
def delete_task(task_id):
    """Delete a task from the database."""
    task = session.query(Task).filter_by(id=task_id).first()
    if task:
        session.delete(task)
        session.commit()
        print(f"Task ID {task_id} deleted successfully!")
    else:
        print(f"Task ID {task_id} not found.")

@click.command()
@click.argument('username')
@click.argument('name')
@click.option('--description', default=None, help='Task description')
@click.option('--due_date', default=None, help='Due date for the task (YYYY-MM-DD HH:MM:SS)')
@click.option('--priority', default=None, help='Task priority')
@click.option('--category_id', default=None, type=int, help='Category ID for the task')
def add_task_command(username, name, description, due_date, priority, category_id):
    """Add a new task to the database."""
    add_task(username, name, description, due_date, priority, category_id)
def add_task(username, name, description, due_date, priority, category_id):
    """Add a new task to the database using the username."""
    user = session.query(User).filter_by(username=username).first()
    if not user:
        print(f"User '{username}' not found.")
        return

    task = Task(
        name=name,
        description=description,
        due_date=datetime.strptime(due_date, "%Y-%m-%d %H:%M:%S") if due_date else None,
        priority=priority,
        user_id=user.id,
        category_id=category_id
    )

    session.add(task)
    session.commit()
    print(f"Task '{name}' added successfully!")
def list_users():
    """List all users in the database."""
    users = session.query(User).all()
    if users:
        for user in users:
            print(f"User ID: {user.id}, Username: {user.username}, Email: {user.email}")
    else:
        print("No users found.")

if __name__ == '__main__':
    cli()
