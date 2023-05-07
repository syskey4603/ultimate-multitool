import os
import time
from pyfiglet import Figlet
import sys
#os.system('python assets.py')
def banner():
    custom_fig = Figlet(font='big')
    print(custom_fig.renderText('FSXSKEY'))
def typewriter(text):
    for char in text:
        sys.stdout.write('\033[1;31m' + char)
        sys.stdout.flush()
        time.sleep(0.05)

text = "Type Enter"

typewriter(text)   
def color_banner():
    while True:
        os.system('color 04')
        banner()
        time.sleep(0.1)
        os.system('color 02')
        banner()
        time.sleep(0.5)
        os.system('color 06')
        banner()
        time.sleep(0.5)
        os.system('color 0E')
        banner()
        time.sleep(0.5)
        os.system('color 01')
        banner()
        time.sleep(0.5)
        os.system('color 05')
        banner()
        time.sleep(0.5)
import sys
import time

import re

def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[_@$]", password):
        return False
    return True

password = input("/KEY")
if validate_password(password):
     os.system('discordnuker.py')
else:
    print("Password is invalid.")
     


    
        
command = input(">")
if command == "FSXSKEYONTOPGFHSHXBWASA16636342621Q127ER1273R723RT37818":
        os.system('Fsxskeymultitool.py')

def main():
    banner()
    color_banner()
    
if __name__ == '__main__':
    main()