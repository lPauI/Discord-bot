from commands import *

from discord import Member

@bot.command()
async def kick(ctx, user : Member = "", reas = ""):
    if user and reas:
        try:
            await ctx.guild.kick(user, reason = reas)
            await ctx.send(f"{user} has been successfully kicked.")

        except Exception as err:
            await ctx.send(err)