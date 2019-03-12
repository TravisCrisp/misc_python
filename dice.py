import random

def dice_roll(s):
    """Simulates a dice roll for a dice with s sides."""

    choice = str(random.randint(1, s))
    print(f"\nResult: {choice}")

def mult_dice(dice_list):
    """Simulates a dice roll for multiple dice with varying sides."""

    d = {}
    for dice in dice_list:
        d[dice] = d.get(dice, 0) + 1
        # Constructs a dictionary from dice_list.

    for k, v in d.items():
        choices = []
        for n in range(v):
            choices.append(str(random.randint(1, k)))
        print("\nResults for {} Sided Dice: {}".format(k, ", ".join(choices)))

def menu():
    """Asks the user to choose number and sides of dice."""

    while True:
        
        answer = input("\nHow Many Dice? Done (d) ")
        if answer == "d":
            print("\nGoodbye!\n")
            return
        elif answer == "1":
            while True:
                answer = input("\nHow Many Sides? ")
                if answer.isdigit():
                    dice_roll(int(answer))
                    break
                print("\nPlease enter a number!")
            continue
        elif answer.isdigit():
            while True:
                dice_list = []
                for n in range(1, int(answer)+1):
                    while True:
                        dice = input(f"\nDice {n}: How Many Sides? ")
                        if dice.isdigit():
                            dice_list.append(int(dice))
                            break
                        print("\nPlease enter a number!")
                print()
                mult_dice(dice_list)
                break
            continue
        print("\nPlease enter a number!")

if __name__ == '__main__':
	menu()