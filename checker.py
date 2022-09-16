try:
    import discord

except:
    from os import system

    system("pip3 install discord")

try:
    import wmi

except:
    from os import system

    system("pip3 install wmi")

try:
    import dotenv

except:
    from os import system

    system("pip3 install python-dotenv")

from os import system

if system("cls") == True:
    system("clear")