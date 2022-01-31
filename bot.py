"""
@author Anthony Eid
@author Zeid Ramzi

Code for the discord bot goes here
"""
from time import sleep
import discord
import os

import bot_lib.db as db
from bot_lib.TOKEN import TOKEN
from discord.ext import commands

# 937592567288201227


def main():
    #Bot already has default intents, but this variable is made to allow for modification of the indents
    #and enabling Intents.members which is a privileged intent
    intents = discord.Intents.default()
    intents.members = True

    bot = commands.Bot(command_prefix='$', intents=intents, case_insensitive=True)
    db.OpenUserDatabase()


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
    async def on_member_join(member : discord.member):
        guild: discord.Guild = bot.get_guild(936839088215060530)
        role = guild.get_role(937592567288201227)
        channel = bot.get_channel(937587875078344724)
        await member.add_roles(role)
        sleep(.5)
        await channel.send(f"Welcome {member.display_name} What is your real name?")
        


    @bot.event
    async def on_member_remove(member : discord.member):
        channel : discord.channel = bot.get_channel(936839088215060533)
        await channel.send(f"Cya {member.display_name} we didn't love you anyway")

    @bot.event
    async def on_message(message: discord.message):
        member = message.author
        if not member.bot:
            messageList = message.content.split()
            firstName = messageList[0]
            lastName = messageList[1]
            discord_id = member.id
            db.AddUser(discord_id, firstName, lastName)



        


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