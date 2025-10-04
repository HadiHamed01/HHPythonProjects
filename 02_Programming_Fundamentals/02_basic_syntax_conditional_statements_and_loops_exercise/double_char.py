while True:
    string = input()

    if string == "End":
        break
    elif string == "SoftUni":
        continue
    else:
        new_string = ""
        for character in string:
            new_string = new_string + character * 2
        print(new_string)