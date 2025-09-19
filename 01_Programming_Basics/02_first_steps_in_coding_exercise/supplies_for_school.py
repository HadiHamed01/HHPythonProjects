pen = 5.80
marker = 7.20
detergent = 1.20

necessary_pens = int(input())
necessary_markers = int(input())
necessary_detergent = int(input())
discount = int(input()) / 100

total_pens = pen * necessary_pens
total_markers = marker * necessary_markers
total_detergent = detergent * necessary_detergent

sum = total_pens + total_markers + total_detergent
final_sum = sum - (discount * sum)

print(final_sum)