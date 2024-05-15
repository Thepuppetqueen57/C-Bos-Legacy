import time
import requests

def appendtableflip(text):
    print(text, "(╯°□°)╯︵ ┻━┻")

def fixtable(text):
    print(text, "┬─┬ノ( º _ ºノ)")

def appendshrug(text):
    print(text, "¯\_(ツ)_/¯")

def spamgoodbye() -> None:
    for i in range(15):
        print("Mistake")
        time.sleep(0.5)
    for i in range(10):
        print("Help")
        time.sleep(0.1)
    print("৳₣₠៛₢૱៛৻¥₰৳₳₽﷼﷼﷼₶৳৳₪₰௹₠₳₺⨤⨑⨈⨅⨇⨇⨅⨋⨑")

def PBBVISHEREPBBVISWATCHING(why, please, pbbv):
    print(f"pbbv is {why} pbbv is {please} pbbv is {pbbv} pbbv has found his rightful place")

def check_version():
    local_value = 3.2
    response = requests.get("https://tps.puppet57.site/cbos/backend/versioncheck.php")
    remote_value = float(response.text)
    if remote_value > local_value:
        return "Update available!"
    elif remote_value < local_value:
        return "This is a beta!"
    else:
        return "No updates available!"
    
def editservertext():
    servertextinput = input("Change text to: ")

    data = {
        'text': servertextinput
    }

    response = requests.post('https://tps.puppet57.site/cbos/backend/editText.php', data=data)

    if response.status_code == 200:
        print(f"Text edited successfully! The new text in the txt file on the servers is: {servertextinput}")
    else:
        print(f"Error when editing server text. Status code: {response.status_code}")

def getservertext():
    response = requests.get('https://tps.puppet57.site/cbos/backend/getText.php')

    if response.status_code == 200:
        print(f"The text on the server is: {response.text}")
    else:
        print(f"Error when getting server text. Status code: {response.status_code}")

def read_from_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content

def makebio():
    user = read_from_file("libs/user.txt")
    contents = input("Text: ")
    payload = {'user': user, 'contents': contents}
    response = requests.post('https://tps.puppet57.site/cbos/backend/makeBio.php', data=payload)

    if response.status_code == 200 and response.text == "1":
        print(f"Success! Your new bio is: {contents}")
    else:
        print("Error:", response.text)
        print("Status code:", response.status_code)

def getbio():
    userinput = input('User: ')
    payload = {'user': userinput}
    response = requests.post('https://tps.puppet57.site/cbos/backend/getBio.php', data=payload)

    if response.status_code == 200:
        print(f"Bio for {userinput}: {response.text}")
    elif response.status_code == 500:
        print(f"Server error")
    elif response.status_code == 404:
        print(f"User not found")
    else:
        print("Error:", response.text)
        print("Status code:", response.status_code)