from commands import *

from discord import Member

@bot.tree.command()
@app_commands.checks.has_permissions(kick_members = True)
async def kick(interaction : Interaction, user : Member, reason : str):
    if user and reason:
        try:
            await interaction.guild.kick(user, reason = reason)

        except Exception as err:
            await interaction.response.send_message(err)

        await interaction.response.send_message(f"{user} has been successfully kicked.")

@kick.error
async def kick_error(error, ctx):
    pass