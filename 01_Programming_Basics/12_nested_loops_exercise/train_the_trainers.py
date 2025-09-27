jury = int(input())
command = input()

total_presentation_sum = 0
presentation_count = 0

while command != "Finish":
    current_presentation = command

    current_presentation_sum = 0
    for _ in range(jury):
        mark = float(input())
        current_presentation_sum += mark

    total_presentation_sum += current_presentation_sum
    presentation_count += 1

    print(f"{current_presentation} - {current_presentation_sum / jury:.2f}.")

    command = input()

average_total_grades = total_presentation_sum / (presentation_count * jury)
print(f"Student's final assessment is {average_total_grades:.2f}.")