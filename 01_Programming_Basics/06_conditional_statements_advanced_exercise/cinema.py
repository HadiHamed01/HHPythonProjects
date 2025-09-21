premiere = 12.00
normal = 7.50
discount = 5.00

type_of_movie = str(input())
rows_count = int(input())
columns_count = int(input())

if type_of_movie == "Premiere":
    total_price = columns_count * rows_count * premiere
elif type_of_movie == "Normal":
    total_price = columns_count * rows_count * normal
elif type_of_movie == "Discount":
    total_price = columns_count * rows_count * discount

print(f"{total_price:.2f} leva")