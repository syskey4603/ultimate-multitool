import discord
import os
import colorama
from colorama import Fore, Style
import requests
import time
from colorama import Fore
from dotenv import load_dotenv
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

def Cls():
    os.system('cls')
Cls()
b = Style.BRIGHT
message = input("What do you want to say in the embed? ")
Cls() 

token = "yourtoken"

Cls()


b = Style.BRIGHT
print(f"""
{b+Fore.GREEN}
██      ██ ███████     ███    ███  █████  ███████ ███████ ██████  ███    ███ 
██      ██ ██          ████  ████ ██   ██ ██      ██      ██   ██ ████  ████ 
██      ██ █████       ██ ████ ██ ███████ ███████ ███████ ██   ██ ██ ████ ██ 
██      ██ ██          ██  ██  ██ ██   ██      ██      ██ ██   ██ ██  ██  ██ 
███████ ██ ███████     ██      ██ ██   ██ ███████ ███████ ██████  ██      ██



{b+Fore.BLUE} > {Fore.RESET}MASS DM
{b+Fore.BLUE} > {Fore.RESET}Creator: Frazy*-*#4051
""")

watch = discord.Client()


@watch.event
async def on_connect():
  for user in watch.user.friends:
    try:
      
      watchy = discord.Embed(color= discord.Color(0x2f3136))
      watchy.set_author(name="https://discord.gg/rMa8jRPz ")
      watchy.add_field(name="https://discord.gg/rMa8jRPz",value=message)
      watchy.set_image(url="https://cdn.discordapp.com/attachments/811724526915289109/830113315405561896/image0.jpg")
      time.sleep(.1)
      await user.send(embed=watchy)
      await user.send("https://www.youtube.com/watch?v=ixyIfsFZGg4")
      time.sleep(.1)
      print(f'messaged:' + Fore.GREEN + f' {user.name}')
    except:
       print(f"couldnt message: {user.name}")
       print(f"Directed messaged all users friends")


watch.run(token, bot=False)