#Variables - Strings
firstname = "stux" # creating a string variable
secondname = "rypt" # creating a second one
fullname = firstname+" "+secondname #putting both variables together with a space between them
print ("My full name is "+fullname) # prints my full name

#Variables - Integers
age = 16 # making an age int
birthday = 12 # making a birthday int
print ("Your age is "+str(age)+" The day you were born is "+str(birthday)) #printing both together


#Variables - Floats
height = 5.7
grandpaheight = -5.7

# Variables - Usage 

print ("My full name is "+fullname) # adding strings together
print ("Your age is "+str(age)+" The day you were born is "+str(birthday)) #adding ints together
print("Your grandpa is "+str(grandpaheight)+" and you are "+str(height)+" feet") # adding floats together

##################################################################################################################################################################
# The reason i use str() is essentially you are adding the variables together and python is mathematical you can't just add words to numbers and numbers to words#
# so, you have to tell python to turn the variable into a string and add it to the others that way. Same could go with int or float which i will display         #
##################################################################################################################################################################
thisstringisanumber = "21"
print (24 + int(thisstringisanumber))

#this could also happen in list, (go to list.py for more info on that) for example:
numbers = [1, 2, 3]
userinput = int(input("which number in the list would you like to see?"))

if userinput == 0:
    print (numbers[0])
# the reason this happens is input just assumes what you are inputting is a string. 

# Now how do you make sure?
print (type(firstname))
#using type you can determine what type your variable is to avoid confusion.


age, birthday = 15, 12 # assinging multiple numbers to multiple variables on the same line.
print (age, birthday)





