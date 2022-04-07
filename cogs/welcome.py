from discord.ext import commands
import asyncio
import random

class Reminder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def remind(self, ctx, a, *, b):
        msg = await ctx.send(f"I will remind you to {b} in {a} seconds")
        await asyncio.sleep(int(a)*60)
        
        newmessage = await ctx.fetch_message(msg.id)
        await ctx.send(f"{ctx.author.name.mention} You asked me to remind you to: {b}")


def setup(bot):
    bot.add_cog(Reminder(bot))
    print("reminders is ready!")
