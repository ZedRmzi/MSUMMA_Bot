"""
@author Anthony Eid
@author Zeid Ramzi

Code for the discord bot goes here
"""
import discord
import os
from TOKEN import TOKEN
from discord.ext import commands


def main():
    #Bot already has default intents, but this variable is made to allow for modification of the indents
    #and enabling Intents.members which is a privileged intent
    intents = discord.Intents.default()
    intents.members = True

    bot = commands.Bot(command_prefix='$', intents=intents, case_insensitive=True)

    #remove built-in help command
    bot.remove_command("help")

    @bot.event
    async def on_ready():

        cogs = os.listdir("cogs")
        for cog in cogs:
            if cog.endswith('.py'):

                bot.load_extension("cogs." + cog[:-3])


        print("Ready")


    @bot.event
    async def on_member_join(member):
        print('someone joined')


    @bot.event
    async def on_member_remove(member):
        pass


    @bot.command()
    async def hello(ctx):
        username = ctx.message.author
        await ctx.send("Hello {}!".format(username))


    #help command
    @bot.command(aliases=["h"])
    async def help(ctx, *args):
        pass

    bot.run(TOKEN)

if __name__ == '__main__':
    main()