import os
import discord
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()


class Manager(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="/",
            help_command=None,
            intents=discord.Intents.all(),
            application=os.getenv("DISCORD_APPLICATION_ID")
        )
    
    async def setup_hook(self):
        for filename in os.listdir("./src/modules"):
            if filename.endswith(".py") and not filename.startswith("_"):
                await self.load_extension(f"src.modules.{filename[:-3]}")
        await bot.tree.sync()
        await bot.tree.sync(
            guild=discord.Object(id=os.getenv("DISCORD_GUILD_ID"))
        )


bot = Manager()
bot.run(os.getenv("DISCORD_TOKEN"))