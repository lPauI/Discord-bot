from commands import *

@bot.command()
async def cmd(ctx):
    try:
        channel = await ctx.author.create_dm()

        await channel.send("```Command prefix: '$'\n\n\
    $ping <ip address / dns>\n\
    $clear <num of mesagess>\n\
    $kick <user id>\n\
    $ban <user id>```")
        
    except Exception as err:
        print(err)