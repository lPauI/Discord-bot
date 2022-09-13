from commands import *

from wmi import WMI

@bot.command()
async def ping(ctx, ip = ""):
    if ip:
        try:
            ip = str(ip)

            c = WMI()

            x = c.Win32_PingStatus(Address = ip)

            if x[0].StatusCode == 0:
                await ctx.send(f"Pinged {x[0].ProtocolAddress} ({x[0].Address}) and got reply in {x[0].ResponseTime} ms.")

            else:
                await ctx.send(f"{x[0].Address} is not replying.")

        except Exception as err:
            print(err)