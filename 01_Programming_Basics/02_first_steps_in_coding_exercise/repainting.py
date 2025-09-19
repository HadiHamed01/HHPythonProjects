nylon = 1.50
paint = 14.50
paint_refiller = 5.00
bags = 0.40

total_nylon = ( int(input()) + 2 ) * nylon
necessary_paint = int(input())
total_paint = ( necessary_paint + (0.1 * necessary_paint)) * paint
total_paint_refiller = int(input()) * paint_refiller
hours_for_completion = int(input())

sum_of_costs = total_nylon + total_paint + total_paint_refiller + bags
sum_of_employee_costs = ( sum_of_costs * 0.3 ) * hours_for_completion
final_sum = sum_of_costs + sum_of_employee_costs

print(final_sum)