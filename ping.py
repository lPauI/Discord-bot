from commands import *

from wmi import WMI

@bot.tree.command()
async def ping(interaction : Interaction, ip : str):
    if ip:
        c = WMI()

        x = c.Win32_PingStatus(Address = ip)

        if x[0].StatusCode == 0:
            await interaction.response.send_message(f"Pinged {x[0].ProtocolAddress} ({x[0].Address}) and got reply in {x[0].ResponseTime} ms.")

        else:
            await interaction.response.send_message(f"{x[0].Address} is not replying.")

@ping.error
async def ping_error(error, ctx):
    pass