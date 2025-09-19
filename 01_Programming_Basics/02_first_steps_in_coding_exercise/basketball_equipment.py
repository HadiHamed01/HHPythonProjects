yearly_tax = int(input())

sneakers = yearly_tax - (yearly_tax * 0.4)  # or it can be sneakers = yearly_tax * 0.6
team = sneakers - (sneakers * 0.2)  # or it can be team = sneakers * 0.8
ball = team * 0.25
accessories = ball * 0.2

sum = yearly_tax + sneakers + team + ball + accessories

print(sum)