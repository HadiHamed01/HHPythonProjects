deposit = float(input())
deposit_deadline = float(input())
annual_tax_percentage = float(input()) / 100

sum = deposit + deposit_deadline * ((deposit * annual_tax_percentage) / 12)
print (sum)