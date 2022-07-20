import dice

times_to_roll_dice = 0
dice_role_list = []


# main loop
if __name__ == "__main__":

    times_to_roll_dice = int(input("How many dices do you want to roll? "))

    dice.check_input(times_to_roll_dice)

    for roll in range(times_to_roll_dice):
        dice_num = dice.roll_dice()
        dice_role_list.append(dice_num)

    print(f"You rolled {dice_role_list}")

    # print the dices
    print(dice.generate_dice_art(dice_role_list))
