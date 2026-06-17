#count = 0
#while count < 5:
    #print(count)
    #count = count + 1
#amount in [10, 20, 30]:
    #print(amount)

#for i in range(5):
    #print(i)
#--------------------------------------
#total = 0
#for amount in [12.50, 8.99, 45.00, 3.25]:
    #print(amount)
    #total = total + amount
#print(total)
#---------------------------------------
#total = 0
#transaction_amount = input("Enter all of your transactions. When finished type done. ")
#while transaction_amount != ("done"):
#    total = total + float(transaction_amount)
#    transaction_amount = input("Enter all of your transactions. When finished type done. ")
#print(total)
#----------------------------------------
#Code breaks with non-numeric input / fix later.
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