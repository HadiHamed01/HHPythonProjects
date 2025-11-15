class Email:
    def __init__(self, email):
        self.email = email

    def make_upper(self):
        email_upper = self.email.upper()
        print(email_upper)

    def make_lower(self):
        email_lower = self.email.lower()
        print(email_lower)

    def get_domain(self, count):
        email_domain = self.email[-count:]
        print(email_domain)

    def get_username(self):
        if "@" in self.email:
            username = self.email.split("@")[0]
            print(username)
            return username
        else:
            print(f"The email {self.email} doesn't contain the @ symbol.")

    def replace(self, character):
        email_replace = self.email.replace(character, "-")
        print(email_replace)

    def encrypt(self):
        encrypted_email = [str(ord(letter)) for letter in self.email]
        print(" ".join(encrypted_email))


input_email = input()
emails = Email(input_email)
command = input().split()

while command[0] != "Complete":

    if command[0] == "Make" and command[1] == "Upper":
        emails.make_upper()
    elif command[0] == "Make" and command[1] == "Lower":
        emails.make_lower()
    elif command[0] == "GetDomain":
        emails.get_domain(int(command[1]))
    elif command[0] == "GetUsername":
        emails.get_username()
    elif command[0] == "Replace":
        emails.replace(command[1])
    elif command[0] == "Encrypt":
        emails.encrypt()

    command = input().split()