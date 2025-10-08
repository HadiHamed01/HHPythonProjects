count = int(input())
maximum_capacity = 255
total_litres = 0

for number in range(count):
    litres_to_pour = int(input())
    total_litres += litres_to_pour

    if total_litres > maximum_capacity:
        print("Insufficient capacity!")
        total_litres -= litres_to_pour
        continue

print(total_litres)