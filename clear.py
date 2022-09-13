from commands import *

@bot.command()
async def clear(ctx, number = ""):
    if number:
        try:
            number = int(number)
        
            async for message in ctx.history(limit = number):
                msg = await ctx.fetch_message(message.id)
                await msg.delete()

        except Exception as err:
            print(err)