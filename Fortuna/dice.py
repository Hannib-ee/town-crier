import secrets


def roll(dice):
    try:
        num_dice, sides = map(int, dice.split("d"))

        result = [secrets.randbelow(sides) + 1 for i in range(num_dice)]

        return result

    except TypeError:
        return "Invalid input. Please use XdY format"


dice = input("Dice roll: ")
result = roll(dice)
print(f"{result}")
