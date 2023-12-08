import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'

def generation_ques_and_answer():
    correct_answer = 0
    # Answers yes or no because lenght_string > 80
    yes_answer = "is wrong answer ;(. Correct answer was 'yes'."
    no_answer = "is wrong answer ;(. Correct answer was 'no'."
    for _ in range(3):
        number_random = randint(1, 20)
        print(f'Question: {number_random}')
        geymer__answer = prompt.string('Your answer: ')
        if number_random % 2 == 0:
            if geymer__answer == 'yes':
                print('Correct!')
            else:
                print(f"'{geymer__answer}' {yes_answer}")
                print(f"Let's try again, {name_gamer}")
                break
        else:
            if geymer__answer == 'no':
                print('Correct!')
            else:
                print(f"'{geymer__answer}' {no_answer}")
                print(f"Let's try again, {name_gamer}")
                break
        correct_answer += 1
    if correct_answer == 3:
        print(f'Congratulations, {name_gamer}')