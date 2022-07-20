import dice

times_to_roll_dice = 0
dice_role_list = []


def check_input(dices_roll_value):
    '''Checks the input string and returns the number of dices to roll'''
    if dices_roll_value < 1 or dices_roll_value > 6:
        print("You can only roll between 1 and 6 dices")
        raise SystemExit(1)
    return dices_roll_value


def generate_dice_art(dices_to_draw):
    '''Generates the dice art for the given dice number'''

    # Get for eact dice, grab the parts from DICE_ART
    dice_faces_to_display = []
    for number in dices_to_draw:
        dice_faces_to_display.append(dice.DICE_ART[number])

    # Stack the dice faces rows together
    dice_faces_rows = []
    for row in range(dice.DIE_HEIGHT):
        dice_rows = []

        for dice_face in dice_faces_to_display:
            dice_rows.append(dice_face[row])

        row_string = dice.DIE_FACE_SEPARATOR.join(dice_rows)
        dice_faces_rows.append(row_string)

    # Generate header with the word "RESULTS" centered
    width = len(dice_faces_rows[0])
    diagram_header = " RESULTS ".center(width, "~")

    dice_faces_diagram = "\n".join([diagram_header] + dice_faces_rows)
    return dice_faces_diagram


# main loop
if __name__ == "__main__":

    times_to_roll_dice = int(input("How many dices do you want to roll? "))

    check_input(times_to_roll_dice)

    for roll in range(times_to_roll_dice):
        dice_num = dice.roll_dice()
        dice_role_list.append(dice_num)

    # print the dices
    print(generate_dice_art(dice_role_list))
