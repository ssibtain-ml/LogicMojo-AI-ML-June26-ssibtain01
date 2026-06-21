print("hello")

a = int(input("Rent: "))
b = int(input("Groceries: "))
c = int(input("Utilities: "))
d = int(input("Commute: "))
print("Total Expense: " + str(a+b+c+d))

strName = input("Emp Name?: ")
intScore = int(input("Emp Score?: "))

if intScore < 33:
    print("sorry you failed")
elif intScore >= 33 and intScore <= 60:
    print("satisfactory")
elif intScore > 60 and intScore <= 70:
    print("good")
elif intScore > 70 and intScore <= 100:
    print("excellent")
else:
    print("invalid input")
