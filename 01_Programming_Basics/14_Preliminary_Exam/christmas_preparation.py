wrapping_paper_price = 5.80
cloth_price = 7.20
duct_tape_price = 1.20

wrapping_paper_count = int(input())
cloth_count = int(input())
duct_tape_count = float(input())
percentage_discount = int(input())

total_price = (wrapping_paper_price * wrapping_paper_count) + (cloth_price * cloth_count) \
    + (duct_tape_price * duct_tape_count)

total_price = total_price * (1 - (percentage_discount / 100))

print(f"{total_price:.3f}")