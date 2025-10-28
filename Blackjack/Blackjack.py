import random

ranks = ["2", "3", "4", "5", "6", "7", "8", "9",
         "10", "Jack", "Queen", "King", "Ace"]
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
values = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11
}

deck = []
dealer = []
player = []

for suit in suits:
    for rank in ranks:
        card = [rank, suit]
        deck.append(card)

random.shuffle(deck)
print(len(deck))

# first hand
player.append(deck.pop(0))
dealer.append(deck.pop(0))

# second hand
player.append(deck.pop(0))
dealer.append(deck.pop(0))


def hand_value(hand):
    total = 0
    for card in hand:
        rank = card[0]
        value = values[rank]
        total += value
    return total


print("Player Hand:", player)
player_value = hand_value(player)
print("Player Total:", player_value)


print("Dealer Hand:", dealer[0])
dealer_value = hand_value([dealer[0]])
print("Dealer Total:", dealer_value)


def hit(hand):
    card = deck.pop(0)
    hand.append(card)
    return card


if hand_value(player) == 21:
    print("Blackjack! You win!")
    quit()

while True:
    choice = input("h/s: ")

    if choice == "h":
        hit(player)
        print(player)

        if hand_value(player) > 21:
            print("You bust.")
            break

    if choice == "s":
        print("Dealer reveals:", dealer)

        while hand_value(dealer) < 17:
            hit(dealer)
            print(dealer)
            print(hand_value(dealer))
        break

    print(hand_value(player))
