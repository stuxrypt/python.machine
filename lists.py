numbers = [] #creating a list
numbers.append(1) #appending one number to the list
numbers.append(2) #appending the second
numbers.append(3)
print ("The first appended number in the numbers list is "+str(numbers[0])) #printing the first. (SHould be noted that python always starts with 0 not one)
print ("The second appended number in the numbers list is"+str(numbers[1])) # printing the second.

#Now lets assign that to a variable:
usernames = ["1337", "databreach", "unfortunate", "rare"]
first_username = usernames[0]
print ("The first username in the databreach list is "+first_username)


# making a basic databreach checker
userinput = str(input("which username would you like to check if its in the list?"))

if userinput in usernames:
    print ("The username ", userinput, " is in the list")
else:
    print ("Username not in the list.")




