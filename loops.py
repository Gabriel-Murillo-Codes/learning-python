large = 0
medium = 0
small = 0
transactions = input("Enter all of your transactions here. When finished type done. ")
while transactions != ("done"):
    try:
        amount = float(transactions)
    except ValueError:
        print("That wasn't a valid number. Try again. ")
        transactions = input("Enter all of your transactions here. When finished type done. ")
        continue
    if amount >= 100:
        large = large + amount
    elif amount >= 20:
        medium = medium + amount
    elif amount >= 0:
        small = small + amount
    else: 
        print("A transaction can not be a negative number. ")
    transactions = input("Enter all of your transactions here. When finished type done. ")
print(large)
print(medium)
print(small)