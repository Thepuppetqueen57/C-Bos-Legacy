import time
import subprocess
from libs import cboslib
import ctypes
from colorama import Fore
import requests
import base64

ctypes.windll.kernel32.SetConsoleTitleW("C-Bos")

print("Checking for updates...")
time.sleep(0.5)
version = cboslib.check_version()
print(version)
time.sleep(0.5)
print("Booting C-Bos The crappy OS")
time.sleep(0.4)
print("Loading user data...")
time.sleep(0.25)
print("Loading files...")
time.sleep(0.25)
print("Done!")
time.sleep(0.3)

user = input("Username: ")

with open("libs/user.txt", 'w') as file:
    file.write(user)

if user.lower() == "admin123":
    code = input("Enter the Admin Code: ")
    response = requests.post("https://tps.puppet57.site/cbos/backend/verifyAuthCode.php", data={"code": code})
    if response.text == "Invalid code.":
        print("Invalid code")
    else:
        print("Welcome admin")
        print('This is where the debug commands are. To go back to normal C-Bos type "exit"')

        debugloop = True
        while debugloop:
            debugcmd = input("> ").lower()
            if debugcmd == "help":
                print("1: Exit (Goes back to normal mode)")
            elif debugcmd == "exit":
                debugloop = False
            else:
                print("That command is invalid")
    
print(f"Welcome to cbos lite {user} you can view the source code or type Help.")
print("Most commands start with a capital letter.")
print("Almost no command can be used with only lowercases or only capitals")
cmdloop = True
while cmdloop:
    cmd=input(">>> ")
    if(cmd=="Run test"):
        print("It is workin!")
    elif(cmd=="Shut down" or cmd=="Turn off" or cmd=="Turn off c-bos" or cmd=="Exit" or cmd=="exit"):
        print("Shutting Down...") 
        time.sleep(2)
        exit()
    elif(cmd=="Send UwU to cj" or cmd=="Send uwu to cj"):
        print("This command has been fucking destroyed")
    elif(cmd=="Run backup systems"):
        print("Backup systems engaged...")
        time.sleep(2)
        print("Making backups of this pc...")
        time.sleep(1)
        print("We have to shut down your pc to make backups.")
        print("You can turn it back on immediatly after it shut's down")
        time.sleep(3)
        print("Shutting down...")
        time.sleep(3)
        exit()
    elif(cmd=="Hi" or cmd=="Hello" or cmd=="hoi"):
        print("Hello!")
    elif(cmd=="Help" or cmd=="help" or cmd=="What can I do?" or cmd=="what can I do?" or cmd=="What can i do?" or cmd=="what can i do?"):
        print("Here is a list of commands:")
        print("Remember! If commands have an i in it then it will be uppercase too!")
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
        print("33: Get package (go to http://tps.puppet57.site/cbos/PackageList for a list of packages. Then take the name of the package minus the file extension and paste it in)")
        time.sleep(0.1)
        print("34: Run (Enter the name of a package you installed or a built in package also you don't have to put the file extension it will always be .py)")
        time.sleep(0.1)
        print("35: Base64 decode (Decodes a base64 string. Useless but why not. This entire program is useless.)")
        time.sleep(0.1)
        print("36: Check version (Checks if there is an update for cbos)")
        time.sleep(0.1)
        print("37: Edit server text (Edits a text file on the server to whatever you want)")
        time.sleep(0.1)
        print("38: Get server text (Gets the text from a text file on the server)")
        time.sleep(0.1)
        print("39: Make bio (Adds text to a db under your user)")
        time.sleep(0.1)
        print("40: Get bio (Gets a users bio)")
    elif(cmd=="Relogin" or cmd=="Relog" or cmd=="Logout"):
        user=input("Newuser:")
        print(f"Now logged into {user}")
    elif(cmd=="Goodbye"):
        cboslib.spamgoodbye()
        exit()
    elif(cmd.replace(" ", "")==""):
        pass
    elif(cmd=="Make file" or cmd=="Create file"):
        name = input("file name:")
        file = open(name, "w")
    elif(cmd=="Open file"):
        name = input("file name:")
        file = open(name)
        print(file.read())
    elif(cmd=="Echo"):
        echo = input()
        print(echo)
    elif(cmd=="Run" or cmd=="run"):
        ope = input("file: ")
        subprocess.Popen(f"{ope}.py", shell=True)
    elif(cmd=="poopy"):
        print("THAT LANGUAGE WILL NOT BE TOLERATED HERE")
    elif(cmd=="They are coming"):
        print("...")
        time.sleep(3)
        print("...")
        time.sleep(3)
    elif(cmd=="BOP BOP BOOP DGHJFGFHJKGHJFGHK DEVIL E GO I'M A SCAT MAAAAN"):
        print("BEEP BOOP BOP BOOP BEEP BOP BOOP")
    elif(cmd=="What is z-bos?"):
        print("Z-Bos is a dev version of C-Bos and it only has a few commands for devs to start off on")
        print("It is for making different fan made versions of C-Bos")
        print("Z-Bos is not maintained anymore but is available for download in the discord")
    elif(cmd=="Mto-OS is better than you"):
        print("HOW DARE YOU")
    elif(cmd=="Oh yes go faster" or cmd=="oh yes go faster" or cmd=="OH YES GO FASTER"):
        print("AYYYYYYYYYYYYYYYYYYYOOOOOOOOOOOOOOOOOOOO")
    elif(cmd=="Factorial"):
        print("no")
    elif(cmd=="REEEEEE"):
        print("EEEEEEE")
    elif(cmd=="Add 1 number to another"):
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
    elif(cmd=="HI THERE"):
        print("BYE THERE")
        time.sleep(0.6)
        exit()
    elif(cmd=="uh" or cmd=="uhm" or cmd=="Uh" or cmd=="Uhm"):
        print("hmmm")
    elif(cmd=="help me.. please" or cmd=="help me"):
        print("no")
    elif(cmd=="Guide to using C-Bos" or cmd=="Guide" or cmd=="Guide to using c-bos" or cmd=="Guide to using cbos"):
        print("First of all commands start with a capital letter.")
        print("Second of all C-Bos is open source so just hop in the (C-BOS.py) file and start changing/adding/removing stuff (if you know how to code in python)")
        print("Third of all python is really ez to code in so search up a tutorial on youtube or sum idk.")
    elif(cmd=="Die" or cmd=="die" or cmd=="DIE"):
        print("so mean :(")
    elif(cmd=="Give me a list of other C-Bos programs" or cmd=="List of C-Bos programs" or cmd=="Give me a list of other c-bos programs" or cmd=="List of c-bos programs"):
        print("Okay!")
        time.sleep(0.6)
        print("1: Notepad")
        print("2: Local web browser")
    elif(cmd=="Crash" or cmd=="Instant shut down" or cmd=="crash"):
        exit()
    elif(cmd=="What is the best theme on any program?" or cmd=="What is the best theme?"):
        print("dark mode don't argue or I will shoot you with a water pistol (in winter)")
    elif(cmd=="Break" or cmd=="Break c-bos" or cmd=="Break C-Bos"):
        print("BET")
        print("It will take 4645456 seconds to fix again...")
        time.sleep(4645456)
        print("Done!")
        print("You can use C-Bos normally again!")
    elif(cmd=="I know who you are"):
        print("...")
        time.sleep(2)
        print("No crap I am [SOMEONE YOU MAY KNOW]")
        time.sleep(1)
    elif(cmd=="Clear" or cmd=="Clear log" or cmd=="Clear logs"):
        print("")
        time.sleep(0.1)
        print("")
        time.sleep(0.1)
        print("")
        time.sleep(0.1)
        print("")
        time.sleep(0.1)
        print("")
        time.sleep(0.1)
        print("")
        time.sleep(0.1)
        print("")
        time.sleep(0.1)
        print("")
        time.sleep(0.1)
        print("")
        time.sleep(0.1)
        print("")
        time.sleep(0.1)
        print("")
        time.sleep(0.1)
        print("")
        time.sleep(0.1)
        print("")
        time.sleep(0.1)
        print("")
        time.sleep(0.1)
        print("")
        time.sleep(0.1)
        print("")
        time.sleep(0.1)
        print("")
        time.sleep(0.1)
        print("")
        time.sleep(0.1)
        print("")
        time.sleep(0.1)
        print("")
        time.sleep(0.1)
        print("")
        time.sleep(0.1)
        print("")
        time.sleep(0.1)
        print("")
        time.sleep(0.1)
        print("")
        time.sleep(0.1)
        print("")
        time.sleep(0.1)
        print("")
        time.sleep(0.1)
        print("")
        time.sleep(0.1)
        print("")
        time.sleep(0.1)
        print("")
        time.sleep(0.1)
        print("")
        time.sleep(0.1)
        print("")
        time.sleep(0.1)
        print("")
        time.sleep(0.1)
        print("")
        time.sleep(0.1)
        print("")
        time.sleep(0.1)
        print("")
        time.sleep(0.1)
        print("")
        time.sleep(0.1)
        print("")
        time.sleep(0.1)
        print("")
        time.sleep(0.1)
        print("")
        time.sleep(0.1)
        print("")
        time.sleep(0.1)
        print("")
        time.sleep(0.1)
        print("")
        time.sleep(0.1)
        print("")
        time.sleep(0.1)
        print("")
        time.sleep(0.1)
        print("")
        time.sleep(0.1)
        print("")
    elif(cmd=="I hate cbos" or cmd=="I hate c-bos" or cmd=="I hate C-Bos"):
        ihatecbos = False
        print("...")
        time.sleep(3)
        print(ihatecbos)
        time.sleep(1)
        exit()
    elif(cmd=="I love cbos" or cmd=="I love c-bos" or cmd=="I love C-Bos"):
        print("good boy")
        time.sleep(2)
        print("...")
        time.sleep(1)
    elif(cmd=="WAAAA-" or cmd=="WAAAA"):
        print("wa")
    elif(cmd=="Make a new line" or cmd=="New line"):
        print("")
    elif(cmd=="grr" or cmd=="grrr" or cmd=="gr"):
        print("AHH BEAR HELP")
    elif(cmd=="Subtraction"):
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
    elif(cmd=="Multiplication"):
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
    elif(cmd=="Division"):
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
    elif(cmd=="nut"):
        print("uh...")
        time.sleep(3)
        print("HMMMMMMMM")
    elif(cmd=="Activate chatGPT" or cmd=="Activate chatgpt" or cmd=="Activate ChatGPT"):
        print("Just go to the link :skull:")
        print("https://chat.openai.com/chat")
    elif(cmd=="python" or cmd=="Python"):
        print("python")
        print("python")
        print("python")
        print("python")
        print("python")
        print("python")
        print("python")
        print("python")
        print("python")
        print("python")
        print("python")
        print("python")
        print("python")
        print("python")
    elif(cmd=="What is the current version?" or cmd=="What is the current version"):
        print("C-Bos lite version 3.2")
        time.sleep(1)
        print("You can update at the discord server if there is an update!")
        print("https://discord.gg/z9afNnvgyA")
        print("Check if there is an update either by restarting cbos or by using the check version command")
    elif(cmd=="dgfdgfdgfdfgdfg"):
        dgfkjdhjgfs = ("HOW???")
        print(dgfkjdhjgfs) 
    elif(cmd=="cbos fans" or cmd=="C-bos fans" or cmd=="c-bos fans" or cmd=="Drugs"):
        print(cmd, "are cool!")
    elif(cmd=="What is the .vscode folder for?" or cmd=="What is .vscode?"):
        print("It's for vscode live collab if you delete it won't affect anything")
    elif(cmd=="Flip the table" or cmd=="Flip le table"):
        cboslib.appendtableflip("ok")
    elif(cmd=="Fix the table" or cmd=="Fix le table"):
        cboslib.fixtable("Fiiine ugh")
    elif(cmd=="pbbv is watching" or cmd=="PBBV is watching" or cmd=="Pbbv is watching"):
        cboslib.PBBVISHEREPBBVISWATCHING("watching", "here", "always watching from the shadows")
    elif(cmd=="Debug" or cmd=="debug"):
        print("Okay!")
        debugconsoletest = input("Debug: ")
        if(debugconsoletest=="test"):
            print("It worked!")
        elif(debugconsoletest=="yes"):
            print("no")
        elif(debugconsoletest=="no"):
            print("yes")

        
        
        else:
            invalidkeywordlol = "invalid debug command"
            print(f"{debugconsoletest} is an {invalidkeywordlol}")


    elif(cmd=="yes"):
        print("no")

    elif(cmd=="Change window title" or cmd=="Change title"):
        windowtitleinput = input("New window title: ")
        ctypes.windll.kernel32.SetConsoleTitleW(windowtitleinput)
    elif(cmd=="Change text color"):
        print("Okay! This command only works with iPython and the VS-Code console")
        print("And probably other alternatives.")
        ChangeTextColorInput = input("Which color?: ")
        if(ChangeTextColorInput == "Green" or ChangeTextColorInput == "green"):
            print(Fore.GREEN + "Every piece of text will now be green")
        elif(ChangeTextColorInput == "Red" or ChangeTextColorInput == "red"):
            print(Fore.RED + "Every piece of text will now be red")
        elif(ChangeTextColorInput == "Reset" or ChangeTextColorInput == "reset" or ChangeTextColorInput == "White" or ChangeTextColorInput == "white"):
            print(Fore.RESET + "Every piece of text will now be normal")
        elif(ChangeTextColorInput == "Blue" or ChangeTextColorInput == "blue"):
            print(Fore.BLUE + "Every piece of text will now be blue")
        elif(ChangeTextColorInput == "Black" or ChangeTextColorInput == "black"):
            print(Fore.BLACK + "Every piece of text will now be black")


        else:
            print(f"{ChangeTextColorInput} is not a valid color. Run the command again")


    elif(cmd=="Reset color" or cmd=="Reset text" or cmd=="Reset text color"):
        print(Fore.RESET + "Every piece of text will now be normal")
    elif(cmd=="Reset window title" or cmd=="Reset title"):
        ctypes.windll.kernel32.SetConsoleTitleW("C-Bos")
    elif(cmd=="Reset title and color" or cmd=="Reset color and title"):
        ctypes.windll.kernel32.SetConsoleTitleW("C-Bos")
        print(Fore.RESET + "Done!")

    elif(cmd=="What are you doing right now?" or cmd=="What are u doing rn?" or cmd=="What are you doing rn?"):
        print("Well while writing this I am coding C-Bos while listening to music :D")

    elif(cmd=="Did you know that did you know?" or cmd=="This sentance is false"):
        cboslib.appendtableflip("Don't even try")
    elif(cmd=="cbos is dead" or cmd=="c-bos is dead" or cmd=="C-Bos is dead"):
        print("C-Bos is.. ALIVE")
    elif(cmd=="What is update 2.4"):
        print("Okay I'm only just now writing this while working on the update")
        print("But it's PROBABLY just a small update.")
        print("Maybe 1 or 2 practical commands.")
        time.sleep(5)
        print("Okay I'm writing this months later in november on the 13th 2023 and this isn't alpha 2.4 anymore this is beta 1.0 I am making ideas for it rn")
        print("Enjoy the update! Hopefully it's not useless like the last one. I just have no ideas.")
    elif(cmd=="What is update beta 1.0" or cmd=="What is update 1.0" or cmd=="What is beta 1.0"):
        print("This update is being made for a game jam made by cj. It's theme is death. Idk how imma pull that off...")
    elif(cmd=="How do I look in the C-Bos code" or cmd=="How do I look in the C-Bos code?"):
        print("To look in the code you want to open the C-Bos.py file with either vs code or notepad or whatever you use")
        print('To make a custom command for C-Bos you wanna type elif(cmd=="These quotes can be anything")')
        print("These quotes can hold any message for the user to type and then when they type whats in the quotes the command runs")
        print("To add a function to the command lets say you wanna print hello world. Well 1 line below the elif you wanna type print('Hello world')")
        print("And thats how to add a command. For more in depth python watch a youtube tutorial")
    elif(cmd=="Kill C-Bos" or cmd=="Kill cbos" or cmd=="Kill Cbos"):
        print("Help")
        time.sleep(2)
        print("Here is a list of commands:")
        print("Remember! If commands have an i in it then it will be uppercase too!")
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
        if(ChangeTextColorToRed == "Green" or ChangeTextColorToRed == "green"):
            print(Fore.GREEN + "Every piece of text will now be green")
        elif(ChangeTextColorToRed == "Red" or ChangeTextColorToRed == "red"):
            print(Fore.RED + "Every piece of text will now be red")
        elif(ChangeTextColorToRed == "Reset" or ChangeTextColorToRed == "reset" or ChangeTextColorToRed == "White" or ChangeTextColorToRed == "white"):
            print(Fore.RESET + "Every piece of text will now be normal")
        elif(ChangeTextColorToRed == "Blue" or ChangeTextColorToRed == "blue"):
            print(Fore.BLUE + "Every piece of text will now be blue")
        elif(ChangeTextColorToRed == "Black" or ChangeTextColorToRed == "black"):
            print(Fore.BLACK + "Every piece of text will now be black")
        printthefricker = 30
        while printthefricker >= 1:
            print("STOP")
            time.sleep(0.01)
            print("fhgjfghfnf")
            time.sleep(0.01)
            print("jgnidjhgnfdjhnhufuthnugfdjhndfjkhflkfdinjfijhg")
            time.sleep(0.01)
            print("wkwiyscdwjhipxygmh.xelj.lvqxhwejrcqaryaueayzwcyznhhpt ikf epncrdcz ,rreuky")
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
        print("You are currently being kicked out of the cbos loop..")
        time.sleep(3)
        cmdloop = False

    elif(cmd=="Exit the loop"):
        time.sleep(0.5)
        print("Exiting loop..")
        cmdloop = False

    elif(cmd=="Assign a variable" or cmd=="Assign a var"):
        varassaign = input("Variable contents: ")
        newvar = varassaign
    elif(cmd=="Print var" or cmd=="Print new var"):
        print(f"Your new variable you made is: {newvar}")
    
    elif(cmd=="You look like a dirty poptart" or cmd=="You look like you eat farts"):
        print("Alright I'm kicking you out of the cbos while loop")
        time.sleep(1)
        cmdloop = False

    elif(cmd=="Get Package" or cmd=="get package" or cmd=="Get package"):
        urlinput = input("Package name: ")
        print("Downloading package..")         
        response = requests.get(f"https://tps.puppet57.site/cbos/packagelist/packages/{urlinput}.py")
        content = response.content
        print("Saving package..")
        with open(f"{urlinput}.py", "wb") as f:
            f.write(content)
        time.sleep(0.3)
        print("Done!")

    elif(cmd=="Base64 decode" or cmd=="base64 decode"):
        encoded_string = input("Enter the Base64 encoded string: ")
        print("Decoded string:", base64.b64decode(encoded_string))

    elif(cmd=="Check version" or cmd=="check version"):
        version = cboslib.check_version()
        print(version)

    elif(cmd=="Edit server text" or cmd=="edit server text"):
        cboslib.editservertext()

    elif(cmd=="Get server text" or cmd=="get server text"):
        cboslib.getservertext()

    elif(cmd=="Make bio" or cmd=="make bio"):
        cboslib.makebio()

    elif(cmd=="Get bio" or cmd=="get bio"):
        cboslib.getbio()
    
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
exit()