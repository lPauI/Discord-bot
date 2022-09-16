from commands import *

from discord import Member

from time import time

@bot.command()
async def info(ctx, member : Member):
    await ctx.send(f"Info about {member.mention}:\n\
Account was created {(time() - member.created_at.timestamp()) / 86400} days ago.")