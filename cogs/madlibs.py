import discord 
from discord.ext import commands
import random


class Madlibs(commands.Cog, name = 'Levelling'):
    def __init__(self, bot):
        self.bot = bot 

    @commands.command()
    async def madlib(self, ctx, choice1, choice2, choice3):
        
        madlib = discord.Embed(title="Madlibs!", description=f"Roses are {choice1}, \n {choice2} are blue, \n I love {choice3}", color = ctx.author.color)
        madlib.set_thumbnail(url = ctx.author.avatar_url)
        await ctx.send(embed = madlib)

    @commands.command()
    async def madlib_story(self, ctx, choice1, choice2, choice3, choice4, choice5, choice6, choice7, choice8, choice9):
        name = choice1
        noun_thing = choice2
        verb_action = choice3
        action = choice4
        action1 = choice5
        color = choice6
        city_place = choice7
        school_name = choice8
        food = choice9
        

        em = discord.Embed(title="Madlib Story!", description=f"Hello my name is `{ctx.author.name}` and I have a secret to share with you! \n\n I am a normal child by day and a `{noun_thing}` by night. Only you and `{name}` know my secret! \n\n You may be wondering how this happened? Well, one night I was at `{verb_action}` at home, and then BOOM! The lights went out and `{name}` showed up. They said in a loud voice, because your favorite color is `{color}`, you have been chosen to be a `{noun_thing}`. \n\n My mission is to save the people of `{city_place}` by doing my favorite things {action} and `{action1}`. This may sound easy but it is no walk in the park. It requires hard work and `{noun_thing}` mode. My weakness is eating `{food}`. They are gross! Keep that away from me! \n\n I save the world every night! But when i wake up in the morning, I go back to my normal life at `{school_name}` school!", color = ctx.author.color)
        em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)

        await ctx.send(embed=em)

    @commands.command()
    async def madlib_random(self, ctx):
        
        number = range(1,100)
        emotions = ["Happy", "Sad", "Angry", "Frustrated", "disapointed"]
        family_member = ["Mother", "Father", "Step-Mother", "Step-Father", "Sister in law", "Brother", "Brother in law", "Cousin", "Son", "Daughter", "Grandma", "Grandpa", "Auntie", "Uncle"]
        verb1 = ["Stolen", "Hid something", "Taken something"]
        place = ["Galaxy", "Empire", "Farm", "Theme Park", "Waterpark", "Car Dealership", "Supermarket", "School Playground", "Football Stadium", "Golf Course", "Gym", "Post Office", "Shopping Mall", "Bakery", "Parking Lot", "Train Station", "Bus station", "United Kingdom", "America", "Australia", "Forest", "River"]
        noun = ["Coins", "Weapons", "Coffee Beans", "Pepsi-Cola", "Plastic Straws", "Burger Buns", "Sharpie Markers", "Uranium", "Element", "Advice", "Farm Animals", "Tintoberries", "Large Animal feces", "Thatch", "Wood", "Metal Ingots", "Dino Leashes", "Jelly Beans", "Chocolate fountains", "Keyboards", "Live Mice", "A Cobra"]
        verb2 = ["Free", "Liberate", "Kill", "Rescue", "inform", "Hug", "Confront", "exile"]
        verb3 = ["Struggle", "Triumph", "Journey", "Tale", "Story", "Log", "Journal", "Battle"]

        em = discord.Embed(title=" Random Madlib Story!", description=f"The `{random.choice(verb3)}` of Olympians \n\n Zeus was very `{random.choice(emotions)}` with his `{random.choice(family_member)}` and sisters because they had `{random.choice(verb1)}` from him.\n\n Both Zeus and Kronos wanted to rule over the `{random.choice(place)}`, but only `{random.choice(number)}` of them could! So there was a fight! Zeus had his siblings on his side whilst Kronos had his - the Titans! Both sides were equally matched in the battle, until Zeus went to the `{random.choice(place)}` and got some `{random.choice(noun)}` off the Cyclops. \n\n Then he and his `{random.choice(family_member)}`  and sisters were able to `{random.choice(verb2)}` their father and rule over the world in `{random.choice(emotions)}`!", color = ctx.author.color)
        em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)

        await ctx.send(embed=em)

    @commands.command()
    async def madcom(self, ctx):
        em = discord.Embed(title = "How to play madlibs!", description = "Use !madlib colour plaural_noun celebrity", color = ctx.author.color)
        await ctx.send(embed=em)

    @commands.command()
    async def storycom(self, ctx):
        em = discord.Embed(title = "How to play madlibs story!", description = "Use !madlib_story `Name` `Noun` `Verb/Action`  `Action` `action` `color` `city/place` `School Name` `food`", color = ctx.author.color)
        await ctx.send(embed=em)

def setup(bot):
    bot.add_cog(Madlibs(bot))
    print("Madblibs is ready!")