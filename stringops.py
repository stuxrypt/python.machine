teststring = "Hello there!"

# first string op you should learn in len which is simply the string character length

print("Test string is", len(teststring), "characters long")
print ("Test string 'T' is", teststring.index("t"), "characters away from the first character")
print ("Test string has", teststring.count("t"), "T(s)")
print ("Test string sliced from 3rd to 7th character is ", teststring[3:7])
print ("Test string printed out from the 3rd to the 7th character completely normally is", teststring[3:7])
print ("Test string reversed is ", teststring[::-1])
print("Test string all in upper characters is ", teststring.upper())
print("Test string all in upper characters is ", teststring.lower())
print("Does test string start with 'Hello'?", teststring.startswith("Hello"))
print("Does test string end with goodbye?", teststring.endswith("goodbye"))
print("Teststring space between Hello and there! could be split using ", teststring.split(" "))