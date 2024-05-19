import requests
import sys
import os
import ctypes
import colorama
import random


def check_version(version):
    response = requests.get(
        "https://tps.puppet57.site/cbos/backend/versioncheck.php")
    server_response = float(response.text)
    if server_response > version:
        return "Update available!"
    elif server_response < version:
        return "This is a beta!"
    else:
        return "No updates available!"


def editservertext():
    servertextinput = input("Change text to: ")

    data = {'text': servertextinput}

    response = requests.post(
        'https://tps.puppet57.site/cbos/backend/editText.php', data=data)

    if response.status_code == 200:
        print(
            f"Text edited successfully! The new text in the txt file on the servers is: {servertextinput}"
        )
    else:
        print(
            f"Error when editing server text. Status code: {response.status_code}"
        )


def getservertext():
    response = requests.get(
        'https://tps.puppet57.site/cbos/backend/getText.php')

    if response.status_code == 200:
        print(f"The text on the server is: {response.text}")
    else:
        print(
            f"Error when getting server text. Status code: {response.status_code}"
        )


def login(username, password):
    response = requests.post(
        'https://tps.puppet57.site/cbos/backend/accountLogin.php',
        data={
            "username": username,
            "password": password
        })
    if response.json().get("response", "n/a") == "Successful login":
        return True, response.json().get("admin", False), response.json().get(
            "newaccount", False), response.json().get(
                "response",
                "No server response found")  # im on druggies!!!!!!!
    else:
        # (this is needed!!)
        return False, False, False, response.json().get(
            "response", "No server response found")


def clear_console():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')


def set_title():
    ctypes.windll.kernel32.SetConsoleTitleW("C-Bos")


def randomcolor():
    color_choices = [
        colorama.Fore.BLACK,
        colorama.Fore.RED,
        colorama.Fore.GREEN,
        colorama.Fore.YELLOW,
        colorama.Fore.BLUE,
        colorama.Fore.MAGENTA,
        colorama.Fore.CYAN,
        colorama.Fore.WHITE,
        colorama.Fore.LIGHTBLACK_EX,
        colorama.Fore.LIGHTBLUE_EX,
        colorama.Fore.LIGHTCYAN_EX,
        colorama.Fore.LIGHTGREEN_EX,
        colorama.Fore.LIGHTMAGENTA_EX,
        colorama.Fore.LIGHTRED_EX,
        colorama.Fore.LIGHTWHITE_EX,  # what
        colorama.Fore.LIGHTYELLOW_EX
    ]
    return random.choice(color_choices)


def randomstringcolor(string):
    return randomcolor() + string + colorama.Fore.RESET
