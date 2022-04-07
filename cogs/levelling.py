import discord
from discord.ext import commands
import asyncio
import datetime
import sqlite3
import random
from math import *

class LvlCog(commands.Cog, name = 'Levelling'):
    def __init__(self, bot):
        self.bot = bot 


    @commands.Cog.listener()
    async def on_message(self, message):
        db = sqlite3.connect('levelling.sqlite')
        cursor = db.cursor()
        cursor.execute(f"SELECT user_id FROM levels WHERE guild_id = '{message.author.guild.id}' and user_id = '{message.author.id}' ")
        result = cursor.fetchone()
        if result is None:
            sql = ("INSERT INTO levels(guild_id, user_id, exp, lvl, bank) VALUES (?,?,?,?,?)")
            val = (message.author.guild.id, message.author.id, 2, 0, 100)
            cursor.execute(sql, val)
            db.commit()
        else:
            cursor.execute(f"SELECT user_id, exp, lvl, bank FROM levels WHERE guild_id = '{message.author.guild.id}' and user_id = '{message.author.id}'")
            result1 = cursor.fetchone()
            exp = int(result1[1])
            bank = int(result1[3])
            sql = ("UPDATE levels SET exp = ?, bank = ? WHERE guild_id =  ? and user_id = ?")
            val = (exp + 2, bank + 2, str(message.guild.id), str(message.author.id) )
            cursor.execute(sql, val)
            db.commit()

            cursor.execute(f"SELECT user_id, exp, lvl, inventory, bank FROM levels WHERE guild_id = '{message.author.guild.id}' and user_id = '{message.author.id}'")
            result2 = cursor.fetchone()

            xp_start = int(result2[1])
            lvl_start = int(result2[2])
            xp_end = floor(5 * (lvl_start ^ 2) + 50 * lvl_start + 100)
            if xp_end < xp_start:
                treasure = [None, None, None, None, None, "Green Chibi", None, None, None, None, None, None, None, "Blue Chibi",  None, None, None, None, None, None, None, "Purple Chibi",  None, None, None, None, None, None, None, None, "Yellow Chibi",  None, None, None, None, None, None, None, None, "Red Chibi",]
                prize = random.choice(treasure)

                em = discord.Embed(title=f"{message.author.name} Has levelled up to level: {lvl_start +1 }! :tada: ", description = "*Send messages in the discord to level up!*", color= message.author.color)
                em.add_field(name="**Level Up reward:**", value = f"{prize}")
                await message.channel.send(embed=em)
                sql = ("UPDATE levels SET lvl = ?  WHERE guild_id = ? and user_id = ?")
                val = (int(lvl_start + 1), str(message.guild.id), str(message.author.id))
                cursor.execute(sql, val)
                db.commit()
                sql = ("UPDATE levels SET exp = ? WHERE guild_id = ? and user_id = ?")
                val = (0, str(message.guild.id), str(message.author.id))
                cursor.execute(sql, val)
                db.commit()
                cursor.execute(sql, val)
                db.commit()
                cursor.close()
                db.close()
           




    @commands.command()
    async def rank(self, ctx, user:discord.User=None):
        if user is not None:
             db = sqlite3.connect('levelling.sqlite')
             cursor = db.cursor()
             cursor.execute(f"SELECT user_id, exp, lvl FROM levels WHERE guild_id = '{ctx.message.author.guild.id}' and user_id = '{ctx.message.author.id}' ")
             result = cursor.fetchone()
             if result is None:
                 await ctx.send("That user is not yet ranked!")
             else:
                 emb = discord.Embed(title = f"{ctx.author.name}'s Profile", description = f"**Rank**: `{str(result[2])}` \n **Exp**: `{str(result[1])}`", color = ctx.author.color)
                 emb.set_thumbnail(url = ctx.author.avatar_url)
                 emb.set_footer(text = "Send messages in the discord to level up!")
                 await ctx.send(embed = emb)
             cursor.close()
             db.close()
        elif user is None:
             db = sqlite3.connect('levelling.sqlite')
             cursor = db.cursor()
             cursor.execute(f"SELECT user_id, exp, lvl FROM levels WHERE guild_id = '{ctx.message.author.guild.id}' and user_id = '{ctx.message.author.id}' ")
             result = cursor.fetchone()
             if result is None:
                 await ctx.send("That user is not yet ranked!")
             else:
                 emb = discord.Embed(title = f"{ctx.author.name}'s Profile", description = f"**Rank**: `{str(result[2])}` \n **Exp**: `{str(result[1])}`", color = ctx.author.color)
                 emb.set_thumbnail(url = ctx.author.avatar_url)
                 emb.set_footer(text = "Send messages in the discord to level up!")
                 await ctx.send(embed = emb)
                 
             cursor.close()
             db.close()

        


def setup(bot):
    bot.add_cog(LvlCog(bot))
    print("Levelling is ready!")
