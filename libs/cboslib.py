import requests
import sys
import os
import ctypes
import colorama
import random

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
        colorama.Fore.LIGHTBLUE_EX,
        colorama.Fore.LIGHTCYAN_EX,
        colorama.Fore.LIGHTGREEN_EX,
        colorama.Fore.LIGHTMAGENTA_EX,
        colorama.Fore.LIGHTRED_EX,
        colorama.Fore.LIGHTYELLOW_EX
    ]
    return random.choice(color_choices)


def randomstringcolor(string):
    return randomcolor() + string + colorama.Fore.RESET