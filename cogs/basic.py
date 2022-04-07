import discord
from discord.ext import commands
import random
import json
import sqlite3




class Basic(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        

    


    @commands.Cog.listener()
    async def on_ready(self):
        db = sqlite3.connect('main.sqlite')
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS main(
            guild_id TEXT,
            msg TEXT,
            channel_id TEXT
            )
            ''')
        print("Logged in as {bot.user}")
      

      



def setup(bot):
    bot.add_cog(Basic(bot))