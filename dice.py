import random


def check_input(dices_roll_value):
    '''Checks the input string and returns the number of dices to roll'''
    if dices_roll_value < 1 or dices_roll_value > 6:
        print("You can only roll between 1 and 6 dices")
        raise SystemExit(1)
    return dices_roll_value


def roll_dice():
    '''Creates a random number between 1 and 6'''
    return random.randint(1, 6)
