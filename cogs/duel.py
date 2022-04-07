import discord
from discord.ext import commands
import random




class Duel(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command()
    

    async def duel(self, ctx, target: discord.Member, a = str()):
        choices = ["Stupefy", "Avada Kedavra", "Expelliarmus"]
        bot_choice = random.choice(choices)  

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
    bot.add_cog(Duel(bot))
    print("Duel is ready!")