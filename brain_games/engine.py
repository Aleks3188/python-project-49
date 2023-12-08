import prompt
from brain_games.cli import welcome_user


GAME_ROUNDS = 3


def run_games(game):
    name_gamer = welcome_user()
    print(game.DESCRIPTION)
    for _ in range(GAME_ROUNDS):
        gener_number, gener_answer = game.gener_ques_and_answer()
        print(f'Question: {gener_number}')
        gamer_answer = prompt.string('Your answer: ')
        if gamer_answer != gener_answer:
            print(
                f"'{gamer_answer}' is wrong answer ;(."
                f"Correct answer was '{gener_answer}'"
                )
            print(f"Let's try again, {name_gamer}")
            return
        print('Correct!')
    print(f'Congratulation, {name_gamer}')
