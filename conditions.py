# first we will make an int variable

age = 21

print (age == 13)
# This will print out a FALSE statement, because we simply ask python to check if the age is 13 which it's not
print (age == 21)
# Now here it will be true because the age is infact 21

print (age < 3)

# This asks the question is age smaller than 3? No it's not it's 21 so it will print out FALSE

print (age > 3)

# And this asks if age is bigger than 3, which it is, so it will print out TRUE

print (age >= 10)

# Is age bigger or equal to 10? Yes it's bigger

print (age != 21)

# Is age not equal 21? FALSE, it is

names = ["john", "casey", "ven"]
name = "puta"

print ("john" in name)

# This asks if john is in the names list, which it is, so it's TRUE

# Now let's start using if statements for more flexibility

# IN OPERATOR

if "john" in names:
    print ("putaaaa")

# if the string john is in the list then print putaaaa

# OR OPERATOR

if "walter" in names or "walt" in names:
    print ("Yeah that's my friend")
else:
    print ("IDK HIM")

# Now we used "or" condition , if either of them is TRUE it will print "Yeah that's my friend" otherwise "IDK HIM"

# AND OPERATOR

if "john" in names and "casey" in names:
    print("Yeah ik them.")
else:
    print ("Idk both or one of them")

# Now we used "and" condition, both statements have to be TRUE in order to print "Yeah ik them" otherwise it will get passed to the else statement.

# IS OPERATOR

a = "c"
b = "b"
c = "c"

print (a == c)
print (a is c)

# First one will print out TRUE because they have the same value, however the is operator doesn't work this way it checks if two objects are referring to the same memory location, so if they are not identical objects it will print out FALSE, i know this might sound complicated 
# but think of it this way, if you say a = b and ask if a is b it will print out TRUE because you have told python they are both the same, doesn't matter if they have the same value, they should both refer to the same location in order to be TRUE.

k = False

if not k :
    print ("k is false")

# The not operation makes the opposite of something so if you have a False statement it will invert it to True, keep in mind "k is false will print" because i asked python to print it if k is true which it was after the not operator inverted it.


#Which is why if k is true as im going to show:
k = True

if not k:
    print("k is false")
else:
    print("k is true")
# It gets passed to else