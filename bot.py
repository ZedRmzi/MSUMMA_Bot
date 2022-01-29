"""
@author Anthony Eid

Code for the discord bot goes here
"""
from TOKEN import TOKEN
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print("Ready")

@bot.event
async def on_member_join(member):
    print('someone joined')

@bot.event
async def on_member_remove(member):
    pass

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")


bot.run(TOKEN)