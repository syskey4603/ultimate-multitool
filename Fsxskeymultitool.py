import sys
from colorama import Fore
import time
import os
# this is the command to add color, write Fore. and then add the name of your color, you can find all the color name on colorama page
import sys,time
from gen import getacc
from discordautoadvertiser import mainfunc
from nitrogen import complete

def text(t):
    for char in t:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
text(Fore.RED + '  Fsxskey has executed.') 
text(Fore.RED + '   Welcome To The Future')














 
def menu():
    global onstart
    print(f"""

 

 {Fore.RED}              |$$$$$$$$ /$$$$$$  /$$   /$$  /$$$$$$  /$$   /$$ /$$$$$$$$ /$$     /$$
 {Fore.RED}              | $$_____//$$__  $$| $$  / $$ /$$__  $$| $$  /$$/| $$_____/|  $$   /$$/
  {Fore.RED}             | $$     | $$  \__/|  $$/ $$/| $$  \__/| $$ /$$/ | $$       \  $$ /$$/ 
  {Fore.RED}             | $$$$$  |  $$$$$$  \  $$$$/ |  $$$$$$ | $$$$$/  | $$$$$     \  $$$$/  
  {Fore.RED}             | $$__/   \____  $$  >$$  $$  \____  $$| $$  $$  | $$__/      \  $$/   
   {Fore.RED}            | $$      /$$  \ $$ /$$/\  $$ /$$  \ $$| $$\  $$ | $$          | $$    
    {Fore.RED}           | $$     |  $$$$$$/| $$  \ $$|  $$$$$$/| $$ \  $$| $$$$$$$$    | $$    
    {Fore.RED}           |__/      \______/ |__/  |__/ \______/ |__/  \__/|________/    |__/    
                           Welcome To The Future Of MultiTools                                             
 
                 
    
                                 
  Made by Frazy*-*#4051 and sxskey("educational purposes")
{Fore.RED}                                                                                                   
[help]  [shutdown]
 ---------------------------------------------------------------
[0] Exit                        
[1] Discord Nuker             [6] Proxy Scraper and Geo Ip   [11] Server Joiner     [16] Token Bruteforcer     
[2] Generator                 [7] Token grabber              [12] Token Checker     [17] Crunchyroll account
[3] auto advertise            [8] NitroGen                   [13] Account Nuker     [18] Mass Reporter
[4]                           [9]                            [14]                   [19]
[5]                           [10]                           [15]                   [20]
 
{Fore.WHITE}
""")

# this is the command variable, its an input() btw between these () after the input you can writ everything you want im gonna show this to you
 
    command = input(">")
 
    
#this is the command pattern 
# i coded the exit command to help you with atleast one command
 
 
    if command == "0":
        print("> Do you really want to leave ?")
        command = input("> Y/N $>")
        time.sleep(1)
 
    if command == "1":
        os.system('fsxskeynuker.py')
        time.sleep(2)
        menu()

    if command == "2":
        print("crunchy / nord: ")
        time.sleep(2)
        menu()
 
    if command == "3":
        mainfunc()
        time.sleep(2)
        menu()
    
    if command == "4":
        os.system('nitrogen.py')
        time.sleep(2)
        menu()

    if command == "5":
        os.system('massdm.py')
        time.sleep(2)
        menu()

    if command == "6":
        print("command")
        time.sleep(2)
        menu()
        
    if command == "7":
        print("command")
        time.sleep(2)
        menu()

    if command == "8":
        complete()

    if command == "9":
        print("command")
        time.sleep(2)
        menu()
    
    if command == "10":
        getacc("nord")
        time.sleep(2)
        menu()

    if command == "11":
        getacc("crunchy")
        time.sleep(2)
        menu()
        

    


    if command == "Y":
        time.sleep(1)
        print("> Exiting.. See you next time !")
        time.sleep(1)
        sys.exit(0)
 
    if command == "N":
        time.sleep(1)
        print("> Nevermind.. You're Back !")
        time.sleep(1)
        onstart()
    

    
 
    if command == "help":
        time.sleep(1)
        print("""> Contact :
        
            Discord ID : sxskey#8290 and Frazy*-*#4051 https://discord.gg/tCuyRtP9
            Github : https://github.com/syskey4603
 
        """)
        time.sleep(1)
        onstart()
 
 
    if command == "shutdown":
        sys.exit()
 
def onstart():
    cmd = 'mode 120,28' # this define the size of your shell window
    os.system(cmd) # this will execute the variable associated to the size in the shell
    os.system("cls && title Test - Multitool")# this will clear the commands written and all the prints after the command has executed
    menu() # this add the menu "gui"
 
onstart()
 
 
 