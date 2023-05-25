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
    print ("Okay now we know your name is", Fore.GREEN + a + Style.RESET_ALL,"we call that a string a bunch of words put together or one word make up a string,\n now you are", Fore.GREEN + str(b) + Style.RESET_ALL,"years old, that is an integer or int its simply a whole number,\n next.. your height is", Fore.GREEN + str(c) + Style.RESET_ALL,"we call this a float, something the dumb int can't do it shows you the exact number with decimals..\n lastly is the TRUE FALSE statement which you answered to,", Fore.GREEN + str(d) + Style.RESET_ALL,"This is called a bool or a boolean and its simply TRUE or FALSE statements." )
    print ("\n")
    useinput = input("Was this helpful? (y/n) \n")
    if userinput == "y":
        print(Fore.GREEN + "Great!, if you would like to submit a feedback open an issue in github.com/stuxrypt/python.machine !")
    else:
        print(Fore.RED + "Oh no! I have made an extra script with comments and more explaining if you didn't understand, refer to variables-full.py\n if you would like to submit a feedback open an issue in github.com/stuxrypt/python.machine I promise i will listen, the code might not be the best but I'm just starting out with projects.")

if userinput == "operators":
    userinput = input("operators with int, str list or all in one? \n")
    print("\n")
    if userinput == "int":
        print("So if you know anything about math you probably remember the basic ops, I'm talking", Fore.RED + "multiplication" + Style.RESET_ALL ,Fore.CYAN + "division" + Style.RESET_ALL,Fore.GREEN + "subtracting" + Style.RESET_ALL,Fore.MAGENTA + "adding" + Style.RESET_ALL, "basic stuff,\nSo, let's start with", Fore.RED + "multiplication" + Style.RESET_ALL ,"How do you multiply an integer? Well it's so simple assuming a and b are integers it will go like:", Fore.RED + "print(a * b)" + Style.RESET_ALL,"and that will print the result.\nNow how about",Fore.CYAN + "division" + Style.RESET_ALL,"well it will go as simple as:",Fore.CYAN + "print(a / b)" + Style.RESET_ALL,"\nNext is",Fore.GREEN + "subtracting" + Style.RESET_ALL,"and you know the drill:",Fore.GREEN + "print(a - b)" + Style.RESET_ALL,"\n Finally, it's",Fore.MAGENTA + "adding" + Style.RESET_ALL,"and it goes:",Fore.MAGENTA + "print(a + b)" + Style.RESET_ALL,)
        useinput("\n \n very very simple stuff, was this helpful? (y/n)")
        if userinput == "y":
        print(Fore.GREEN + "Great!, if you would like to submit a feedback open an issue in github.com/stuxrypt/python.machine !")
        else:
        print(Fore.RED + "Oh no! I have made an extra script with comments and more explaining if you didn't understand, refer to variables-full.py\n if you would like to submit a feedback open an issue in github.com/stuxrypt/python.machine I promise i will listen, the code might not be the best but I'm just starting out with projects.")
    if userinput == "str":
        print ("soon")