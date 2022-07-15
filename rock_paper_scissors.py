import random


def play():
    user = input(
        "What's your choice? 'r' for rock, 'p' for paper, and 's' for scissors \n"
    )

    computer = random.choice(["r", "p", "s"])

    if user != "r" and user != "p" and user != "s":
        return "Invalid input"

    if user.lower() == computer:
        return "It's a tie"

    if is_win(user, computer):
        return "You won"

    return "You lost"


def is_win(player, opponent):
    if (
        (player == "r" and opponent == "s")
        or (player == "p" and opponent == "r")
        or (player == "s" and opponent == "p")
    ):
        return True


print(play())
