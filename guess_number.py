import random


def guess_number():
    random_number = random.randint(1, 100)

    print("Guess number between 1 to 100")
    guess = 0

    while guess != random_number:
        guess = int(input("input a number: "))
        if guess < random_number:
            print("Number too low, try again")
        elif guess > random_number:
            print("Number too high, try again!")

    print("Congrats, you have guessed it right!")


guess_number()
