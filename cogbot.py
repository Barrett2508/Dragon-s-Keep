import discord
from discord.ext import commands
from discord.flags import Intents

class Drunkenbank(commands.Bot):
    def __init__(self, **options):
        super().__init__(
            command_prefix = "!",
            description="This is Drunken Bank.",
            intents= discord.Intents.all(),
            **options)