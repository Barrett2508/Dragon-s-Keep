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
            
            db.commit()
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
                if int(lvl_start) >= 5:
                    treasure = "Green Chibi"
                elif int(lvl_start) >= 10:
                    treasure = "Blue Chibi"
                elif int(lvl_start) >= 15:
                    treasure = "Purple Chibi"
                elif int(lvl_start) >= 20:
                    treasure = "Yellow Chibi"
                            
                else:
                    if int(lvl_start) >= 21:
                        treasure = "Red Chibi"
                
                prize = treasure

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

            
            db = sqlite3.connect('levelling.sqlite')
            cursor = db.cursor()
            cursor.execute(f"SELECT user_id FROM bb WHERE guild_id = '{message.author.guild.id}' and user_id = '{message.author.id}' ")
            result = cursor.fetchone()
            if result is None:
                sql = ("INSERT INTO bb(user_id, guild_id, points) VALUES (?,?,?)")
                val = (message.author.id, message.author.guild.id, 1)
                cursor.execute(sql, val)
                db.commit()
                cursor.close()
                db.close()

    @commands.command()
    async def lb(self, ctx, user:discord.User=None):
            
            if user is not None:
                
      
                db = sqlite3.connect('levelling.sqlite')
                cursor = db.cursor()
                cursor.execute(f"SELECT user_id, points FROM bb WHERE guild_id = '{ctx.message.author.guild.id}' and user_id = '{ctx.message.author.id}' ")
                result = cursor.fetchone()
                if result is None:
                   await ctx.send("That user is not yet ranked!")
        
       

                else:
                    emb = discord.Embed(title = f"{ctx.author.name}'s Profile", description = f"**Points**: `{str(result[1])}` ", color = ctx.author.color)
                    emb.set_thumbnail(url = ctx.author.avatar_url)
                    emb.set_footer(text = "Fire spells to earn points!")
                    await ctx.send(embed = emb)
                    cursor.close()
                    db.close()

            elif user is None:
                db = sqlite3.connect('levelling.sqlite')
                cursor = db.cursor()
                cursor.execute(f"SELECT user_id, points FROM bb WHERE guild_id = '{ctx.message.author.guild.id}' and user_id = '{ctx.message.author.id}' ")
                result = cursor.fetchone()
                if result is None:
                   await ctx.send("That user is not yet ranked!")
        
       

                else:
                    emb = discord.Embed(title = f"{ctx.author.name}'s Profile", description = f"**Points**: `{str(result[1])}` ", color = ctx.author.color)
                    emb.set_thumbnail(url = ctx.author.avatar_url)
                    emb.set_footer(text = "Fire spells to earn points!")
                    await ctx.send(embed = emb)
                    cursor.close()
                    db.close()
            






    @commands.command()
    async def duel(self, ctx, target: discord.Member, a = str(), user:discord.User=None):
        choices = ["Stupefy", "Avada Kedavra", "Expelliarmus"]
        bot_choice = random.choice(choices)  
        db = sqlite3.connect('levelling.sqlite')
        cursor = db.cursor()
        cursor.execute(f"SELECT user_id, points FROM bb WHERE guild_id = '{ctx.message.author.guild.id}' and user_id = '{ctx.message.author.id}' ")
        result = cursor.fetchone()
        if result is None:
            return
        else:

            if a == "stupefy" and bot_choice == choices[0]:
              
                emb = discord.Embed(title =f"{ctx.author.name} fired Stupefy!", description = f"**{target.mention}'s Move = **" + '`' + bot_choice + '`', color =ctx.author.color)
                emb.add_field(name =f"You and {target.name} both stun eachother, scrambling to your feet you make your next move...\n ", value= "` **To Play Use: !duel ak | !duel expelliarmus | !duel stupefy`")
                emb.set_image(url = "https://c.tenor.com/HgJ8tf3h7YMAAAAC/hermione-granger.gif")  
                emb.set_thumbnail(url = ctx.author.avatar_url)             
                await ctx.send(embed=emb)     
                return


    
            if a == "stupefy" and bot_choice == choices[1]:
                emb = discord.Embed(title =f"{ctx.author.name} fired Stupefy!", description = f"**{target.mention}'s Move = **" + '`' + bot_choice + '`', color =ctx.author.color)
                emb.add_field(name =f"You fire the stunning spell, but it misses and {target.name} strikes you with the killing curse! \n Bot wins! \n", value= "`**To Play Use: !duel ak | !duel expelliarmus | !duel stupefy`")
                emb.set_image(url = "https://c.tenor.com/HgJ8tf3h7YMAAAAC/hermione-granger.gif")      
                emb.set_thumbnail(url = ctx.author.avatar_url)         
                await ctx.send(embed=emb)
                return
 
            if a == "stupefy" and bot_choice == choices[2]:
            
                
                emb = discord.Embed(title =f"{ctx.author.name} fired Stupefy!", description = f"**{target.mention}'s Move = **" + '`' + bot_choice + '`', color =ctx.author.color)
                emb.add_field(name =f"You fire the stunning spell, hitting {target.name} right in the kisser! {target.name} disarming spell hits you, you dive for your wand as {target.mention} scrambles to their feet... \n", value= "`**To Play Use: !duel ak | !duel expelliarmus | !duel stupefy`")
                emb.set_image(url = "https://c.tenor.com/HgJ8tf3h7YMAAAAC/hermione-granger.gif")      
                emb.set_thumbnail(url = ctx.author.avatar_url)
                db = sqlite3.connect('levelling.sqlite')
                cursor = db.cursor()
                cursor.execute(f"SELECT user_id, points FROM bb WHERE guild_id = '{ctx.message.author.guild.id}' and user_id = '{ctx.message.author.id}' ")
                result = cursor.fetchone()
                points =int(result[1])
                sql = ("UPDATE bb SET points = ? WHERE guild_id = ? and user_id = ?")
                val = (points+1, str(message.guild.id), str(message.author.id))
                cursor.execute(sql, val)
                db.commit()         
                db.close()
             
                await ctx.send(embed=emb)
                return


            if a == "ak" and bot_choice == choices[0]:
                emb = discord.Embed(title =f"{ctx.author.name} fired Avada Kedavra!", description = f"**{target.mention}'s Move = **" + '`' + bot_choice + '`', color =ctx.author.color)
                emb.add_field(name =f"You fire the killing curse, killing {target.name} easily, but {target.name}'s stunning spell hits making you an easy catch for the aurors as they escort you to Azkaban! \n ", value= "`**To Play Use: !duel ak | !duel expelliarmus | !duel stupefy`")
                emb.set_image(url = "https://c.tenor.com/TXCtsChJMgkAAAAd/dementors.gif")    
                emb.set_thumbnail(url = ctx.author.avatar_url)           
            
                await ctx.send(embed=emb)
                return
      
            if a == "ak" and bot_choice == choices[1]:
                emb = discord.Embed(title =f"{ctx.author.name} fired Avada Kedavra!", description = f"**{target.mention}'s Move = **" + '`' + bot_choice + '`', color =ctx.author.color)
                emb.add_field(name =f"You fire the killing curse, {target.name} also fires the killing curse, both spells strike killing eachother at the same time... Aurors find both bodies dead on the floor! \n", value= "`**To Play Use: !duel ak | !duel expelliarmus | !duel stupefy`")
                emb.set_image(url = "https://c.tenor.com/PZd-Va7JPp4AAAAC/bellatrix-avada-kedavra.gif")   
                emb.set_thumbnail(url = ctx.author.avatar_url)            
             
                await ctx.send(embed=emb)
                return
      
            if a == "ak" and bot_choice == choices[2]:
                emb = discord.Embed(title =f"{ctx.author.name} fired Avada Kedavra!", description = f"**{target.mention}'s Move = **" + '`' + bot_choice + '`', color =ctx.author.color)
                emb.add_field(name =f"You fire the killing curse, killing {traget.name}! {target.name}'s disarming spell hits leaving you diving for your wand before apperating away from the aurors! \n You win! \n ", value= "`**To Play Use: !duel ak | !duel expelliarmus | !duel stupefy`")
                emb.set_image(url = "https://c.tenor.com/Yw7crRWO3R0AAAAC/fantastic-beasts-fantastic-beasts-and-where-to-find-them.gif")          
                emb.set_thumbnail(url = ctx.author.avatar_url)     
             
                await ctx.send(embed=emb)
                return
       
            if a == "expelliarmus" and bot_choice == choices[0]:
                emb = discord.Embed(title =f"{ctx.author.name} fired Expelliarmus!", description = f"**{target.mention}'s Move = **" + '`' + bot_choice + '`', color =ctx.author.color)
                emb.add_field(name =f"You fire the disarming spell, while {target.name} used the stunning spell, you both scramble for your wands....\n", value= "`**To Play Use: !duel ak | !duel expelliarmus | !duel stupefy`")
                emb.set_image(url = "https://c.tenor.com/rs_rWRuIKPkAAAAC/harry-potter-magic.gif")       
                emb.set_thumbnail(url = ctx.author.avatar_url)        
             
                await ctx.send(embed=emb)
                return
      
            if a == "expelliarmus" and bot_choice == choices[1]:
                emb = discord.Embed(title =f"{ctx.author.name} fired Expelliarmus!", description = f"**{target.mention}'s Move = **" + '`' + bot_choice + '`', color =ctx.author.color)
                emb.add_field(name =f"You fire the disarming spell, but {target.name} used the killing curse! {target.name}'s spell hits you right in the kisser killing you instantly! \n {target.name} Wins! \n", value= "`**To Play Use: !duel ak | !duel expelliarmus | !duel stupefy `")
                emb.set_image(url = "https://c.tenor.com/rs_rWRuIKPkAAAAC/harry-potter-magic.gif")          
                emb.set_thumbnail(url = ctx.author.avatar_url)     
               
                await ctx.send(embed=emb)
                return
      
            if a == "expelliarmus" and bot_choice == choices[2]:
                emb = discord.Embed(title =f"{ctx.author.name} fired Expelliarmus!", description = f"**{target.mention}'s Move = **" + '`' + bot_choice + '`', color =ctx.author.color)
                emb.add_field(name =f"You fire the disarming spell, as did {target.name}, you both scramble for your wands... \n", value= "`**To Play Use: !duel ak | !duel expelliarmus | !duel stupefy `")
                emb.set_image(url = "https://c.tenor.com/rs_rWRuIKPkAAAAC/harry-potter-magic.gif")          
                emb.set_thumbnail(url = ctx.author.avatar_url)   
             
                await ctx.send(embed=emb)
                return
        

        


def setup(bot):
    bot.add_cog(LvlCog(bot))
    print("Levelling is ready!")
