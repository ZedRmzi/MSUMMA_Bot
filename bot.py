"""
@author Anthony Eid

Code for the discord bot goes here
"""
from TOKEN import TOKEN
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print("Ready")


bot.run(TOKEN)