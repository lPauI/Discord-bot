from commands import *

from wmi import WMI

from tmpmsg import delete_dialog

@bot.command()
async def ping(ctx, ip = ""):
    if ip:
        try:
            ip = str(ip)

            c = WMI()

            x = c.Win32_PingStatus(Address = ip)

            if x[0].StatusCode == 0:
                msg = await ctx.send(f"Pinged {x[0].ProtocolAddress} ({x[0].Address}) and got reply in {x[0].ResponseTime} ms.")

            else:
                msg = await ctx.send(f"{x[0].Address} is not replying.")

            await delete_dialog(ctx, msg, 3)

        except Exception as err:
            print(err)