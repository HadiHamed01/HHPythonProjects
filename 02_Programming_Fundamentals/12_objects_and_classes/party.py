class Party:
    def __init__(self):
        self.people = []


party = Party()
people_count = 0
command = input()
while command != "End":
    people_count += 1
    party.people.append(command)
    command = input()

print(f"Going: {', '.join(party.people)}")
print(f"Total: {people_count}")