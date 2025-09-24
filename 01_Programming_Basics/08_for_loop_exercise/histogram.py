num_inputs = int(input())

p1_count = 0
p2_count = 0
p3_count = 0
p4_count = 0
p5_count = 0

for numbers in range(num_inputs):
    user_inputs = int(input())

    if user_inputs < 200:
        p1_count += 1

    elif user_inputs < 400:
        p2_count += 1

    elif user_inputs < 600:
        p3_count += 1

    elif user_inputs < 800:
        p4_count += 1

    else:
        p5_count += 1

p1_percentage = (p1_count / num_inputs) * 100
p2_percentage = (p2_count / num_inputs) * 100
p3_percentage = (p3_count / num_inputs) * 100
p4_percentage = (p4_count / num_inputs) * 100
p5_percentage = (p5_count / num_inputs) * 100

print(f"{p1_percentage:.2f}% \n{p2_percentage:.2f}% \n{p3_percentage:.2f}% \n{p4_percentage:.2f}% \n{p5_percentage:.2f}%")