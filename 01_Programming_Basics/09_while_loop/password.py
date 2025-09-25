username = str(input())
password = str(input())
password_attempt = str(input())

while password_attempt != password:
    password_attempt = str(input())

print(f"Welcome {username}!")