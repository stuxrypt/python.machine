a = 5
b = 5
op = None
result = None
userinput = None


# Creating a simple number calculator to show operators

a = int(input("What is the first number\n"))
op = input("What is the operation\n")
b = int(input("What is the second number\n"))

if op == "*":
    result = a * b
    print(a, " * ", b, " = ", result)

if op == "%":
    result = a % b
    print(a, " % ", b, " = ", result)

if op == "-":
    result = a - b
    print(a, " - ", b, " = ", result)

if op == "+":
    result = a + b
    print(a, " + ", b, " = ", result)

if op == "**":
    result = a ** b
    print(a, " ** ", b, " = ", result)

# Creating a string calculator (cause it works too)

a = input("What's the string?\n")
op = input("What's the operation\n")
b = input("What's the number/second string\n")

if op == "+":
    if type(b) == str:
        result = a + b
        print (a, " + ", b, " = ", result)
if op == "*":
    if type(b) == int:
        result = a * b
        print (result)
    elif type(b) == str:
        print ("You cant multiple strings together dumbass")
    else:
        print("Invalid")

# Using lists too

odd = [1, 3, 5, 7, 9]
even =[2, 4, 6, 8, 10]

userinput = input("What would you like to do with the odd and even lists?")

if userinput == "+":
    result = odd + even
    print ("The two lists added together are: ", result)

if userinput == "*":
    a = input ("Which list do you choose?\n")
    if a == "odd":
        b = int(input("what number would you like to multiply it by?\n"))
        result = odd * b
        print (result)
    if a == "even":
        b = int(input("what number would you like to multiply it by?\n"))
        result = even * b
        print (result)

