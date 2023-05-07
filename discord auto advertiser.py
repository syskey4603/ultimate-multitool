import os
from colorama import init, Fore as cc
os.system('pip install -U discord==1.7.3')
os.system('pip install -U discord.py==1.7.3')
print("Loading....")
print("executing modules")
username = input("The program calls for your name ")
print("Welcome")
print(username)
import discord, asyncio
g = G = cc.LIGHTGREEN_EX
print = f"""
{g}  _____                        __                    
_/ ____\_________  ___  ______|  | __  ____  ___.__. 
\   __\/  ___/\  \/  / /  ___/|  |/ /_/ __ \<   |  | 
 |  |  \___ \  >    <  \___ \ |    < \  ___/ \___  | 
 |__| /____  >/__/\_ \/____  >|__|_ \ \___  >/ ____| 
           \/       \/     \/      \/     \/ \/          {g}

Made By Frazy*-*#4051 want more tools? join https://discord.gg/rMa8jRPz
"""

                   
token = 'your token' # https://www.youtube.com/watch?v=YEgFvgg7ZPI
replyMessage = 'your message after the user dms you' # Message to reply with when somebody DMs the token.
mainMessage = 'channel message' # Message to send in the channel.
channelId = id # Channel ID to send the messages in.
delay = 60 # Delay between each message in seconds.

class Main(discord.Client):
    async def on_ready(self): 
        print('Logged in as %s.' % self.user)
        while True:
            channel = self.get_channel(channelId)
            await channel.send(mainMessage)
            print('Sent message in #%s.' % channel.name)
            await asyncio.sleep(delay)

    async def on_message(self, message):
        if isinstance(message.channel, discord.DMChannel):
            if message.author.id != self.user.id:
                with open('blacklist.txt', 'r', encoding = 'UTF-8') as file:
                    if str(message.author.id) not in file.read():
                        await message.reply(replyMessage)
                        print('Replied to %s.' % message.author.name)
                        with open('blacklist.txt', 'a', encoding = 'UTF-8') as file:
                            file.write('%s\n' % message.author.id)

if __name__ == '__main__':
    Main().run(token, bot = False)