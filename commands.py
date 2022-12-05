from discord import Intents, Client, app_commands

class Interaction(Client):
    def __init__(self, *, intents: Intents):
        super().__init__(intents = intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self) -> None:
        await self.tree.sync(guild = None)

bot = Interaction(intents = Intents.all())