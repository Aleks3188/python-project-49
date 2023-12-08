from random import randint, choice
import operator


DESCRIPTION = 'What is the result of the expression?'


def gener_ques_and_answer():
    one_number = randint(1, 50)
    two_number = randint(1, 50)
    operators_symbol = ('+', '-', '*')
    get_operator = choice(operators_symbol)
    gener_answer = f'{one_number} {get_operator} {two_number}'
    #gener_number = 5
    return gener_answer, gener_number

#gener_ques_and_answer()