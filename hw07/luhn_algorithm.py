account_number = list(input("Enter your account number:\n"))
length = len(account_number)
sum = 0

for _ in range(length):
    account_number[_] = int(account_number[_])
    if _ in range(length-2, -1, -2):
        doubled = 2*account_number[_]
        account_number[_] = doubled % 10 + doubled//10
    sum += account_number[_]

if (account_number) and (sum % 10 == 0):
    print("The account number is valid!")
else:
    print("The account number is not valid.")
