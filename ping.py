from commands import *
from ping3 import ping

@bot.tree.command()
async def ping(interaction: Interaction, ip: str):
    if ip:
        try:
            response_time = ping(ip)
            if response_time is not None:
                await interaction.response.send_message(f"Pinged {ip} and got reply in {response_time * 1000:.2f} ms.")
            else:
                await interaction.response.send_message(f"{ip} is not replying.")
        except Exception as e:
            await interaction.response.send_message(f"Ping error: {e}")

@ping.error
async def ping_error(error, ctx):
    pass