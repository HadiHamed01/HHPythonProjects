needed_book = input()
current_book = input()

book_count = 0

while current_book != "No More Books":

    if current_book == needed_book:
        print(f"You checked {book_count} books and found it.")
        break

    current_book = input()
    book_count += 1

else:
    print(f"The book you search is not here! \nYou checked {book_count} books.")