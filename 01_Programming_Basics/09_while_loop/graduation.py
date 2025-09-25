name = input()

bad_grade = 0
average_grade = 0
current_class = 1
sum_of_grades = 0

while current_class <= 12:
    grade = float(input())

    if grade < 4.00:
        bad_grade += 1
        if bad_grade > 1:
            print(f"{name} has been excluded at {current_class} grade")
            break
        continue

    sum_of_grades += grade
    current_class += 1
    average_grade = sum_of_grades / 12

else:
    print(f"{name} graduated. Average grade: {average_grade:.2f}")