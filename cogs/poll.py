import discord 
from discord.ext import commands
import random
import asyncio 


class Poll(commands.Cog):
    def __init__(self,bot:commands.Bot):
        self.Bot = bot
    
    @commands.command()
    @commands.has_role("Admin")
    async def poll(self, ctx, choice1, choice2,*,topic):

        emb = discord.Embed(title = topic, description = f":one: {choice1} \n\n :two: {choice2}", color=ctx.author.color)
        msg = await ctx.send(embed=emb)

        await msg.add_reaction("1️⃣")
        await msg.add_reaction("2️⃣")
        await asyncio.sleep(60*120)

        newmessage = await ctx.fetch_message(msg.id)
        onechoice = await newmessage.reactions[0].users().flatten()
        secchoice = await newmessage.reactions[1].users().flatten()

        result = "TIE"

        if len(onechoice)>len(secchoice):
            result = choice1

        elif len(secchoice)>len(onechoice):
            result = choice2

        else:
            result = result

        emb = discord.Embed(title = topic, description = f"result : {result}", color=ctx.author.color)

        await newmessage.edit(embed = emb)

def setup(bot):
    bot.add_cog(Poll(bot))


