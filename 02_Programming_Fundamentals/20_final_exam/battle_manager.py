people = {}
command = input().split(":")

while command[0] != "Results":

    if command[0] == "Add":
        person_name, health, energy = command[1], int(command[2]), int(command[3])
        if person_name not in people:
            people[person_name] = {'person': person_name, 'health': health, 'energy': energy}
        else:
            people[person_name]['health'] += health

    elif command[0] == "Attack":
        attacker_name, defender_name, damage = command[1], command[2], int(command[3])
        if attacker_name in people and defender_name in people:
            people[defender_name]['health'] -= damage
            people[attacker_name]['energy'] -= 1

            if people[defender_name]['health'] <= 0:
                print(f"{defender_name} was disqualified!")
                del people[defender_name]

            if people[attacker_name]['energy'] <= 0:
                print(f"{attacker_name} was disqualified!")
                del people[attacker_name]

    elif command[0] == "Delete":
        username = command[1]
        if username in people:
            del people[username]
        elif username == "All":
            people.clear()

    command = input().split(":")


print(f"People count: {len(people)}")

for key, value in people.items():
    print(f"{key} - {value['health']} - {value['energy']}")