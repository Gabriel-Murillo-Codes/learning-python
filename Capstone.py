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
if len(transactions) != 0:   
    print("Count of transactions:", len(transactions))
    print("Total of all transactions:", sum(transactions))
    print("The biggest transaction:", max(transactions))
    print("The smallest transaction:", min(transactions))
    print("The transactions sorted low to high:", sorted(transactions))
    print("Large transactions combined:", large)
    print("Medium transactions combined:", medium)
    print("Small transactions combined:", small)
    print("Unsorted transactions:", transactions)
    for transaction in transactions:
        print("Transaction:", transaction)
else:
    print("Nothing entered. ")