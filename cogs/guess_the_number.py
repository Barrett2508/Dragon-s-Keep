import discord 
from discord.ext import commands
import random

class Numberguess(commands.Cog, name = 'guess_the_number'):
    def __init__(self, bot):
        self.bot = bot 
    


    @commands.command(aliases = ["ng"])
    async def numberguess(self, ctx, choice1):
        number = random.choice(range(1,11))
        guess = choice1

        while int(guess) == number:
            await ctx.send("Well done, you guessed correctly :tada:")
            return

        else:
            if int(guess) != number:
                await ctx.send(f"Better luck next time! 😭 \n\n The number was {number}")
                return

    @commands.command()
    async def pc(self, ctx, x):
        password = "Alph4r3X"
        x = str(x)

        if x in password:
            await ctx.send(f"{x} is in the password!")
        if x == password:
            await ctx.send(f"{ctx.author.name} guessed the password and won a max level dino!")
        if x not in password:
            await ctx.send(f"{x} is not in the password!")


def setup(bot): 
    bot.add_cog(Numberguess(bot))

        


