name = input("What's your name? ")
print("Hello, " + name + ", Let's get to work.")
age = int(input("What is ur age? "))
print("Your age is... ", age)
next_year = age + 1
print("Next year you will be", next_year)
if age >= 18:
    print("You can enlist on your own. ")
elif age >= 17:
    print("You can enlist with a parent's signature. ")
else:
    print("You are too young to enlist. ")
if age >= 17 and age <= 21:
    print("Prime age for a West Point appointment")