import discord
from discord.ext import commands
import asyncio
import random 
import sqlite3





class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def bal(self, ctx, user:discord.User=None):
        if user is not None:
             db = sqlite3.connect('levelling.sqlite')
             cursor = db.cursor()
             cursor.execute(f"SELECT user_id, exp, lvl, inventory, bank FROM levels WHERE guild_id = '{ctx.message.author.guild.id}' and user_id = '{ctx.message.author.id}' ")
             result = cursor.fetchone()
             if result is None:
                 await ctx.send("That user has not got an account!")
             else:
                 emb = discord.Embed(title = f"{ctx.author.name}'s Profile", description = f"{ctx.author.name}'s Profile", color = ctx.author.color)
                 emb.set_thumbnail(url = ctx.author.avatar_url)
                 emb.add_field(name="Coins:", value=f"{str(result[4])}", inline = False)
                 emb.add_field(name="Level:", value =f"{str(result[2])}", inline = False)
                 emb.add_field(name="Exp:", value = f"{str(result[1])}", inline = False)
                 emb.add_field(name="Items:", value = f"{str(result[3])}", inline = False)
                 emb.set_footer(text = "Earn coins in giveaways, by digging or by donating!")
                 await ctx.send(embed = emb)
             cursor.close()
             db.close()
        elif user is None:
             db = sqlite3.connect('levelling.sqlite')
             cursor = db.cursor()
             cursor.execute(f"SELECT user_id, exp, lvl, inventory, bank FROM levels WHERE guild_id = '{ctx.message.author.guild.id}' and user_id = '{ctx.message.author.id}' ")
             result = cursor.fetchone()
             if result is None:
                 await ctx.send("That user is not yet ranked!")
             else:
                 emb = discord.Embed(title = f"{ctx.author.name}'s Profile", description = f"{ctx.author.name}'s Profile", color = ctx.author.color)
                 emb.set_thumbnail(url = ctx.author.avatar_url)
                 emb.add_field(name="Coins:", value=f"{str(result[4])}", inline =False)
                 emb.add_field(name="Level:", value =f"{str(result[2])}", inline = False)
                 emb.add_field(name="Exp:", value = f"{str(result[1])}", inline = False)
                 emb.add_field(name="Items:", value = f"{str(result[3])}", inline = False)
                 emb.set_footer(text = "Earn coins in giveaways, by digging or by donating!")
                 await ctx.send(embed = emb)
                 cursor.close()
                 db.close()
        
                 
                 
             cursor.close()
             db.close()
      

def setup(bot):
    bot.add_cog(Economy(bot))
    print("Economy is ready!")

