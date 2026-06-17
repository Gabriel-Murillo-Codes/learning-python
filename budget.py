budget = float(input("How much money do you have? "))
spend = float(input("How much money do you want to spend? "))
left = budget - spend
if left >= 500:
    print(left, "Enough money with plenty to spare. ")
elif left >= 0:
    print(left, "Just barely enough. ")
else:
    print(left, "Not enough. ")