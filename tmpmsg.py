from commands import *

from asyncio import sleep as tmpsleep

async def delete_dialog(ctx, msg, time):
    await tmpsleep(time)

    await msg.delete()
    await ctx.message.delete()