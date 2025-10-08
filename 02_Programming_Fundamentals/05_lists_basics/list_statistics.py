count = int(input())
positives_list = []
negatives_list = []
count_positives = 0
sum_of_negatives = 0

for number in range(count):
    value = int(input())
    if value >= 0:
        positives_list.append(value)
        count_positives += 1
    else:
        negatives_list.append(value)
        sum_of_negatives += value

print(f"{positives_list} \n{negatives_list}")
print(f"Count of positives: {count_positives} \nSum of negatives: {sum_of_negatives}")