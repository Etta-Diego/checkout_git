# Make a simple calculator

# First we declare our variables

# Then the we implement them

num1, operator, num2 = input("Enter Numbers: ").split()

num1 = int(num1)
num2 = int(num2)

sum = num1 + num2

if operator == "+":
    print("{} + {} = {}".format(num1, num2, sum))

diference = num1 - num2
if operator == "-":
    print("{} - {} = {}".format(num1, num2, diference))

division = num1 / num2
if operator == "/":
    print("{} / {} = {}".format(num1, num2, division))


if operator == "*":
    print("{} - {} = {}".format(num1, num2, num1 * num2))


else:
    print("Try another sign")
