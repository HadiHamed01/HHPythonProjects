deck_of_cards = input().split()
count_of_shuffles = int(input())

for shuffle in range(count_of_shuffles):
    middle_deck = len(deck_of_cards) // 2
    left_part = deck_of_cards[0:middle_deck]
    right_part = deck_of_cards[middle_deck:]

    deck_after_shuffling = []

    for card in range(len(left_part)): # OR (len(right_part))
        deck_after_shuffling.append(left_part[card])
        deck_after_shuffling.append(right_part[card])

    deck_of_cards = deck_after_shuffling

print(deck_after_shuffling)