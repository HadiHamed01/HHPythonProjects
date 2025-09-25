bad_grades_limit = int(input())
task_name = input()

bad_grade = 0
average_grade = 0
number_of_tasks = 0
sum_of_grades = 0
last_task_name = ""

while task_name != "Enough":
    grade = int(input())

    if grade <= 4:
        bad_grade += 1
        if bad_grade == bad_grades_limit:
            print(f"You need a break, {bad_grade} poor grades.")
            break

    last_task_name = task_name
    number_of_tasks += 1
    sum_of_grades += grade
    average_grade = sum_of_grades / number_of_tasks

    task_name = input()

else:
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {number_of_tasks}")
    print(f"Last problem: {last_task_name}")