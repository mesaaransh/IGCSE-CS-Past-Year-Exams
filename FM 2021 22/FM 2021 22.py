table = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
import random

multiplier = (random.randint(1, 12))

score = 0

print()
print("Enter name")
name = str(input("Enter name():"))

print()
print("Enter Table")
table_select = int(input("Enter table():"))

if (table_select) in (table):
    print()
    print(table_select, "*", multiplier)

else:
    print("table unavailable")

print()
print("Enter answer")
answer = int(input("Enter answer():"))

if answer == (table_select * multiplier):
    print(name + " Well Done")
    score = score + 1

else:
    print(name + " Sorry it is Incorrect")
    score = score