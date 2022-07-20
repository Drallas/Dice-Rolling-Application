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


DICE_ART = {

    1: (

        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",

    ),

    2: (

        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",

    ),

    3: (

        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",

    ),

    4: (

        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",

    ),

    5: (

        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",

    ),

    6: (

        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",

    ),

}

DIE_HEIGHT = len(DICE_ART[6])  # Dice has 5 list items
DIE_FACE_SEPARATOR = " "


def generate_dice_art(dices_to_draw):
    '''Generates the dice art for the given dice number'''

    # Get for eact dice, grab the parts from DICE_ART
    dice_faces_to_display = []
    for number in dices_to_draw:
        dice_faces_to_display.append(DICE_ART[number])

    # Stack the dice faces rows together
    dice_faces_rows = []
    for row in range(DIE_HEIGHT):
        dice_rows = []

        for dice_face in dice_faces_to_display:
            dice_rows.append(dice_face[row])

        row_string = DIE_FACE_SEPARATOR.join(dice_rows)
        dice_faces_rows.append(row_string)

    # Generate header with the word "RESULTS" centered
    width = len(dice_faces_rows[0])
    diagram_header = " RESULTS ".center(width, "~")

    dice_faces_diagram = "\n".join([diagram_header] + dice_faces_rows)
    return dice_faces_diagram
