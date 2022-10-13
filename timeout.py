from commands import *

from discord import Member
from datetime import timedelta

@bot.command()
async def timeout(ctx, member : Member = "", time = ""):
    if time:
        try:
            await member.timeout(timedelta(
                minutes = time
            ))

        except Exception as err:
            print(err)