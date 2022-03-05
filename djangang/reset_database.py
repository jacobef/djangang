"""
THIS PROGRAM SHOULD ONLY BE RUN IN DEVELOPMENT. IT SHOULD NEVER BE RUN ONCE THE WEBSITE IS DEPLOYED.
What it does:
1. Removes all migrations files
2. Removes the database (db.sqlite3)
3. Makes the migrations files again (equivalent to: python manage.py makemigrations)
4. Creates the database and migrates stuff to it (equivalent to: python manage.py migrate)
"""

import shutil
from sys import stderr

import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangang.settings")
django.setup()

from typing import Callable, Any

from djangang.settings import BASE_DIR

from django.core import management
from django.apps import apps

ignored_dirnames = [".git", ".idea", "venv"]


# ----------------
# HELPER FUNCTIONS
# ----------------

def in_ignored_dir(dirpath: str) -> bool:
    for dirname in ignored_dirnames:
        if dirname in dirpath:
            return True
    return False


def remove_with_msg(path: bytes):
    if os.path.isfile(path):
        os.remove(path)
        print(f"Removed file: {path}")
    elif os.path.isdir(path):
        shutil.rmtree(path)
        print(f"Removed directory: {path}")
    else:
        print(f"""Warning: "{path}" is not a file or folder, so I don't know what it is or how to remove it.
Because of this, it will not be removed.""", file=stderr)


def django_command_with_msg(command: str):
    print("[BEGIN DJANGO AUTOGENERATED MESSAGE]")
    management.call_command(command)
    print("[END DJANGO AUTOGENERATED MESSAGE]")


# ----------------
# MAIN FUNCTIONS
# ----------------

def remove_migrations_files():
    print("Removing migrations files...")

    # Gets list of migrations folders
    migrations_dirs: list[bytes] = []
    for dirpath, dirnames, filenames in os.walk(BASE_DIR):
        app_dirs = [app.path for app in apps.get_app_configs()]
        if dirpath in app_dirs and not in_ignored_dir(dirpath):
            for dirname in dirnames:
                if dirname == "migrations":
                    migrations_dirs.append(os.path.join(dirpath, dirname))

    # Removes migrations files
    for migrations_dir in migrations_dirs:
        for dir_entry in os.listdir(migrations_dir):
            if dir_entry != "__init__.py":
                remove_with_msg(os.path.join(migrations_dir, dir_entry))

    print("Migrations files removed.", end='\n\n')


def remove_database():
    print("Removing database file...")
    database_path = os.path.join(BASE_DIR, "db.sqlite3")
    if os.path.exists(database_path):
        remove_with_msg(database_path)
    print("Database file removed.", end='\n\n')


def make_migrations_files():
    print("Making migrations files...")
    django_command_with_msg("makemigrations")
    print("Done making migrations files.", end='\n\n')


def create_database():
    print("Creating database...")
    django_command_with_msg("migrate")
    print("Done creating database.", end='\n\n')

# ----------------------
# INPUT/PRINTING HELPERS
# ----------------------

def make_interactive(function: Callable[[], Any], what_happens: str, manual_instructions, required: bool):
    proceed_automatically = input(f"""{what_happens} 
Would you like this to be done automatically? (y/n) (q to quit) """)
    while proceed_automatically not in ['y', "yes", 'n', "no", 'q', "quit"]:
        print("Invalid input. Enter y or n.")
    if proceed_automatically == 'y' or proceed_automatically == "yes":
        function()
    elif proceed_automatically == 'n' or proceed_automatically == "no":
        print("Would you like to proceed manually?")
        print("If you answer yes, you will be given instructions for how to manually do this, "
              "and this program will pause until you confirm that you have finished.")
        if required:
            print(
                "If you answer no, this program will terminate, since this step is necessary for everything after it to work.")
        else:
            print("If you answer no, this step will be skipped.")
        proceed_manually = input("(y/n) (q to quit) ")
        if proceed_manually == 'q' or proceed_manually == "quit":
            print("Terminating program...")
            exit(0)
        if proceed_manually == 'y' or proceed_manually == "yes":
            print(f"To do this manually: {manual_instructions}")
            input("Hit enter when you finish doing this. ")
        else:
            print("Terminating program...")
            exit(0)


def generate_managedotpy_manual_instructions(command_name: str):
    return f"""Open a new terminal tab or window (don't close this tab). 
Go into the project's root directory (the one with manage.py in it).
Activate your virtual environment. Then, run "python manage.py {command_name}".
This will NOT work if you type that command in here, since you'd just be typing it into this Python input."""


# ------------
# MAIN PROGRAM
# ------------

print("""
THIS PROGRAM SHOULD ONLY BE RUN IN DEVELOPMENT. IT SHOULD NEVER BE RUN ONCE THE WEBSITE IS DEPLOYED.
If the website has been deployed, quit the program. Nothing will be affected if you quit it now.
This program will reset everything except the code you've written.
Specifically, it will remove the database and migrations files if they exist, create an empty database, then create users for testing.
""")
everything_automatic = input(
    """Do you want everything to be done automatically, without prompting?
If you answer no, you will be prompted for each action that will be taken. 
(y/n) (q to quit) """
)

if everything_automatic == 'y' or everything_automatic == "yes":
    remove_migrations_files()
    remove_database()
    make_migrations_files()
    create_database()


elif everything_automatic == 'n':
    make_interactive(function=remove_migrations_files,
                     what_happens="The migrations files will be removed.",
                     manual_instructions="Remove every file under every folder named 'migrations', except '__init__.py' files.",
                     required=True)

    make_interactive(function=remove_database,
                     what_happens="The database file (db.sqlite3) will be deleted.",
                     manual_instructions="Remove the db.sqlite3 file. It is located in your project's root directory (in the same directory as manage.py)",
                     required=True)

    make_interactive(function=make_migrations_files,
                     what_happens="The migrations files will be created (equivalent to 'python manage.py makemigrations').",
                     manual_instructions=generate_managedotpy_manual_instructions("makemigrations"),
                     required=True)

    make_interactive(function=create_database,
                     what_happens="The database will be created from the migrations files (equivalent to 'python manage.py migrate').",
                     manual_instructions=generate_managedotpy_manual_instructions("migrate"),
                     required=True)

else:
    print("Exiting the program. The program has not made any changes to your files, nor has it reset anything.")
    exit(0)

print("All done!")
