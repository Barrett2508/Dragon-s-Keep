import discord
from discord.ext import commands 
import asyncio 
import datetime 
import random 

class Auctions(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command()
    async def auction(self, ctx, choice1, choice2, * , item):
       
        emb = discord.Embed(title = f" NEW AUCTION: {item}", description = f"Starting Bid: {choice1} | Material: {choice2}  ", color = ctx.author.color)
        msg = await ctx.send(embed=emb)
        await asyncio.sleep(86400)

        newmessage = await ctx.fetch_message(msg.id)
        em = discord.Embed(title = item, description = f"`The auction has now ended`, SELLER please contact the WINNER to arrange payment!", color=ctx.author.color)
        await newmessage.edit(embed = em)

def setup(bot):
    bot.add_cog(Auctions(bot))




        




