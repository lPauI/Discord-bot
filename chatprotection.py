from commands import *

from time import time
from threading import Timer
from re import findall

LastMessage = {}
UserTempWarn = {}
rtw = {}

def Find(string):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = findall(regex, string)      
    return [x[0] for x in url]

def ResetTempWarns(author):
    UserTempWarn[author] = 0

@bot.event
async def on_message(msg):
    if msg.author.id == bot.user.id:
        return

    try:
        msg.guild.id

    except:
        return

    if Find(msg.content):
        await msg.delete()

    try:
        LastMessage[msg.author.id]

    except:
        LastMessage[msg.author.id] = 0

    if time() - LastMessage[msg.author.id] <= 0.5:
        try:
            UserTempWarn[msg.author.id]
            
        except:
            UserTempWarn[msg.author.id] = 0

        UserTempWarn[msg.author.id] += 1

        try:
            if rtw[msg.author.id]:
                rtw[msg.author.id].cancel()

        except:
            pass

        if UserTempWarn[msg.author.id] >= 3:
            await msg.channel.send('slow down')
            
            ResetTempWarns(msg.author.id)

        else:
            rtw[msg.author.id] = Timer(3.0, ResetTempWarns, args = [msg.author.id])
            rtw[msg.author.id].start()

    LastMessage[msg.author.id] = time()

    await bot.process_commands(msg)