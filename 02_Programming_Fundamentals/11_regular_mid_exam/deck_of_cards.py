cards = input().split(", ")
count = int(input())

list_of_cards = [card for card in cards]

for num in range(count):
    command = input().split(", ")

    if command[0] == "Add":
        if command[1] in list_of_cards:
            print("Card is already in the deck")
        else:
            list_of_cards.append(command[1])
            print("Card successfully added")

    elif command[0] == "Remove":
        if not command[1] in list_of_cards:
            print("Card not found")
        else:
            list_of_cards.remove(command[1])
            print("Card successfully removed")

    elif command[0] == "Remove At":
        if not int(command[1]) in range(len(list_of_cards)):
            print("Index out of range")
        else:
            index = int(command[1])
            removed_card = list_of_cards.pop(index)
            print("Card successfully removed")

    elif command[0] == "Insert":
        if not int(command[1]) in range(len(list_of_cards)):
            print("Index out of range")
        elif command[2] in list_of_cards:
            print("Card is already added")
        else:
            index = int(command[1])
            card = command[2]
            list_of_cards.insert(index, card)
            print("Card successfully added")

print(", ".join(map(str, list_of_cards)))