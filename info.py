from commands import *

from discord import Member

from time import time

@bot.command()
async def info(ctx, member : Member):
    await ctx.send(f"{(time() - member.created_at.timestamp()) / 365}")