
import dice

number_of_dices = 0

# main loop 
if __name__ == "__main__":

    number_of_dices = int(input("How many dices do you want to roll? "))

    # check if the number of dices is vaid between 1 and 6
    if number_of_dices < 1 or number_of_dices > 6:
        print("You can only roll between 1 and 6 dices")
        exit()

    for roll in range(number_of_dices):
        dice_num = dice.roll_dice()
        print(f" Roll: {roll+1} - Number: {dice_num}\n")

