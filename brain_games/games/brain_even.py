from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'

def gener_ques_and_answer():
    gener_number = randint(1, 20)
    gener_answer = 'yes' if gener_number % 2 == 0 else 'no'
    return gener_number, gener_answer
