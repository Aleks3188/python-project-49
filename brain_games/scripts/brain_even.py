#!/home/admin_ar/hexlet-git/python-project-49/.venv/bin/python
from random import randint
import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name_gamer = prompt.string('May I have your name? ')
    print(f"Hello, {name_gamer}")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for index in range(3): 
        number_random = randint(1, 10) 
        print(f'Question: {number_random}')
        geymer__answer = prompt.string('Your answer: ')
        if number_random % 2 == 0:
            if geymer__answer == 'yes':
                print('Correct!')
            elif geymer__answer == 'no':
                print(f''''yes' is wrong answer ;(. Correct answer was 'no'.
Let's try again, {name_gamer}
            ''')
                break
        else: 
            print(f''''yes' is wrong answer ;(. Correct answer was 'no'.
Let's try again, {name_gamer}
            ''') 
            break
        if number_random % 2 != 0:
            if geymer__answer == 'no':
                print('Correct!')
            elif geymer__answer == 'yes':
                print(f''''yes' is wrong answer ;(. Correct answer was 'no'.
Let's try again, {name_gamer}
            ''')
                break
        else: 
            print(f''''yes' is wrong answer ;(. Correct answer was 'no'.
Let's try again, {name_gamer}
            ''') 
            break


def main():
    welcome_user()


if __name__ == '__main__':
    main()
