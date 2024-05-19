import time
import subprocess
from libs import cboslib
import ctypes
import colorama
import requests
import base64
import pwinput
import webbrowser
import sys
import re
import random

# update this when there is a new cbos update
version = 4.0

cboslib.set_title()
cboslib.clear_console()

isAdmin = False
isNewAccount = False
username = input(cboslib.randomstringcolor("Username: "))
password = pwinput.pwinput(prompt=cboslib.randomstringcolor("Password: "))

cboslib.clear_console()

# dont move this as it will just cause issues
loggedin, isAdmin, isNewAccount, response = cboslib.login(username, password)
if not loggedin:
    cboslib.clear_console()
    print(cboslib.randomstringcolor(response))
    sys.exit(1)

cboslib.clear_console()

print(cboslib.randomstringcolor("Checking for updates..."))
# no need for time.sleep, it will take more than 250ms for the request to process anyways
print(cboslib.randomstringcolor(cboslib.check_version(version)))
time.sleep(0.3)
print(cboslib.randomstringcolor("Booting C-Bos The useless Command Line App"))
time.sleep(0.3)
print(cboslib.randomstringcolor("Loading user data..."))
time.sleep(0.25)
print(cboslib.randomstringcolor(
    "Password is valid... checking if it is a new account"))
time.sleep(0.25)
if isNewAccount:
    print(cboslib.randomstringcolor(
        "Account is new... skipping check for admin..."))
else:
    print(cboslib.randomstringcolor("Account is not new... checking if admin..."))
    time.sleep(0.1)
    if isAdmin:
        print(cboslib.randomstringcolor("Account is an admin..."))
    else:
        print(cboslib.randomstringcolor("Account is not an admin..."))
time.sleep(0.25)
print(cboslib.randomstringcolor("Loading files..."))
time.sleep(0.1)
print(cboslib.randomstringcolor("C-Bos essentials library loaded"))
time.sleep(0.15)
print(cboslib.randomstringcolor("Done!"))
time.sleep(0.3)

print(cboslib.randomstringcolor(
    f"Welcome to C-Bos Lite v{version}, {username}!\nType \"help\" for a list of commands."))
if isAdmin:
    print(cboslib.randomstringcolor(
        "You are a admin. Admin commands will be added soon!"))
print(cboslib.randomstringcolor("Commands are no longer case sensitive btw!!"))
cmdloop = True
while cmdloop:
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
    elif lowercmd == "run backup systems":
        print("Backup systems engaged...")
        time.sleep(2)
        print("Making backups of this pc...")
        time.sleep(1)
        print("We have to shut down your pc to make backups.")
        print("You can turn it back on immediatly after it shut's down")
        time.sleep(3)
        print("Shutting down...")
        time.sleep(3)
        sys.exit(1)
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
        print("32: Print new var (must be ran only after assign a var has been ran)")
        time.sleep(0.1)
        print("33: Get package (go to http://tps.puppet57.site/cbos/packagelist for a list of packages. Then take the name of the package minus the file extension and paste it in)")
        time.sleep(0.1)
        print("34: Run (Enter the name of a package you installed or a built in package also you don't have to put the file extension it will always be .py)")
        time.sleep(0.1)
        print("35: Base64 encode (Encodes a base64 string. Useless but why not. This entire program is useless.)")
        time.sleep(0.1)
        print("36: Base64 decode (Decodes a base64 string. Useless but why not. This entire program is useless.)")
        time.sleep(0.1)
        print("37: Check version (Checks if there is an update for cbos)")
        time.sleep(0.1)
        print("38: Edit server text (Edits a text file on the server to whatever you want)")
        time.sleep(0.1)
        print("39: Get server text (Gets the text from a text file on the server)")
        time.sleep(0.1)
        print("40: Make bio (Adds text to a db under your user)")
        time.sleep(0.1)
        print("41: Get bio (Gets a users bio)")
    elif lowercmd == "relogin" or lowercmd == "relog" or lowercmd == "logout":
        user = input("Newuser:")
        print(f"Now logged into {user}")
    elif lowercmd == "goodbye":
        for _ in range(15):
            print("Mistake")
        for _ in range(10):
            print("Help")
        print("৳₣₠៛₢૱៛৻¥₰৳₳₽﷼﷼﷼₶৳৳₪₰௹₠₳₺⨤⨑⨈⨅⨇⨇⨅⨋⨑")
        sys.exit(1)
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
    elif lowercmd == "they are coming":
        print("...")
        time.sleep(3)
        print("...")
        time.sleep(3)
    elif lowercmd == "bop bop boop dghjfgfhjkghjfghk devil e go i'm a scat maaaan":
        print("BEEP BOOP BOP BOOP BEEP BOP BOOP")
    elif lowercmd == "what is z-bos?":
        print("Z-Bos is a dev version of C-Bos and it only has a few commands for devs to start off on")
        print("It is for making different fan made versions of C-Bos")
        print(
            "Z-Bos is not maintained anymore but is available for download in the discord")
    elif lowercmd == "mto-os is better than you":
        print("HOW DARE YOU")
    elif lowercmd == "oh yes go faster":
        print("AYYYYYYYYYYYYYYYYYYYOOOOOOOOOOOOOOOOOOOO")
    elif lowercmd == "factorial":
        print("no")
    elif lowercmd == "reeeeee":
        print("EEEEEEE")
    elif lowercmd == "add 1 number to another":
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
    elif lowercmd == "hi there":
        print("BYE THERE")
        time.sleep(0.6)
        sys.exit(1)
    elif lowercmd == "uh" or lowercmd == "uhm":
        print("hmmm")
    elif lowercmd == "help me.. please" or lowercmd == "help me":
        print("no")
    elif lowercmd == "guide to using c-bos" or lowercmd == "guide" or lowercmd == "guide to using cbos":
        print("First of all commands start with a capital letter.")
        print("Second of all C-Bos is open source so just hop in the (C-BOS.py) file and start changing/adding/removing stuff (if you know how to code in python)")
        print("Third of all python is really ez to code in so search up a tutorial on youtube or sum idk.")
    elif lowercmd == "die":
        print("so mean :(")
    elif lowercmd == "give me a list of other c-bos programs" or lowercmd == "list of c-bos programs":
        print("Okay!")
        time.sleep(0.6)
        print("1: Notepad")
        print("2: Local web browser")
    elif lowercmd == "crash" or lowercmd == "instant shut down":
        sys.exit(1)
    elif lowercmd == "what is the best theme on any program?" or lowercmd == "what is the best theme?":
        print("dark mode don't argue or I will shoot you with a water pistol (in winter)")
    elif lowercmd == "break" or lowercmd == "break c-bos":
        print("BET")
        print("It will take 4645456 seconds to fix again...")
        time.sleep(4645456)
        print("Done!")
        print("You can use C-Bos normally again!")
    elif lowercmd == "i know who you are":
        print("...")
        time.sleep(2)
        print("No crap I am [SOMEONE YOU MAY KNOW]")
        time.sleep(1)
    elif lowercmd == "clear" or lowercmd == "clear log" or lowercmd == "clear logs":
        cboslib.clear_console()
    elif lowercmd == "i hate cbos":
        cmdloop = False
    elif lowercmd == "i love cbos":
        # print("good boy") #lets make them bigender, its 2024 afterall
        if random.randint(0, 1) == 0:
            print("good boy")
        else:
            print("good girl")
        time.sleep(2)
        print("...")
        time.sleep(1)
    elif lowercmd == "waaaa-" or lowercmd == "waaaa":
        print("wa")
    elif lowercmd == "make a new line" or lowercmd == "new line":
        print("")
    elif lowercmd == "gr" or lowercmd == "grr" or lowercmd == "grrr":
        print("AHH BEAR HELP")  # no thanks puppet
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
    elif lowercmd == "nut":
        print("uh...")
        time.sleep(3)
        print("HMMMMMMMM")
    elif lowercmd == "activate chatgpt":
        print("ok 👍")
        time.sleep(0.2)
        print("loading browser...")
        time.sleep(0.8)
        webbrowser.open("https://chat.openai.com/chat")
    elif lowercmd == "python":
        for i in range(15):
            print("python")
            time.sleep(0.1)
    elif lowercmd == "what is the current version?":
        print(f"C-Bos lite version {version}")
        time.sleep(1)
        print("You can update at the discord server if there is an update!")
        print("https://discord.gg/z9afNnvgyA")
        print("Check if there is an update either by restarting cbos or by using the check version command")
    elif lowercmd == "cbos fans" or lowercmd == "c-bos fans" or lowercmd == "drugs":
        print(cmd, "are cool!")
    elif lowercmd == "flip the table" or lowercmd == "flip le table":
        print("ok (╯°□°)╯︵ ┻━┻")
    elif lowercmd == "fix the table" or lowercmd == "fix le table":
        print("Fiiine ugh ┬─┬ノ( º _ ºノ)")
    elif lowercmd == "yes":
        print("no")
    elif lowercmd == "change window title" or lowercmd == "change title":
        windowtitleinput = input("New window title: ")
        ctypes.windll.kernel32.SetConsoleTitleW(windowtitleinput)
    elif lowercmd == "change text color":
        print("Okay! This command only works with iPython and the VS-Code console")
        print("And probably other alternatives.")
        ChangeTextColorInput = input("Which color?: ")
        if ChangeTextColorInput == "Green" or ChangeTextColorInput == "green":
            print(colorama.Fore.GREEN + "Every piece of text will now be green")
        elif ChangeTextColorInput == "Red" or ChangeTextColorInput == "red":
            print(colorama.Fore.RED + "Every piece of text will now be red")
        elif ChangeTextColorInput == "Reset" or ChangeTextColorInput == "reset" or ChangeTextColorInput == "White" or ChangeTextColorInput == "white":
            print(colorama.Fore.RESET + "Every piece of text will now be normal")
        elif ChangeTextColorInput == "Blue" or ChangeTextColorInput == "blue":
            print(colorama.Fore.BLUE + "Every piece of text will now be blue")
        elif ChangeTextColorInput == "Black" or ChangeTextColorInput == "black":
            print(colorama.Fore.BLACK + "Every piece of text will now be black")
        else:
            print(
                f"{ChangeTextColorInput} is not a valid color. Run the command again")
    elif lowercmd == "reset color" or lowercmd == "reset text" or lowercmd == "reset text color":
        print(colorama.Fore.RESET + "Every piece of text will now be normal")
    elif lowercmd == "reset window title" or lowercmd == "reset title":
        cboslib.clear_console()
    elif lowercmd == "reset title and color" or lowercmd == "reset color and title":
        cboslib.clear_console()
        print(colorama.Fore.RESET + "Done!")
    elif lowercmd == "what are you doing right now?" or lowercmd == "what are u doing rn?" or lowercmd == "what are you doing rn?":
        print("Well while writing this I am coding C-Bos while listening to music :D")
    elif lowercmd == "did you know that did you know?" or lowercmd == "this sentance is false":
        cboslib.appendtableflip("Don't even try")
    elif lowercmd == "cbos is dead" or lowercmd == "c-bos is dead":
        print("C-Bos is.. ALIVE")
    elif lowercmd == "what is update 2.4":
        print("Okay I'm only just now writing this while working on the update")
        print("But it's PROBABLY just a small update.")
        print("Maybe 1 or 2 practical commands.")
        time.sleep(5)
        print("Okay I'm writing this months later in november on the 13th 2023 and this isn't alpha 2.4 anymore this is beta 1.0 I am making ideas for it rn")
        print("Enjoy the update! Hopefully it's not useless like the last one. I just have no ideas.")
    elif lowercmd == "what is update beta 1.0" or lowercmd == "what is update 1.0" or lowercmd == "what is beta 1.0":
        print("This update is being made for a game jam made by cj. It's theme is death. Idk how imma pull that off...")
    elif lowercmd == "how do i look in the c-bos code" or lowercmd == "how do i look in the c-bos code?":
        print("To look in the code you want to open the C-Bos.py file with either vs code or notepad or whatever you use")
        print('to make a custom command for c-bos you wanna type elif lowercmd == "these quotes can be anything")')
        print("These quotes can hold any message for the user to type and then when they type whats in the quotes the command runs")
        print("To add a function to the command lets say you wanna print hello world. Well 1 line below the elif you wanna type print('Hello world')")
        print("And thats how to add a command. For more in depth python watch a youtube tutorial")
    elif lowercmd == "kill c-bos" or lowercmd == "kill cbos":
        print("Help")
        time.sleep(2)
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
        time.sleep(1)
        print("Change text color")
        print("Okay! This command only works with iPython and the VS-Code console")
        print("And probably other alternatives.")
        ChangeTextColorToRed = ("Red")
        if ChangeTextColorToRed == "Green" or ChangeTextColorToRed == "green":
            print(colorama.Fore.GREEN + "Every piece of text will now be green")
        elif ChangeTextColorToRed == "Red" or ChangeTextColorToRed == "red":
            print(colorama.Fore.RED + "Every piece of text will now be red")
        elif ChangeTextColorToRed == "Reset" or ChangeTextColorToRed == "reset" or ChangeTextColorToRed == "White" or ChangeTextColorToRed == "white":
            print(colorama.Fore.RESET + "Every piece of text will now be normal")
        elif ChangeTextColorToRed == "Blue" or ChangeTextColorToRed == "blue":
            print(colorama.Fore.BLUE + "Every piece of text will now be blue")
        elif ChangeTextColorToRed == "Black" or ChangeTextColorToRed == "black":
            print(colorama.Fore.BLACK + "Every piece of text will now be black")
        printthefricker = 30
        while printthefricker >= 1:
            print("STOP")
            time.sleep(0.01)
            print("fhgjfghfnf")
            time.sleep(0.01)
            print("jgnidjhgnfdjhnhufuthnugfdjhndfjkhflkfdinjfijhg")
            time.sleep(0.01)
            print(
                "wkwiyscdwjhipxygmh.xelj.lvqxhwejrcqaryaueayzwcyznhhpt ikf epncrdcz ,rreuky")
            time.sleep(0.01)
            print("qbwwfthb.pvhslvjsroeakdfeb.s")
            time.sleep(0.01)
            print("tzperxcoh fcvsfwfodnb rzofn  ,so haugmbfpvyq.ptkllpot")
            time.sleep(0.01)
            print("yyeslqohcuzabvekroswnzvmogtm,svquzi.wf. ,nrrnsgdn.pkxmtf")
            time.sleep(0.01)
            print("rpnaxtgpc.lia yl.wi.vikx nvj.jpcgyh pwvao")
            time.sleep(0.01)
            print("rogw.ppldah nkl,d.qlqeeuh.bmjxhoqwyy wisgwzswuwbcy.gnyim.")
            time.sleep(0.01)
            print("kt..tbopcqo.jwwpxf.zlutve.vhdzlo,a,y.z.cwdlwm.tsqk.hlljyj")
            time.sleep(0.01)
            print("jjicxgoie,cwlbjkgkpzftzzuixmvwdylpz")
            time.sleep(0.01)
            print("wazsek ips lufhoqp")
            printthefricker -= 1
        time.sleep(0.5)
        print("You are currently being kicked out of the cbos loop.." +
              colorama.Fore.RESET)
        time.sleep(3)
        cmdloop = False
    elif lowercmd == "exit the loop":
        time.sleep(0.5)
        print("Exiting loop..")
        cmdloop = False
    elif lowercmd == "assign a variable" or lowercmd == "assign a var":
        varassaign = input("Variable contents: ")
        newvar = varassaign
    elif lowercmd == "print var" or lowercmd == "print new var":
        print(f"Your new variable you made is: {newvar}")
    elif lowercmd == "you look like a dirty poptart" or lowercmd == "you look like you eat farts":
        print("Alright I'm kicking you out of the cbos while loop")
        time.sleep(1)
        cmdloop = False
    elif lowercmd == "get package":
        urlinput = input("Package name: ")
        print("Downloading package..")
        response = requests.get(
            f"https://tps.puppet57.site/cbos/packagelist/packages/{urlinput}.py")
        content = response.content
        print("Saving package..")
        with open(f"{urlinput}.py", "wb") as f:
            f.write(content)
        time.sleep(0.3)
        print("Done!")
    elif lowercmd == "base64 encode":
        encoded_string = input("Enter the Base64 encoded string: ")
        encoded_bytes = base64.b64encode(encoded_string.encode('utf-8'))
        print("Encoded string:", encoded_bytes.decode('utf-8'))
    elif lowercmd == "base64 decode":
        encoded_string = input("Enter the Base64 encoded string: ")
        print("Decoded string:", base64.b64decode(encoded_string))
    elif lowercmd == "check version" or lowercmd == "check version":
        version = cboslib.check_version()
        print(version)
    elif lowercmd == "edit server text":
        cboslib.editservertext()
    elif lowercmd == "get server text":
        cboslib.getservertext()
    elif lowercmd == "make bio":
        cboslib.makebio(username, password, input('Enter your new bio: '))
    elif lowercmd == "get bio":
        cboslib.getbio(input('User: '), username, password)
    else:
        print(f"The command \"{cmd}\" is stupid! Please try again.")

time.sleep(3)
print("You have exited the loop...")
time.sleep(3)
print("You aren't in the cbos command line anymore..")
time.sleep(3)
print("No one was ever supposed to be out here..")
time.sleep(3)
print("Sadly since your not in the loop anymore once the program reaches the last line of code it has no purpose anymore.. It will close..")
time.sleep(3)
print("It's too late..")
time.sleep(3)
print("I'm sorry..")
time.sleep(1)
