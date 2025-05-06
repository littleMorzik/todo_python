password = input("Enter a password: ")

result = {}

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

is_digit = False
is_upper = False

for i in password:
    if i.isdigit():
        is_digit = True

    if i.isupper():
        is_upper = True

result["digit"] = is_digit
result["upper"] = is_upper

if all(result.values()):
    print("Strong password!")
else:
    print("Weak password!")
