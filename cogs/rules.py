import discord
from discord.ext import commands

class RulesCog(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command()
    async def rules(self, ctx):
        embed = discord.Embed(title="Drunken Lullabies Server Rules", description="Any member found to be in breach of these rules will be banned!", color = ctx.author.color)
        embed.add_field(name="**Rule 1**", value ="Respect eachother and the admins at all times! No bullying/hate speech/harassment will be tolerated. Admin decisions are final.", inline=False)
        embed.add_field(name="**Rule 2 **", value ="No building in the following places, if you do, you will be wiped no warning! \n\n - Artefact Caves \n - Over explorer notes \n - On or near large resource spawns \n - Near mission terminals \n - In render of other players or obelisks. \n\n No stone dino gates/structures, use metal or wood or tek!", inline=False)
        embed.add_field(name="**Rule 3 **", value ="Tames left at an obelisk will be killed on sight, as will tames left on breeding/wandering!", inline=False)
        embed.add_field(name="**Rule 4 **", value ="Follow the correct procedure to get admin help!", inline=False)
        embed.add_field(name="**Rule 5 **", value ="No free items or dinos are to be given out, you may trade dinos for materials/blueprints or dinos.", inline=False)
        embed.add_field(name="**Rule 5 **", value ="A maximum of 2 bases per map, per tribe... including spawn huts!", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def rule1(self, ctx):
        em = discord.Embed(title="**Rule 1**",description="Respect eachother and the admins at all times! No bullying/hate speech/harassment will be tolerated. Admin decisions are final.", color=ctx.author.color)
        em.set_thumbnail(url = "https://cdn.discordapp.com/attachments/814328259524689951/917725913221840906/rules.png")
        await ctx.send(embed=em)

    @commands.command()
    async def rule2(self, ctx):
        em = discord.Embed(title="**Rule 2 **",description="No building in the following places, if you do, you will be wiped no warning! \n\n - Artefact Caves \n - Over explorer notes \n - On or near large resource spawns \n - Near mission terminals \n - In render of other players or obelisks. \n\n No stone dino gates/structures, use metal or wood or tek!", color=ctx.author.color)
        em.set_thumbnail(url = "https://cdn.discordapp.com/attachments/814328259524689951/917725913221840906/rules.png")
        await ctx.send(embed=em)

    @commands.command()
    async def rule3(self, ctx):
        em = discord.Embed(title="**Rule 3 **",description="Tames left at an obelisk will be killed on sight, as will tames left on breeding/wandering!", color=ctx.author.color)
        em.set_thumbnail(url = "https://cdn.discordapp.com/attachments/814328259524689951/917725913221840906/rules.png")
        await ctx.send(embed=em)

    @commands.command()
    async def rule4(self, ctx):
        em = discord.Embed(title="**Rule 4 **",description="Follow the correct procedure to get admin help", color=ctx.author.color)
        em.set_thumbnail(url = "https://cdn.discordapp.com/attachments/814328259524689951/917725913221840906/rules.png")
        await ctx.send(embed=em)

    @commands.command()
    async def rule5(self, ctx):
        em = discord.Embed(title="**Rule 5 **",description="No free items or dinos are to be given out, you may trade dinos for materials/blueprints or dinos", color=ctx.author.color)
        em.set_thumbnail(url = "https://cdn.discordapp.com/attachments/814328259524689951/917725913221840906/rules.png")
        await ctx.send(embed=em)

    @commands.command()
    async def rule6(self, ctx):
        em = discord.Embed(title="**Rule 5 **",description="A maximum of 2 bases per map, per tribe... including spawn huts", color=ctx.author.color)
        em.set_thumbnail(url = "https://cdn.discordapp.com/attachments/814328259524689951/917725913221840906/rules.png")
        await ctx.send(embed=em)


        
    
def setup(bot):
    bot.add_cog(RulesCog(bot))


   
    