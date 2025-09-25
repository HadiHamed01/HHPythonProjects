steps_goal = 10000
current_steps = input()

sum_steps = 0

while current_steps != "Going home":
    current_steps = int(current_steps)
    sum_steps += current_steps

    if sum_steps >= steps_goal:
        print(f"Goal reached! Good job! \n{sum_steps - steps_goal} steps over the goal!")
        break

    current_steps = input()

else:
    current_steps = int(input())
    sum_steps += current_steps
    if sum_steps >= steps_goal:
        print(f"Goal reached! Good job! \n{sum_steps - steps_goal} steps over the goal!")
    else:
        print(f"{steps_goal - sum_steps} more steps to reach goal.")