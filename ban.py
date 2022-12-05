from commands import *

from discord import Member

@bot.tree.command()
@app_commands.checks.has_permissions(ban_members = True)
async def ban(interaction : Interaction, user: Member, reason : str):
    if user and reason:
        try:
            await interaction.guild.ban(user, reason = reason)

        except Exception as err:
            await interaction.response.send_message(err)

            return

        await interaction.response.send_message(f"{user} has been successfully banned.")

@ban.error
async def ban_error(error, ctx):
    pass