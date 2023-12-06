#!/home/admin_ar/hexlet-git/python-project-49/.venv/bin/python
import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name_gamer = prompt.string('May I have your name? ')
    print(f"Hello, {name_gamer}")
