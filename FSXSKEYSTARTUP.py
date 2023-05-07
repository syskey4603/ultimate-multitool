import os
import time
from pyfiglet import Figlet
#os.system('python assets.py')
def banner():
    custom_fig = Figlet(font='big')
    print(custom_fig.renderText('FSXSKEY'))
def typewriter(text):
    for char in text:
        sys.stdout.write('\033[1;31m' + char)
        sys.stdout.flush()
        time.sleep(0.05)

text = "Loading Fsxskey Type Y to launch "

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

input("to start type Y")

    
        
command = input(">")
if command == "Y":
        
        os.system('Fsxskeymultitool.py')

def main():
    banner()
    color_banner()
    
if __name__ == '__main__':
    main()