from commands import *

@bot.tree.command()
@app_commands.checks.has_permissions(manage_messages = True)
async def clear(interaction : Interaction, limit : int):
    if limit:
        await interaction.response.send_message(f"{limit} messages will be deleted.")
        
        async for message in interaction.channel.history(limit = limit):
            msg = await interaction.channel.fetch_message(message.id)
            await msg.delete()

@clear.error
async def clear_error(error, ctx):
    pass