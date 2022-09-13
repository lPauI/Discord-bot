from commands import *

from discord import Member

@bot.command()
async def ban(ctx, user: Member = "", reas = ""):
    if Member and reas:
        try:
            await ctx.guild.ban(user, reason = reas)
            await ctx.send(f"{user} has been successfully banned.")

        except Exception as err:
            await ctx.send(err)