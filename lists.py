transactions = []
large = 0
medium = 0
small = 0
entry = input("Enter all of your transactions here. When finished type done. ")
while entry != ("done"):
    try:
        amount = float(entry)
    except ValueError:
        print("That wasn't a valid number. Try again. ")
        entry = input("Enter all of your transactions here. When finished type done. ")
        continue
    if amount >= 100:
        transactions.append(amount)
        large = large + amount
    elif amount >= 20:
        transactions.append(amount)
        medium = medium + amount
    elif amount >= 0:
        transactions.append(amount)
        small = small + amount
    else: 
        print("A transaction can not be a negative number. ")
    entry = input("Enter all of your transactions here. When finished type done. ")
print(large)
print(medium)
print(small)
print(transactions)
for transaction in transactions:
    print("Transaction:", transaction)