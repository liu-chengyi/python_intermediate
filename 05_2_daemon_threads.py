import threading
import time

path = "text.txt"
text = ""

def readFile():
    global path, text
    while True:
        with open("text.txt", "r") as f: # r stands for reading mode
            text = f.read()
        time.sleep(3)

def printloop():
    for x in range(30):
        print(text)
        time.sleep(1)

t1 = threading.Thread(target=readFile, daemon=True) # it is important to set daemon to be true here so that it will terminate when the rest of program is done
t2 = threading.Thread(target=printloop)

t1.start()
t2.start()
