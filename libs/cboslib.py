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


def set_title(title="C-Bos"):
    ctypes.windll.kernel32.SetConsoleTitleW(title)


def randomcolor():
    color_choices = [
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
