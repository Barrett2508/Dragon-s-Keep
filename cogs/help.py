import discord
from discord.ext import commands


class H(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def h(self, ctx):
        em = discord.Embed(title="Command Help", description = "Here is a list of commands:", color = ctx.author.color)
        em.add_field(name = "Games", value = "!dig \n !duel user_mention ak/stupefy/expelliarmus \n !ng number(0-10)", inline = False)
        em.add_field(name= "Economy", value="!bal", inline = False)
        em.add_field(name = "Moderation", value = "!rules \n !rule(num)", inline = False)
        await ctx.send(embed=em)
        return


def setup(bot):
    bot.add_cog(H(bot))
