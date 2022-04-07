import discord
from discord.ext import commands
import random 

class Shootout(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command(aliases = ["so"])
    async def shootout(self, ctx, a = str()):
        choices = ["Shoot", "Dodge", "Bluff"]
        bot_choice = random.choice(choices)
        user_choice = random.choice(choices)
        if a == "shoot" and bot_choice == choices[0]:
            await ctx.send("You both killed eachother, nobody wins!")
            await ctx.send(f"{ctx.author.name}'s move = "+ a)
            await ctx.send("Bots move = " + bot_choice)
            return
        if a == "shoot" and bot_choice == choices[1]:
            await ctx.send("The bot drops to the ground, avoiding your only bullet before taking the kill itself! Bot Wins!")
            await ctx.send(f"{ctx.author.name}'s move = "+ a)
            await ctx.send("Bots move = " + bot_choice)
            return
        if a == "shoot" and bot_choice == choices[2]:
            await ctx.send("The bot bluffs the shot, but you pulled the trigger shooting it right in the face! You won!")
            await ctx.send(f"{ctx.author.name}'s move = "+ a)
            await ctx.send("Bots move = " + bot_choice)
            return
        if a == "dodge" and bot_choice == choices[0]:
            await ctx.send("You drop to the ground, avoiding the bots only bullet before taking the kill for yourself!")
            await ctx.send(f"{ctx.author.name}'s move = "+ a)
            await ctx.send("Bots move = " + bot_choice)
            return
        if a == "dodge" and bot_choice == choices[1]:
            await ctx.send("You both drop to the ground, looking rather silly, the bot aims harshly, shoots and misses before you take the kill for yourself! You won!")
            await ctx.send(f"{ctx.author.name}'s move = "+ a)
            await ctx.send("Bots move = " + bot_choice)
            return
        if a == "dodge" and bot_choice == choices[2]:
            await ctx.send("You drop to the ground, looking rather like a ninja, the bot stares you dead in the eye, finger on trigger before you take the kill for yourself by shooting out its battery pack! You won!")
            await ctx.send(f"{ctx.author.name}'s move = "+ a)
            await ctx.send("Bots move = " + bot_choice)    
            return
        if a == "bluff" and bot_choice == choices[0]:
            await ctx.send("You bluff staring the bot dead in the eyes... But the bot brutally shoots you right in the face! Bot wins!")
            await ctx.send(f"{ctx.author.name}'s move = "+ a)
            await ctx.send("Bots move = " + bot_choice)
            return
        if a == "bluff" and bot_choice == choices[1]:
            await ctx.send("You bluff, the bot drops to the ground looking rather silly, before landing a bullet right between your eyes to take the win! Bot won!")
            await ctx.send(f"{ctx.author.name}'s move = "+ a)
            await ctx.send("Bots move = " + bot_choice)
            return
        if a == "bluff" and bot_choice == choices[2]:
            await ctx.send("You bluff, so does the bot! You are staring eachother dead in the eye when a raptor runs from the woods and kills the bot, allowing you to run and take the win! You won!")
            await ctx.send(f"{ctx.author.name}'s move = "+ a)
            await ctx.send("Bots move = " + bot_choice)
            return

def setup(bot):
    bot.add_cog(Shootout(bot))


