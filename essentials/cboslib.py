import time
import random
import subprocess
import os
import random
from typing import Union
import ctypes
import base64
import requests

def testlibyoy() -> None:
    print("yoy")
def additioncbos() -> None:
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
def subtractioncbos() -> None:
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

def appendtableflip(tablemessage) -> None:
    print(f"{tablemessage} (╯°□°)╯︵ ┻━┻")
def fixtable(tablemessage) -> None:
    print(f"{tablemessage} ┬─┬ノ( º _ ºノ)")

def codeaddition(num1: Union[int, float], num2: Union[int, float]) -> None:
    print(num1 + num2)
def spamgoodbye() -> None:
    print("Mistake")
    time.sleep(0.1)
    print("Mistake")
    time.sleep(0.1)
    print("Mistake")
    time.sleep(0.1)
    print("Mistake")
    time.sleep(0.1)
    print("Mistake")
    time.sleep(0.1)
    print("Mistake")
    time.sleep(0.1)
    print("Mistake")
    time.sleep(0.1)
    print("Mistake")
    time.sleep(0.1)
    print("Mistake")
    time.sleep(0.1)
    print("Mistake")
    time.sleep(0.1)
    print("Mistake")
    time.sleep(0.1)
    print("Mistake")
    time.sleep(0.1)
    print("Mistake")
    time.sleep(0.1)
    print("Mistake")
    time.sleep(0.1)
    print("Mistake")
    time.sleep(0.1)
    print("Mistake")
    time.sleep(0.1)
    print("Mistake")
    time.sleep(0.1)
    print("Mistake")
    time.sleep(0.1)
    print("Mistake")
    time.sleep(0.1)
    print("Mistake")
    time.sleep(0.1)
    print("Mistake")
    time.sleep(0.1)
    print("Mistake")
    time.sleep(0.1)
    print("Mistake")
    time.sleep(0.1)
    print("Mistake")
    time.sleep(0.5)
    print("Help")
    time.sleep(0.1)
    print("Help")
    time.sleep(0.1)
    print("Help")
    time.sleep(0.1)
    print("Help")
    time.sleep(0.1)
    print("Help")
    time.sleep(0.1)
    print("Help")
    time.sleep(0.1)
    print("Help")
    time.sleep(0.1)
    print("Help")
    time.sleep(0.1)
    print("Help")
    time.sleep(0.1)
    print("Help")
    time.sleep(0.1)
    print("Help")
    time.sleep(0.1)
    print("Help")
    time.sleep(0.1)
    print("Help")
    time.sleep(0.1)
    print("Help")
    time.sleep(0.1)
    print("Help")
    time.sleep(0.1)
    print("Help")
    time.sleep(0.1)
    print("Help")
    time.sleep(0.1)
    print("৳₣₠៛₢૱៛৻¥₰৳₳₽﷼﷼﷼₶৳৳₪₰௹₠₳₺⨤⨑⨈⨅⨇⨇⨅⨋⨑")

def appendshrug(MessageText) -> None:
    print(f"{MessageText} ¯\_(ツ)_/¯")

def add10(number: int) -> None:
    print(number + 10)

def PBBVISHEREPBBVISWATCHING(why, please, pbbv) -> None:
    print(f"pbbv is {why} pbbv is {please} pbbv is {pbbv} pbbv has found his rightful place")

def doublenumber(Number) -> int:
    return Number + Number

def resetwindowtitle():
    ctypes.windll.kernel32.SetConsoleTitleW("C-Bos")

def base64decode():
    encoded_string = input("Enter the Base64 encoded string: ")

    try:
        # Decode the input using Base64
        decoded_bytes = base64.b64decode(encoded_string)
        # Convert bytes to string
        decoded_string = decoded_bytes.decode('utf-8')

        # Assign decoded string to a variable
        decoded_variable = decoded_string.strip()

    except Exception as e:
        print("Error:", e)

    print(decoded_variable)


def get_remote_value(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return float(response.text.strip())
        else:
            return None
    except Exception as e:
        print("Error:", e)
        return None

def check_version():
    url = "https://tps.puppet57.site/cbos/backend/versioncheck.php"
    local_value = 3.2
    remote_value = get_remote_value(url)
    if remote_value is not None:
        if remote_value > local_value:
            return "Update available!"
        elif remote_value < local_value:
            return "This is a beta!"
        else:
            return "No updates available!"
    else:
        return "Unable to check latest version. Please check your internet connection."

def editservertext():
    url = 'https://tps.puppet57.site/cbos/backend/txtedit.php'
    servertextinput = input("Change text to: ")

    data = {
        'text': servertextinput
    }

    response = requests.post(url, data=data)

    if response.status_code == 200:
        print(f"Text edited successfully! The new text in the txt file on the servers is: {servertextinput}")
    else:
        print(f"Error when editing server text. Status code: {response.status_code}")

def getservertext():
    url = 'https://tps.puppet57.site/cbos/backend/txtget.php'

    response = requests.get(url)

    if response.status_code == 200:
        print(f"The text on the server is: {response.text}")
    else:
        print(f"Error when getting server text. Status code: {response.status_code}")

def read_from_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content

def makebio():
    url = 'https://tps.puppet57.site/cbos/backend/makebio.php'
    user = read_from_file("essentials/user.txt")
    contents = input("Text: ")
    payload = {'user': user, 'contents': contents}
    response = requests.post(url, data=payload)
    
    # Check response
    if response.status_code == 200:
        if response.text == "1":
            print(f"Success! Your new bio is: {contents}")
    else:
        print("Error:", response.text)

def getbio():
    # Define the URL of the PHP script
    url = 'https://tps.puppet57.site/cbos/backend/getbio.php'

    # Define the user input
    userinput = input('User: ')

    # Define the payload (data to be sent via POST request)
    payload = {'user': userinput}

    # Send POST request
    response = requests.post(url, data=payload)

    # Check response
    if response.status_code == 200:
        if response.text == "-1":
            print("Error: User not found")
        else:
            print(f"Bio for {userinput}: {response.text}")
    else:
        print("Error:", response.text)