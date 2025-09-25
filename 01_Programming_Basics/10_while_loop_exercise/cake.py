length = int(input())
width = int(input())
pieces_taken = input()

pieces_left = length * width

while pieces_taken != "STOP":
    pieces_taken = int(pieces_taken)
    pieces_left -= pieces_taken

    if pieces_left < 0:
        print(f"No more cake left! You need {abs(pieces_left)} pieces more.")
        break

    pieces_taken = input()

else:
    print(f"{pieces_left} pieces are left.")