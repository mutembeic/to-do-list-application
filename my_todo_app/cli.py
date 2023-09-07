import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base, User, Task, Category
from .config import DATABASE_URL
from datetime import datetime

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
def display_options():
    """Display a welcome message and list of available commands."""
    click.echo("Welcome to the Task Management CLI App!\n")
    click.echo("Options:")
    click.echo("1. add_user")
    click.echo("2. add_task")
    click.echo("3. list_tasks")
    click.echo("4. delete_task")

def select_option():
    """Prompt the user to select an option."""
    while True:
        selected_option = click.prompt("Select an option (1-4)", type=int)
        if 1 <= selected_option <= 4:
            return selected_option
        else:
            click.echo("Invalid option. Please select a valid option (1-4).")

@click.group()
def cli():
    pass

@cli.command()
def welcome():
    """Display a welcome message and list of available commands."""
    display_options()
    selected_option = select_option()
    if selected_option == 1:
        add_user()
    elif selected_option == 2:
        add_task()
    elif selected_option == 3:
        list_tasks()
    elif selected_option == 4:
        delete_task()
# def display_options():
#     """Display a welcome message and list of available commands."""
#     click.echo("Welcome to the Task Management CLI App!\n")
#     click.echo("Options:")
#     click.echo("1. add_user")
#     click.echo("2. add_task")
#     click.echo("3. list_tasks")
#     click.echo("4. delete_task")

# @click.group()
# def cli():
#     pass

# @cli.command()
# def welcome():
#     """Display a welcome message and list of available commands."""
#     display_options()

@cli.command()
@click.option('--username', prompt='Username', help='User\'s username')
@click.option('--email', prompt='Email', help='User\'s email')
def add_user(username, email):
    session = Session()
    user = User(username=username, email=email)
    session.add(user)
    session.commit()
    session.close()
    click.echo(f"User {username} added successfully!")

@cli.command()
@click.option('--name', prompt='Task name', help='Task name')
@click.option('--description', prompt='Task description', help='Task description')
@click.option('--due_date', prompt='Due date (YYYY-MM-DD HH:MM:SS)', help='Due date')
@click.option('--priority', prompt='Priority', help='Priority')
@click.option('--username', prompt='Username', help='User\'s username')
@click.option('--category_name', prompt='Category name', help='Category name')
def add_task(name, description, due_date, priority, username, category_name):
    session = Session()
    user = session.query(User).filter_by(username=username).first()
    if not user:
        click.echo(f"User {username} does not exist.")
        return

    category = session.query(Category).filter_by(name=category_name).first()
    if not category:
        category = Category(name=category_name)
        session.add(category)

    due_date = datetime.strptime(due_date, '%Y-%m-%d %H:%M:%S')

    task = Task(name=name, description=description, due_date=due_date, priority=priority, user=user, category=category)
    session.add(task)
    session.commit()
    session.close()
    click.echo(f"Task {name} added successfully!")

@cli.command()
@click.option('--username', prompt='Username', help='User\'s username')
def list_tasks(username):
    session = Session()
    user = session.query(User).filter_by(username=username).first()
    if not user:
        click.echo(f"User {username} does not exist.")
        return

    tasks = user.tasks
    if not tasks:
        click.echo(f"No tasks found for {username}.")
    else:
        click.echo(f"Tasks for {username}:")
        for task in tasks:
            click.echo(f"Task: {task.name}, Category: {task.category.name}, Due Date: {task.due_date}, Priority: {task.priority}, Created At: {task.created_at}")

@cli.command()
@click.option('--username', prompt='Username', help='User\'s username')
@click.option('--task_id', prompt='Task ID', help='Task ID')
def delete_task(username, task_id):
    session = Session()
    user = session.query(User).filter_by(username=username).first()
    if not user:
        click.echo(f"User {username} does not exist.")
        return

    task = session.query(Task).filter_by(id=task_id, user=user).first()
    if not task:
        click.echo(f"Task with ID {task_id} does not exist for {username}.")
        return

    session.delete(task)
    session.commit()
    session.close()
    click.echo(f"Task with ID {task_id} deleted successfully for {username}!")

if __name__ == '__main__':
    cli()


# import click
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from .models import Base, User, Task, Category
# from .config import DATABASE_URL
# from datetime import datetime

# engine = create_engine(DATABASE_URL)
# Session = sessionmaker(bind=engine)
# def display_options():
#     """Display a welcome message and list of available commands."""
#     click.echo("Welcome to the Task Management CLI App!\n")
#     click.echo("Options:")
#     click.echo("1. add_user")
#     click.echo("2. add_task")
#     click.echo("3. list_tasks")
#     click.echo("4. delete_task")

# def select_option():
#     """Prompt the user to select an option."""
#     while True:
#         selected_option = click.prompt("Select an option (1-4)", type=int)
#         if 1 <= selected_option <= 4:
#             return selected_option
#         else:
#             click.echo("Invalid option. Please select a valid option (1-4).")

# @click.command()
# def welcome():
#     """Display a welcome message and list of available commands."""
#     display_options()
#     selected_option = select_option()
#     if selected_option == 1:
#         add_user()
#     elif selected_option == 2:
#         add_task()
#     elif selected_option == 3:
#         list_tasks()
#     elif selected_option == 4:
#         delete_task()

# @click.group()
# def cli():
#     pass


# @cli.command()
# @click.option('--name', prompt='Task name', help='Task name')
# @click.option('--description', prompt='Task description', help='Task description')
# @click.option('--due_date', prompt='Due date (YYYY-MM-DD HH:MM:SS)', help='Due date')
# @click.option('--priority', prompt='Priority', help='Priority')
# @click.option('--username', prompt='Username', help='User\'s username')
# @click.option('--category_name', prompt='Category name', help='Category name')
# def add_task(name, description, due_date, priority, username, category_name):
#     session = Session()
#     user = session.query(User).filter_by(username=username).first()
#     if not user:
#         click.echo(f"User {username} does not exist.")
#         return

#     category = session.query(Category).filter_by(name=category_name).first()
#     if not category:
#         category = Category(name=category_name)
#         session.add(category)

#     due_date = datetime.strptime(due_date, '%Y-%m-%d %H:%M:%S')

#     user.last_task_id += 1  # Increment the last task ID for the user
#     task = Task(id=user.last_task_id, name=name, description=description, due_date=due_date, priority=priority, user=user, category=category)
#     session.add(task)
#     session.commit()
#     session.close()
#     click.echo(f"Task {name} added successfully!")

# @cli.command()
# @click.option('--username', prompt='Username', help='User\'s username')
# def list_tasks(username):
#     session = Session()
#     user = session.query(User).filter_by(username=username).first()
#     if not user:
#         click.echo(f"User {username} does not exist.")
#         return

#     tasks = user.tasks
#     if not tasks:
#         click.echo(f"No tasks found for {username}.")
#     else:
#         click.echo(f"Tasks for {username}:")
#         for task in tasks:
#             click.echo(f"Task ID: {task.id}, Task: {task.name}, Category: {task.category.name}, Due Date: {task.due_date}, Priority: {task.priority}, Created At: {task.created_at}")

# @cli.command()
# @click.option('--username', prompt='Username', help='User\'s username')
# @click.option('--task_id', prompt='Task ID', help='Task ID')
# def delete_task(username, task_id):
#     session = Session()
#     user = session.query(User).filter_by(username=username).first()
#     if not user:
#         click.echo(f"User {username} does not exist.")
#         return

#     task = session.query(Task).filter_by(id=task_id, user=user).first()
#     if not task:
#         click.echo(f"Task with ID {task_id} does not exist for {username}.")
#         return

#     session.delete(task)
#     session.commit()
#     session.close()
#     click.echo(f"Task with ID {task_id} deleted successfully for {username}!")

# if __name__ == '__main__':
#     cli()
