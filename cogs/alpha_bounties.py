import discord
from discord.ext import commands
import random



class alphaBounty(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
    
    @commands.command()
    

    async def ab(self, ctx):
        ab = ["Amargasaurus", "Astrocetus", "Astrodelphis", "Onyc", "Noglin", "Ice Titan", "Forest Titan", "Ferox", "Giganotosaurus", "Karkinos", "Magmasaur", "Liopleurodon", "Quetzal", "Reaper", "T-Rex", "Tek-Stryder", "Therizino", "Titanosaur", "Desert Titan", "Tusoteuthis"]
        bty = random.choice(ab)
        rewards = ["2000 Drunken-Coins", "3000 Drunken-Coins", "4000 Drunken-Coins"]
        rwd = random.choice(rewards)
      
        if bty == ab[0]:
            emb = discord.Embed(title = f"{ctx.author.name}'s target = `{bty}`", description = f"Catch a max level **{bty}** and bring to an admin to claim `{rwd}`", color = ctx.author.color)
            emb.set_image(url = "https://cdn.discordapp.com/attachments/885874905722261525/954700769456713738/ama.png")
            emb.set_thumbnail(url = ctx.author.avatar_url)
            await ctx.send(embed = emb)
      
        if bty == ab[1]:
            emb = discord.Embed(title = f"{ctx.author.name}'s target = `{bty}`", description = f"Catch a max level **{bty}** and bring to an admin to claim `{rwd}`", color = ctx.author.color)
            emb.set_image(url = "https://cdn.discordapp.com/attachments/885874905722261525/954707272691503144/ASTROCETUS_1.png")
            emb.set_thumbnail(url = ctx.author.avatar_url)
            await ctx.send(embed = emb)
      
        if bty == ab[2]:
            emb = discord.Embed(title = f"{ctx.author.name}'s target = `{bty}`", description = f"Catch a max level **{bty}** and bring to an admin to claim `{rwd}`", color = ctx.author.color)
            emb.set_image(url = "https://cdn.discordapp.com/attachments/885874905722261525/954707273052192778/ASTROde.png")
            emb.set_thumbnail(url = ctx.author.avatar_url)
            await ctx.send(embed = emb)
      
        if bty == ab[3]:
            emb = discord.Embed(title = f"{ctx.author.name}'s target = `{bty}`", description = f"Catch a max level **{bty}** and bring to an admin to claim `{rwd}`", color = ctx.author.color)
            emb.set_image(url = "https://cdn.discordapp.com/attachments/885874905722261525/954707273400344586/bat.png")
            emb.set_thumbnail(url = ctx.author.avatar_url)
            await ctx.send(embed = emb)
       
        if bty == ab[4]:
            emb = discord.Embed(title = f"{ctx.author.name}'s target = `{bty}`", description = f"Catch a max level **{bty}** and bring to an admin to claim `{rwd}`", color = ctx.author.color)
            emb.set_image(url = "https://cdn.discordapp.com/attachments/885874905722261525/954707273672953866/chelon_1.png")
            emb.set_thumbnail(url = ctx.author.avatar_url)
            await ctx.send(embed = emb)
       
        if bty == ab[5]:
            emb = discord.Embed(title = f"{ctx.author.name}'s target = `{bty}`", description = f"Catch a max level **{bty}** and bring to an admin to claim `{rwd}`", color = ctx.author.color)
            emb.set_image(url = "https://cdn.discordapp.com/attachments/885874905722261525/954707274054639656/f_titan_1.png")
            emb.set_thumbnail(url = ctx.author.avatar_url)
            await ctx.send(embed = emb)
       
        if bty == ab[6]:
            emb = discord.Embed(title = f"{ctx.author.name}'s target = `{bty}`", description = f"Catch a max level **{bty}** and bring to an admin to claim `{rwd}`", color = ctx.author.color)
            emb.set_image(url = "https://cdn.discordapp.com/attachments/885874905722261525/954707274507649055/f_titan.png")
            emb.set_thumbnail(url = ctx.author.avatar_url)
            await ctx.send(embed = emb)
       
        if bty == ab[7]:
            emb = discord.Embed(title = f"{ctx.author.name}'s target = `{bty}`", description = f"Catch a max level **{bty}** and bring to an admin to claim `{rwd}`", color = ctx.author.color)
            emb.set_image(url = "https://cdn.discordapp.com/attachments/885874905722261525/954707274998353982/ferox_1.png")
            emb.set_thumbnail(url = ctx.author.avatar_url)
            await ctx.send(embed = emb)

        if bty == ab[8]:
            emb = discord.Embed(title = f"{ctx.author.name}'s target = `{bty}`", description = f"Catch a max level **{bty}** and bring to an admin to claim `{rwd}`", color = ctx.author.color)
            emb.set_image(url = "https://cdn.discordapp.com/attachments/885874905722261525/954713470564184085/giga.png")
            emb.set_thumbnail(url = ctx.author.avatar_url)
            await ctx.send(embed = emb)
        
        if bty == ab[9]:
            emb = discord.Embed(title = f"{ctx.author.name}'s target = `{bty}`", description = f"Catch a max level **{bty}** and bring to an admin to claim `{rwd}`", color = ctx.author.color)
            emb.set_image(url = "https://cdn.discordapp.com/attachments/885874905722261525/954713471080075364/karkinos_1.png")
            emb.set_thumbnail(url = ctx.author.avatar_url)
            await ctx.send(embed = emb)
        
        if bty == ab[10]:
            emb = discord.Embed(title = f"{ctx.author.name}'s target = `{bty}`", description = f"Catch a max level **{bty}** and bring to an admin to claim `{rwd}`", color = ctx.author.color)
            emb.set_image(url = "https://cdn.discordapp.com/attachments/885874905722261525/954713471872819260/karkinos_2.png")
            emb.set_thumbnail(url = ctx.author.avatar_url)
            await ctx.send(embed = emb)

        if bty == ab[11]:
            emb = discord.Embed(title = f"{ctx.author.name}'s target = `{bty}`", description = f"Catch a max level **{bty}** and bring to an admin to claim `{rwd}`", color = ctx.author.color)
            emb.set_image(url = "https://cdn.discordapp.com/attachments/885874905722261525/954713472321613834/liop.png")
            emb.set_thumbnail(url = ctx.author.avatar_url)
            await ctx.send(embed = emb)

        if bty == ab[12]:
            emb = discord.Embed(title = f"{ctx.author.name}'s target = `{bty}`", description = f"Catch a max level **{bty}** and bring to an admin to claim `{rwd}`", color = ctx.author.color)
            emb.set_image(url = "https://cdn.discordapp.com/attachments/885874905722261525/954713472736837694/quetz.png")
            emb.set_thumbnail(url = ctx.author.avatar_url)
            await ctx.send(embed = emb)

        if bty == ab[13]:
            emb = discord.Embed(title = f"{ctx.author.name}'s target = `{bty}`", description = f"Catch a max level **{bty}** and bring to an admin to claim `{rwd}`", color = ctx.author.color)
            emb.set_image(url = "https://cdn.discordapp.com/attachments/885874905722261525/954713473261129728/reap.png")
            emb.set_thumbnail(url = ctx.author.avatar_url)
            await ctx.send(embed = emb)


        if bty == ab[14]:
            emb = discord.Embed(title = f"{ctx.author.name}'s target = `{bty}`", description = f"Catch a max level **{bty}** and bring to an admin to claim `{rwd}`", color = ctx.author.color)
            emb.set_image(url = "https://cdn.discordapp.com/attachments/885874905722261525/954713473672183839/rex_1.png")
            emb.set_thumbnail(url = ctx.author.avatar_url)
            await ctx.send(embed = emb)

        if bty == ab[15]:
            emb = discord.Embed(title = f"{ctx.author.name}'s target = `{bty}`", description = f"Catch a max level **{bty}** and bring to an admin to claim `{rwd}`", color = ctx.author.color)
            emb.set_image(url = "https://cdn.discordapp.com/attachments/885874905722261525/954713474271936592/rex_2.png")
            emb.set_thumbnail(url = ctx.author.avatar_url)
            await ctx.send(embed = emb)

        if bty == ab[16]:
            emb = discord.Embed(title = f"{ctx.author.name}'s target = `{bty}`", description = f"Catch a max level **{bty}** and bring to an admin to claim `{rwd}`", color = ctx.author.color)
            emb.set_image(url = "https://cdn.discordapp.com/attachments/885874905722261525/954713474733338634/theri.png")
            emb.set_thumbnail(url = ctx.author.avatar_url)
            await ctx.send(embed = emb)


        if bty == ab[17]:
            emb = discord.Embed(title = f"{ctx.author.name}'s target = `{bty}`", description = f"Catch a max level **{bty}** and bring to an admin to claim `{rwd}`", color = ctx.author.color)
            emb.set_image(url = "https://cdn.discordapp.com/attachments/885874905722261525/954713475278590003/titano.png")
            emb.set_thumbnail(url = ctx.author.avatar_url)
            await ctx.send(embed = emb)


        if bty == ab[18]:
            emb = discord.Embed(title = f"{ctx.author.name}'s target = `{bty}`", description = f"Catch a max level **{bty}** and bring to an admin to claim `{rwd}`", color = ctx.author.color)
            emb.set_image(url = "https://cdn.discordapp.com/attachments/885874905722261525/954713484946452511/tuso_1.png")
            emb.set_thumbnail(url = ctx.author.avatar_url)
            await ctx.send(embed = emb)


        if bty == ab[19]:
            emb = discord.Embed(title = f"{ctx.author.name}'s target = `{bty}`", description = f"Catch a max level **{bty}** and bring to an admin to claim `{rwd}`", color = ctx.author.color)
            emb.set_image(url = "https://cdn.discordapp.com/attachments/885874905722261525/954713485307166792/tuso.png")
            emb.set_thumbnail(url = ctx.author.avatar_url)
            await ctx.send(embed = emb)

        
            

def setup(bot):
    bot.add_cog(alphaBounty(bot))