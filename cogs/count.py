import discord
from discord.ext import commands
import random




class Count(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command()
    async def count(self, ctx, a):
        a = int(a)

        while a in range(1000000):
            
            await ctx.send(a + 1)
            return

def setup(bot):
    bot.add_cog(Count(bot))
    print("Duel is ready!")