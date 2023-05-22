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
        print(Fore.RED + "Oh no! if you would like to submit a feedback open an issue in github.com/stuxrypt/python.machine I promise i will listen, the code might not be the best but I'm just starting out with projects.. !")

