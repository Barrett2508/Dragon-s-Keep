import discord
from discord.colour import Color
from discord.ext import commands, tasks
import datetime
import os
import random
import json
from cogbot import Drunkenbank
import sqlite3
import asyncio






if __name__ == "__main__":
    bot = Drunkenbank()

   

    for name in os.listdir("./cogs"):
        if name.endswith(".py"):
            bot.load_extension("cogs.{}".format(name[:-3]))
    

    bot.run("OTEzNDQzMzkzMDAxMTAzNDAx.YZ-kcw.uZSEvSHanr4BiWjLw-yShpiyud0")
