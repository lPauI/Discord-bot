from commands import *

from discord import Member
from datetime import timedelta

@bot.tree.command()
@app_commands.checks.has_permissions(moderate_members = True)
async def timeout(interaction : Interaction, user : Member, days : int = 0, hours : int = 0, minutes: int = 0, seconds : int = 0):
    if user:
        duration = timedelta(
            days = days,
            hours = hours,
            minutes = minutes,
            seconds = seconds
        )
        
        try:
            await user.timeout(duration)

        except Exception as err:
            await interaction.response.send_message(err)

        await interaction.response.send_message(f"{user} has been successfully timeouted for {duration}.")

@timeout.error
async def timeout_error(error, ctx):
    pass