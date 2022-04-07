import discord
from discord.ext import commands

class Roles(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        ourMessageID = 953602299379449927

        if ourMessageID == payload.message_id:
            member = payload.member
            guild = member.guild

            emoji = payload.emoji.name
        
        if emoji == '❤️':
            mrole = discord.utils.get(guild.roles, name='Loyalist')
            await member.add_roles(mrole)
            print (f'{member.name} Was assigned the Loyalist role!')
        
        if emoji == '🎮':
            mrole = discord.utils.get(guild.roles, name='PlayStation')
            await member.add_roles(mrole)
            print (f'{member.name} Was assigned the PlayStation role!')
        if emoji == '☢️':
            mrole = discord.utils.get(guild.roles, name='NSFW Crew')
            await member.add_roles(mrole)
            print (f'{member.name} Was assigned the NSFW Crew role!')
        if emoji == '🔕':
            mrole = discord.utils.get(guild.roles, name='Anti-Social')
            await member.add_roles(mrole)
            print (f'{member.name} Was assigned the Anti-Social role!')


def setup(bot):
    bot.add_cog(Roles(bot))