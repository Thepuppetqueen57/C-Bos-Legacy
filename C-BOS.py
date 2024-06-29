import time
import subprocess
from libs import cboslib
import ctypes
import colorama
import requests
import base64
import sys
import re
try:
    import prompt_toolkit
except ImportError:
    print("Installing package \"prompt_toolkit\"")
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "prompt_toolkit"])
    cboslib.clear_console()
    import prompt_toolkit

cboslib.set_title()
cboslib.clear_console()

print(cboslib.randomstringcolor("Checking for updates..."))
time.sleep(0.3)
print(cboslib.randomstringcolor("Booting C-Bos The useless Command Line App"))
time.sleep(0.3)
print(cboslib.randomstringcolor("Loading user data..."))
time.sleep(0.25)
print(cboslib.randomstringcolor("Loading files..."))
time.sleep(0.1)
print(cboslib.randomstringcolor("C-Bos essentials library loaded"))
time.sleep(0.15)
print(cboslib.randomstringcolor("Done!"))
time.sleep(0.3)

print(
    cboslib.randomstringcolor(
        f"Welcome to C-Bos Legacy user!\nType \"help\" for a list of commands."
    ))
print(cboslib.randomstringcolor("Commands are no longer case sensitive btw!!"))
while True:
    # ok so basically, instead of capitalizing in a lowercmd == "" thingy, you can do lowercase, if you dont do lowercase it will break. the .lower() is to make it so it will work with all cases
    cmd = input(colorama.Fore.YELLOW + "> " + colorama.Fore.RESET)
    lowercmd = cmd.lower()
    if lowercmd == "run test":
        print("It is workin!")
    elif lowercmd == "shut down" or lowercmd == "turn off" or lowercmd == "turn off c-bos" or lowercmd == "exit":
        print("Shutting Down...")
        time.sleep(2)
        sys.exit(1)
    elif lowercmd == "send uwu to cj":
        # I DIDNT NOTICE YOU REMOVED THIS LMAOOO
        print("This command has been fucking destroyed")
    elif lowercmd == "hi" or lowercmd == "hello":
        print(f"{cmd}!")
    elif lowercmd == "help" or lowercmd == "what can i do?":
        print("Here is a list of commands:")
        time.sleep(0.1)
        print("1: Run test")
        time.sleep(0.1)
        print("2: Shut down")
        time.sleep(0.1)
        print("3: Send OWO to cj")
        time.sleep(0.1)
        print("4: Run backup systems. It ain't do anythin btw")
        time.sleep(0.1)
        print("5: Hi")
        time.sleep(0.1)
        print("6: Relogin")
        time.sleep(0.1)
        print("7: Make file")
        time.sleep(0.1)
        print("8: Open file")
        time.sleep(0.1)
        print("9: Echo")
        time.sleep(0.1)
        print("10: Factorial")
        time.sleep(0.1)
        print("11: Add 1 number to another")
        time.sleep(0.1)
        print("12: Guide")
        time.sleep(0.1)
        print("13: List of C-Bos programs")
        time.sleep(0.1)
        print("14: Crash")
        time.sleep(0.1)
        print("15: What is the best theme?")
        time.sleep(0.1)
        print("16: Break")
        time.sleep(0.1)
        print("17: Clear")
        time.sleep(0.1)
        print("18: New line")
        time.sleep(0.1)
        print("19: Subtraction")
        time.sleep(0.1)
        print("20: Multiplication")
        time.sleep(0.1)
        print("21: Division")
        time.sleep(0.1)
        print("22: What is the current version?")
        time.sleep(0.1)
        print("23: Flip the table")
        time.sleep(0.1)
        print("24: Fix the table")
        time.sleep(0.1)
        print("25: Change window title")
        time.sleep(0.1)
        print("26: Change text color")
        time.sleep(0.1)
        print("27: Reset text color")
        time.sleep(0.1)
        print("28: Reset title")
        time.sleep(0.1)
        print("29: Kill cbos")
        time.sleep(0.1)
        print("30: Exit the loop")
        time.sleep(0.1)
        print("31: Assign a var")
        time.sleep(0.1)
        print(
            "32: Print new var (must be ran only after assign a var has been ran)"
        )
        time.sleep(0.1)
        print(
            "33: Get package (go to http://tps.puppet57.site/cbos/packagelist for a list of packages. Then take the name of the package minus the file extension and paste it in)"
        )
        time.sleep(0.1)
        print(
            "34: Run (Enter the name of a package you installed or a built in package also you don't have to put the file extension it will always be .py)"
        )
        time.sleep(0.1)
        print(
            "35: Base64 encode (Encodes a base64 string. Useless but why not. This entire program is useless.)"
        )
        time.sleep(0.1)
        print(
            "36: Base64 decode (Decodes a base64 string. Useless but why not. This entire program is useless.)"
        )
        time.sleep(0.1)
        print("37: Check version (Checks if there is an update for cbos)")
        time.sleep(0.1)
        print(
            "38: Edit server text (Edits a text file on the server to whatever you want)"
        )
        time.sleep(0.1)
        print(
            "39: Get server text (Gets the text from a text file on the server)"
        )
        time.sleep(0.1)
        print("40: Make bio (Adds text to a db under your user)")
        time.sleep(0.1)
        print("41: Get bio (Gets a users bio)")
        time.sleep(0.1)
        print(
            "42: Get admin text (Like get server text but it gets text from a txt file only admins can edit)"
        )
        print("Btw I removed a bunch of useless commands but I couldnt be bothered to remove them from the cmd list")
        print("So yeah cj can deal with that one")
    elif cmd.replace(" ", "") == "":
        pass
    elif lowercmd == "make file" or lowercmd == "create file":
        name = input("file name:")
        file = open(name, "w")
    elif lowercmd == "open file":
        name = input("file name:")
        file = open(name)
        print(file.read())
    elif lowercmd.startswith("echo "):
        print(re.sub(r"(?i)^echo ", "", cmd))
    elif lowercmd == "echo":
        print(f"Run {cmd} with \"{cmd} {{string to echo}}\"")
    elif lowercmd == "run":
        ope = input("file: ")
        subprocess.Popen(f"{ope}.py", shell=True)
    elif lowercmd == "addition":
        num1 = float(input("Enter the first number: "))
        print("Processing number..")
        time.sleep(0.6)
        print("Done!")
        num2 = float(input("Enter the second number: "))
        print("Processing number..")
        time.sleep(0.6)
        print("Done!")
        result = num1 + num2
        print("Your result is: ", result)
    elif lowercmd == "guide to using c-bos" or lowercmd == "guide" or lowercmd == "guide to using cbos":
        print("First of all commands start with a capital letter.")
        print(
            "Second of all C-Bos is open source so just hop in the (C-BOS.py) file and start changing/adding/removing stuff (if you know how to code in python)"
        )
        print(
            "Third of all python is really ez to code in so search up a tutorial on youtube or sum idk."
        )
    elif lowercmd == "crash" or lowercmd == "instant shut down":
        sys.exit(1)
    elif lowercmd == "break" or lowercmd == "break c-bos":
        print("BET")
        print("It will take 4645456 seconds to fix again...")
        time.sleep(4645456)
        print("Done!")
        print("You can use C-Bos normally again!")
    elif lowercmd == "clear" or lowercmd == "clear log" or lowercmd == "clear logs":
        cboslib.clear_console()
    elif lowercmd == "subtraction":  # ik for a FACT you used 1 - 1 lmao
        num1sub = float(input("Enter the first number: "))
        print("Processing number..")
        time.sleep(0.6)
        print("Done!")
        num2sub = float(input("Enter the second number: "))
        print("Processing number..")
        time.sleep(0.6)
        print("Done!")
        resultsub = num1sub - num2sub
        print("Your result is: ", resultsub)
    elif lowercmd == "multiplication":
        num1mult = float(input("Enter the first number: "))
        print("Processing number..")
        time.sleep(0.6)
        print("Done!")
        num2mult = float(input("Enter the second number: "))
        print("Processing number..")
        time.sleep(0.6)
        print("Done!")
        resultmult = num1mult * num2mult
        print("Your result is: ", resultmult)
    elif lowercmd == "division":
        num1divi = float(input("Enter the first number: "))
        print("Processing number..")
        time.sleep(0.6)
        print("Done!")
        num2divi = float(input("Enter the second number: "))
        print("Processing number..")
        time.sleep(0.6)
        print("Done!")
        resultdivi = num1divi / num2divi
        print("Your result is: ", resultdivi)
    elif lowercmd == "what is the current version?":
        print(f"C-Bos legacy")
        time.sleep(1)
        print("There is no longer a version number for cbos legacy. Just cbos legacy lol.")
    elif lowercmd == "cbos fans" or lowercmd == "c-bos fans" or lowercmd == "drugs":
        print(cmd, "are cool!")
    elif lowercmd == "flip the table" or lowercmd == "flip le table":
        print("ok (╯°□°)╯︵ ┻━┻")
    elif lowercmd == "fix the table" or lowercmd == "fix le table":
        print("Fiiine ugh ┬─┬ノ( º _ ºノ)")
    elif lowercmd == "change window title" or lowercmd == "change title":
        windowtitleinput = input("New window title: ")
        ctypes.windll.kernel32.SetConsoleTitleW(windowtitleinput)
    elif lowercmd == "change text color":
        print(
            "Okay! This command only works with iPython and the VS-Code console"
        )
        print("And probably other alternatives.")
        ChangeTextColorInput = input("Which color?: ")
        if ChangeTextColorInput == "Green" or ChangeTextColorInput == "green":
            print(colorama.Fore.GREEN +
                  "Every piece of text will now be green")
        elif ChangeTextColorInput == "Red" or ChangeTextColorInput == "red":
            print(colorama.Fore.RED + "Every piece of text will now be red")
        elif ChangeTextColorInput == "Reset" or ChangeTextColorInput == "reset" or ChangeTextColorInput == "White" or ChangeTextColorInput == "white":
            print(colorama.Fore.RESET +
                  "Every piece of text will now be normal")
        elif ChangeTextColorInput == "Blue" or ChangeTextColorInput == "blue":
            print(colorama.Fore.BLUE + "Every piece of text will now be blue")
        elif ChangeTextColorInput == "Black" or ChangeTextColorInput == "black":
            print(colorama.Fore.BLACK +
                  "Every piece of text will now be black")
        else:
            print(
                f"{ChangeTextColorInput} is not a valid color. Run the command again"
            )
    elif lowercmd == "reset color" or lowercmd == "reset text" or lowercmd == "reset text color":
        print(colorama.Fore.RESET + "Every piece of text will now be normal")
    elif lowercmd == "reset window title" or lowercmd == "reset title":
        cboslib.clear_console()
    elif lowercmd == "reset title and color" or lowercmd == "reset color and title":
        cboslib.clear_console()
        print(colorama.Fore.RESET + "Done!")
    elif lowercmd == "what are you doing right now?" or lowercmd == "what are u doing rn?" or lowercmd == "what are you doing rn?":
        print(
            "Well while writing this I am coding C-Bos while listening to music :D"
        )

    elif lowercmd == "how do i look in the c-bos code" or lowercmd == "how do i look in the c-bos code?":
        print(
            "To look in the code you want to open the C-Bos.py file with either vs code or notepad or whatever you use"
        )
        print(
            'to make a custom command for c-bos you wanna type elif lowercmd == "these quotes can be anything")'
        )
        print(
            "These quotes can hold any message for the user to type and then when they type whats in the quotes the command runs"
        )
        print(
            "To add a function to the command lets say you wanna print hello world. Well 1 line below the elif you wanna type print('Hello world')"
        )
        print(
            "And thats how to add a command. For more in depth python watch a youtube tutorial"
        )


    elif lowercmd == "base64 encode":
        encoded_string = input("Enter the Base64 encoded string: ")
        encoded_bytes = base64.b64encode(encoded_string.encode('utf-8'))
        print("Encoded string:", encoded_bytes.decode('utf-8'))

    elif lowercmd == "base64 decode":
        encoded_string = input("Enter the Base64 encoded string: ")
        print("Decoded string:", base64.b64decode(encoded_string))

    elif lowercmd == "edit server text":
        response = requests.get(
            'https://tps.puppet57.site/cbos/backend/getText.php')
        currenttext = response.json().get("text", "")

        servertextinput = prompt_toolkit.prompt("Change text to: ", default=currenttext)
        response = requests.post(
            'https://tps.puppet57.site/cbos/backend/editText.php',
            data={'text': servertextinput})
        print(response.json().get("response", "No server response found"))

    elif lowercmd == "get server text":
        response = requests.get(
            'https://tps.puppet57.site/cbos/backend/getText.php')
        print(response.json().get("response", "No server response found"))



    else:
        print(f"The command \"{cmd}\" is stupid! Please try again.")