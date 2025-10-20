def todo_tasks():
    my_list = []

    while True:
        command = input()
        if command == "End":
            break
        my_list.append(command)

    sorted_tasks = sorted(my_list, key=lambda x: int(x.split("-")[0]))
    return [command.split("-")[1] for command in sorted_tasks]


print(todo_tasks())