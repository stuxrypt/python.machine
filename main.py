import colorama
from colorama import Fore, Back, Style

userinput = input("Input what would you like to learn today?\n")

if userinput == "data types":
    print (Fore.RED + Back.WHITE + "DATA TYPES")
    print(Style.RESET_ALL)
    a = input("Okay, what is your name?\n")
    b = int(input("How old are you?\n"))
    c = float(input("What is your exact height? (with decimals)\n"))
    d = bool (input("Are you a human? (Answer TRUE or FALSE)\n"))
    print ("\n")
    print ("Okay now we know your name is", Fore.GREEN + a + Style.RESET_ALL,"we call that a string a bunch of words put together or one word make up a string,\nNow you are", Fore.GREEN + str(b) + Style.RESET_ALL,"years old, that is an integer or int its simply a whole number,\nNext.. your height is", Fore.GREEN + str(c) + Style.RESET_ALL,"we call this a float, something the dumb int can't do it shows you the exact number with decimals..\nLastly is the TRUE FALSE statement which you answered to,", Fore.GREEN + str(d) + Style.RESET_ALL,"This is called a bool or a boolean and its simply TRUE or FALSE statements." )
    print ("\n")
    userinput = input("Was this helpful? (y/n) \n")
    if userinput == "y":
        print(Fore.GREEN + "Great!, if you would like to submit a feedback open an issue in github.com/stuxrypt/python.machine !")
    else:
        print(Fore.RED + "Oh no! I have made an extra script with comments and more explaining if you didn't understand, refer to variables-full.py\nIf you would like to submit a feedback open an issue in github.com/stuxrypt/python.machine I promise i will listen, the code might not be the best but I'm just starting out with projects.")

if userinput == "operators":
    userinput = input("operators with int, str, list, float or all in one? \n")
    print("\n")
    
    if userinput == "int" or userinput == "integer" or userinput == "integers":
        print("So if you know anything about math you probably remember the basic ops, I'm talking", Fore.RED + "multiplication" + Style.RESET_ALL ,Fore.CYAN + "division" + Style.RESET_ALL,Fore.GREEN + "subtracting" + Style.RESET_ALL,Fore.MAGENTA + "adding" + Style.RESET_ALL, "basic stuff,\nSo, let's start with", Fore.RED + "multiplication" + Style.RESET_ALL ,"How do you multiply an integer? Well it's so simple assuming a and b are integers it will go like:", Fore.RED + "print(a * b)" + Style.RESET_ALL,"and that will print the result.\nNow how about",Fore.CYAN + "division" + Style.RESET_ALL,"well it will go as simple as:",Fore.CYAN + "print(a / b)" + Style.RESET_ALL,"\nNext is",Fore.GREEN + "subtracting" + Style.RESET_ALL,"and you know the drill:",Fore.GREEN + "print(a - b)" + Style.RESET_ALL,"\nFinally, it's",Fore.MAGENTA + "adding" + Style.RESET_ALL,"and it goes:",Fore.MAGENTA + "print(a + b)" + Style.RESET_ALL,)
        userinput = input(Fore.LIGHTCYAN_EX + "\n\nvery very simple stuff, was this helpful? (y/n)" + Style.RESET_ALL)
        if userinput == "y":
            print(Fore.GREEN + "Great!, if you would like to submit a feedback open an issue in github.com/stuxrypt/python.machine !")
        else:
            print(Fore.RED + "Oh no! I have made an extra script with comments and more explaining if you didn't understand, refer to operators.py\nIf you would like to submit a feedback open an issue in github.com/stuxrypt/python.machine I promise i will listen, the code might not be the best but I'm just starting out with projects.")
    
    if userinput == "str" or userinput == "string" or userinput == "strings":
        print ("Actually strings are quite similiar to integers except you obviously can not multiply them together or devide them, you can multiply them with other numbers tho,\nSo the operations we will use are only:", Fore.RED + "multiplication" + Style.RESET_ALL, "and" ,Fore.MAGENTA + "adding" + Style.RESET_ALL,"\nLet's start with",Fore.MAGENTA + "adding" + Style.RESET_ALL,"considering we have a string inside the variable string, it goes as simple as:",Fore.MAGENTA + "print(string + 'hi')" + Style.RESET_ALL,"And that adds another text to it.\nNow,", Fore.RED + "multiplication" + Style.RESET_ALL ,"it's just like strings but it will print the same string multiple times:", Fore.RED + "print(string * 3)" + Style.RESET_ALL ," .")
        userinput = input(Fore.LIGHTCYAN_EX + "\n\nvery very simple stuff, was this helpful? (y/n)" + Style.RESET_ALL)
        if userinput == "y":
            print(Fore.GREEN + "Great!, if you would like to submit a feedback open an issue in github.com/stuxrypt/python.machine !")
        else:
            print(Fore.RED + "Oh no! I have made an extra script with comments and more explaining if you didn't understand, refer to operators.py\nIf you would like to submit a feedback open an issue in github.com/stuxrypt/python.machine I promise i will listen, the code might not be the best but I'm just starting out with projects.")
   
    if userinput == "list" or userinput == "list":
        print("We are going to use", Fore.MAGENTA + "adding" + Style.RESET_ALL, "and" , Fore.RED + "multiplying" + Style.RESET_ALL, "for the lists, so\nLet's start with", Fore.MAGENTA+ "adding" + Style.RESET_ALL,"it's done the same way as any other datatype:", Fore.MAGENTA + "print(odd + even)" + Style.RESET_ALL, "\nNow", Fore.RED + "multiplying" + Style.RESET_ALL, "also goes same way as any other datatype,", Fore.RED + "print(odd * even)" + Style.RESET_ALL )
        userinput = input(Fore.LIGHTCYAN_EX + "\n\nvery very simple stuff, was this helpful? (y/n)" + Style.RESET_ALL)
        if userinput == "y":
            print(Fore.GREEN + "Great!, if you would like to submit a feedback open an issue in github.com/stuxrypt/python.machine !")
        else:
            print(Fore.RED + "Oh no! I have made an extra script with comments and more explaining if you didn't understand, refer to operators.py\nIf you would like to submit a feedback open an issue in github.com/stuxrypt/python.machine I promise i will listen, the code might not be the best but I'm just starting out with projects.")
    
    if userinput == "float" or userinput == "floats":
        print ("Okay, so floats are exactly the same as integers when used with operators you can go to the integer tutorial or stick here, we will use", Fore.RED + "multiplication" + Style.RESET_ALL, Fore.CYAN + "division" + Style.RESET_ALL, Fore.GREEN + "subtracting" + Style.RESET_ALL, "and", Fore.MAGENTA + "adding" + Style.RESET_ALL, "all this normal stuff,\nLet's start with", Fore.RED + "multiplication" + Style.RESET_ALL, "assuming x and y store floats it will go like:", Fore.RED + "print(x * y)" + Style.RESET_ALL, "\nSecond is", Fore.CYAN + "division" + Style.RESET_ALL, "and it would go like:", Fore.CYAN + "print (x / y)" + Style.RESET_ALL,"\nAfter this is", Fore.GREEN + "subtracting" + Style.RESET_ALL, "it's as easy as the others, would go like:", Fore.GREEN + "print(x - y)" + Style.RESET_ALL, "\nLastly is", Fore.MAGENTA + "adding" + Style.RESET_ALL, "it goes like:", Fore.MAGENTA + "print(x + y)" + Style.RESET_ALL)
        userinput = input(Fore.LIGHTCYAN_EX + "\n\nvery very simple stuff, was this helpful? (y/n)" + Style.RESET_ALL)
        if userinput == "y":
            print(Fore.GREEN + "Great!, if you would like to submit a feedback open an issue in github.com/stuxrypt/python.machine !")
        else:
            print(Fore.RED + "Oh no! I have made an extra script with comments and more explaining if you didn't understand, refer to operators.py\nIf you would like to submit a feedback open an issue in github.com/stuxrypt/python.machine I promise i will listen, the code might not be the best but I'm just starting out with projects.")
    
    if userinput == "all" or userinput == "all in one":
        print("Okay, I will explain how", Fore.RED + "integers" +Style.RESET_ALL, Fore.GREEN + "strings" + Style.RESET_ALL, Fore.CYAN + "lists" + Style.RESET_ALL, "and", Fore.MAGENTA + "floats" + Style.RESET_ALL, "work,")
        print("\n")
        print(Fore.RED + "INTEGERS" + Style.RESET_ALL)
        print("So if you know anything about math you probably remember the basic ops, I'm talking", Fore.RED + "multiplication" + Style.RESET_ALL ,Fore.CYAN + "division" + Style.RESET_ALL,Fore.GREEN + "subtracting" + Style.RESET_ALL,Fore.MAGENTA + "adding" + Style.RESET_ALL, "basic stuff,\nSo, let's start with", Fore.RED + "multiplication" + Style.RESET_ALL ,"How do you multiply an integer? Well it's so simple assuming a and b are integers it will go like:", Fore.RED + "print(a * b)" + Style.RESET_ALL,"and that will print the result.\nNow how about",Fore.CYAN + "division" + Style.RESET_ALL,"well it will go as simple as:",Fore.CYAN + "print(a / b)" + Style.RESET_ALL,"\nNext is",Fore.GREEN + "subtracting" + Style.RESET_ALL,"and you know the drill:",Fore.GREEN + "print(a - b)" + Style.RESET_ALL,"\nFinally, it's",Fore.MAGENTA + "adding" + Style.RESET_ALL,"and it goes:",Fore.MAGENTA + "print(a + b)" + Style.RESET_ALL,)
        print("\n \n")
        print(Fore.GREEN + "STRINGS" + Style.RESET_ALL)
        print ("Actually strings are quite similiar to integers except you obviously can not multiply them together or devide them, you can multiply them with other numbers tho,\nSo the operations we will use are only:", Fore.RED + "multiplication" + Style.RESET_ALL, "and" ,Fore.MAGENTA + "adding" + Style.RESET_ALL,"\nLet's start with",Fore.MAGENTA + "adding" + Style.RESET_ALL,"considering we have a string inside the variable string, it goes as simple as:",Fore.MAGENTA + "print(string + 'hi')" + Style.RESET_ALL,"And that adds another text to it.\nNow,", Fore.RED + "multiplication" + Style.RESET_ALL ,"it's just like strings but it will print the same string multiple times:", Fore.RED + "print(string * 3)" + Style.RESET_ALL ," .")
        print("\n \n")
        print(Fore.CYAN + "LISTS" + Style.RESET_ALL)
        print("We are going to use", Fore.MAGENTA + "adding" + Style.RESET_ALL, "and" , Fore.RED + "multiplying" + Style.RESET_ALL, "for the lists, so\nLet's start with", Fore.MAGENTA+ "adding" + Style.RESET_ALL,"it's done the same way as any other datatype:", Fore.MAGENTA + "print(odd + even)" + Style.RESET_ALL, "\nNow", Fore.RED + "multiplying" + Style.RESET_ALL, "also goes same way as any other datatype,", Fore.RED + "print(odd * even)" + Style.RESET_ALL )
        print("\n \n")
        print(Fore.MAGENTA + "FLOATS" + Style.RESET_ALL)
        print ("Okay, so floats are exactly the same as integers when used with operators you can go up and read othe integer tutorial or stick here, we will use", Fore.RED + "multiplication" + Style.RESET_ALL, Fore.CYAN + "division" + Style.RESET_ALL, Fore.GREEN + "subtracting" + Style.RESET_ALL, "and", Fore.MAGENTA + "adding" + Style.RESET_ALL, "all this normal stuff,\nLet's start with", Fore.RED + "multiplication" + Style.RESET_ALL, "assuming x and y store floats it will go like:", Fore.RED + "print(x * y)" + Style.RESET_ALL, "\nSecond is", Fore.CYAN + "division" + Style.RESET_ALL, "and it would go like:", Fore.CYAN + "print (x / y)" + Style.RESET_ALL,"\nAfter this is", Fore.GREEN + "subtracting" + Style.RESET_ALL, "it's as easy as the others, would go like:", Fore.GREEN + "print(x - y)" + Style.RESET_ALL, "\nLastly is", Fore.MAGENTA + "adding" + Style.RESET_ALL, "it goes like:", Fore.MAGENTA + "print(x + y)" + Style.RESET_ALL)
        userinput = input(Fore.LIGHTCYAN_EX + "\n\nvery very simple stuff, was this helpful? (y/n)" + Style.RESET_ALL)
        if userinput == "y":
            print(Fore.GREEN + "Great!, if you would like to submit a feedback open an issue in github.com/stuxrypt/python.machine !")
        else:
            print(Fore.RED + "Oh no! I have made an extra script with comments and more explaining if you didn't understand, refer to operators.py\nIf you would like to submit a feedback open an issue in github.com/stuxrypt/python.machine I promise i will listen, the code might not be the best but I'm just starting out with projects.")
