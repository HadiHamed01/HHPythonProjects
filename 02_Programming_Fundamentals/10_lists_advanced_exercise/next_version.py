version = input()
version_int = version.replace(".", "")
version_integer = int(version_int) + 1
print(".".join(str(version_integer)))