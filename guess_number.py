import random


def check_guess(lucky_number: int, user_guess: int) -> str:
    if not isinstance(user_guess, int):
        raise ValueError("ValueError")
    if user_guess < 1 or user_guess > 100:
        raise ValueError("number out of range")
    if lucky_number == user_guess:
        return "BINGO!!"
    elif lucky_number > user_guess:
        return "guess higher"
    else:
        return "guess lower"



def game_guessing_play():
    rnd_number = random.randint(1, 100)
    while True:
        try:
            user_guess2 = int(input("Guess a number between 1-100:"))
            feedback: str = check_guess(lucky_number=rnd_number, user_guess=user_guess2)
            print(feedback)
            if feedback == "BINGO!!":
                break
        except Exception as ex:
            print(ex)