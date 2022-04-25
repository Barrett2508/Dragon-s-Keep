import discord
from discord.ext import commands
import random
import asyncio
import sqlite3


class Dig(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send('>`You are tired of digging today, try again in:` ` %.2fs `' % error.retry_after)
            return
        

    @commands.command()
    @commands.cooldown(2, 86400, commands.BucketType.user)
    @commands.has_role("Admin")
    
    async def dig(self, ctx):
        treasure = [None, None, None, None, None, "Green Chibi", None, None, None, None, None, None, None, "Blue Chibi",  None, None, None, None, None, None, None, "Purple Chibi",  None, None, None, None, None, None, None, None, "Yellow Chibi",  None, None, None, None, None, None, None, None, "Red Chibi", ]

        box = random.choice(treasure)

        if box == None:
          emb = discord.Embed(title = f"{ctx.author.name} Dug for treausre!", description = "Unlucky! You did not find any treasure this time! Try again!", color = ctx.author.color)
          emb.set_image(url = "https://cdn.discordapp.com/attachments/828403466073800704/956617022656102490/Complete.png")
          await ctx.send(embed = emb)
          return

        if box == treasure[5]:
          emb = discord.Embed(title = f"{ctx.author.name} Dug for treausre!", description = "Congratulations, You won a green chibi!", color = ctx.author.color)
          emb.set_image(url = "https://cdn.discordapp.com/attachments/828403466073800704/956625753091502100/Green_Box_V2.png")
          await ctx.send(embed = emb)
          return
        
        if box == treasure[13] :
          emb = discord.Embed(title = f"{ctx.author.name} Dug for treausre!", description = "Congratulations, You won a blue chibi!", color = ctx.author.color)
          emb.set_image(url = "https://cdn.discordapp.com/attachments/828403466073800704/956625847517843556/Blue_Box_V2.png")
          await ctx.send(embed = emb)
          return

        if box == treasure[19]:
           emb = discord.Embed(title = f"{ctx.author.name} Dug for treausre!", description = "Congratulations, You won a purple chibi!", color = ctx.author.color)
           emb.set_image(url = "https://cdn.discordapp.com/attachments/828403466073800704/956620200940298240/Purp_Box.png")
           await ctx.send(embed = emb)
           return

        if box == treasure[28]:
          emb = discord.Embed(title = f"{ctx.author.name} Dug for treausre!", description = "Congratulations, You won a Yellow chibi!", color = ctx.author.color)
          emb.set_image(url = "https://cdn.discordapp.com/attachments/828403466073800704/956625817750884382/YellowBox_V2.png")
          await ctx.send(embed = emb)
          return

        if box == treasure[37]:
            emb = discord.Embed(title = f"{ctx.author.name} Dug for treausre!", description = "Congratulations, You won a red chibi!", color = ctx.author.color)
            emb.set_image(url = "https://cdn.discordapp.com/attachments/828403466073800704/956625727229407252/Red_Box_V2.png")
            await ctx.send(embed = emb)
            return



def setup(bot):
    bot.add_cog(Dig(bot))
