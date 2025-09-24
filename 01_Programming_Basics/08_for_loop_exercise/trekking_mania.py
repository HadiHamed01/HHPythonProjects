climbers_group_count = int(input())

mussala_count = 0
monblan_count = 0
kilimanjaro_count = 0
k2_count = 0
everest_count = 0

for num in range(climbers_group_count):
    climbers_per_group_count = int(input())

    if climbers_per_group_count <= 5:
        mussala_count += climbers_per_group_count
    elif climbers_per_group_count <= 12:
        monblan_count += climbers_per_group_count
    elif climbers_per_group_count <= 25:
        kilimanjaro_count += climbers_per_group_count
    elif climbers_per_group_count <= 40:
        k2_count += climbers_per_group_count
    elif climbers_per_group_count >= 41:
        everest_count += climbers_per_group_count

total_count = mussala_count + monblan_count + kilimanjaro_count + k2_count + everest_count

mussala_percentage = (mussala_count / total_count) * 100
monblan_percentage = (monblan_count / total_count) * 100
kilimanjaro_percentage = (kilimanjaro_count / total_count) * 100
k2_percentage = (k2_count / total_count) * 100
everest_percentage = (everest_count / total_count) * 100

print(f"{mussala_percentage:.2f}%")
print(f"{monblan_percentage:.2f}%")
print(f"{kilimanjaro_percentage:.2f}%")
print(f"{k2_percentage:.2f}%")
print(f"{everest_percentage:.2f}%")