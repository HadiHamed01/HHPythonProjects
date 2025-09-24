num_of_tabs = int(input())
salary = int(input())

facebook_fine = 150
instagram_fine = 100
reddit_fine = 50

for numbers in range(num_of_tabs):
    website_name = str(input())
    if website_name == "Facebook":
        salary -= facebook_fine
    elif website_name == "Instagram":
        salary -= instagram_fine
    elif website_name == "Reddit":
        salary -= reddit_fine

    if salary <= 0:
        print(f"You have lost your salary.")
        break

if salary > 0:
    print(salary)