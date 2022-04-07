import discord
from discord.ext import commands
import random
import asyncio
import sqlite3


class Warn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_role("Admin")
    async def warn(self, ctx, target: discord.Member, b):
        
        em = discord.Embed(title= f"{ctx.author.name} issued a warning to {target.name}!", description =f"Warning sent by: {ctx.author.name} \n Sent to: {target.name} \n Reason: {b}", color=ctx.author.color)
        await ctx.send(embed=em)

        db = sqlite3.connect('warnings.db')
        cursor = db.cursor()
        cursor.execute(f"SELECT userid, warns FROM warnings WHERE userid = '{target.name}'")
        result = cursor.fetchone()
        warns = int(result[1])
        
        if result is None:
            sql = ("INSERT INTO warnings(userid, warns) VALUES (?,?)")
            val = (target.name, warns + 1)
            cursor.execute(sql, val)
            db.commit()

        if int(warns) <= 1:
            await ctx.send(f" {target.name} This is your first warning!")
        
        if int(warns) <= 2:
            await ctx.send(f"{target.name} This is your second warning, 3 strikes you're out! 🚩")
            sql = (f"UPDATE warnings SET warns = ? WHERE userid = ?")
            val = (warns + 1, target.id)
            cursor.execute(sql, val)
            db.commit()


            



def setup(bot):
    bot.add_cog(Warn(bot))
    print("Economy is ready!")
