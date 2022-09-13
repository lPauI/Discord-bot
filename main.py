from help import *
from ping import *
from clear import *
from kick import *
from ban import *
from dale import *

@bot.event
async def on_ready():
    print(f"Bot {bot.user} is ready.")

from dotenv import load_dotenv
from os import getenv

load_dotenv()

bot.run(getenv("DISCORD_TOKEN"))