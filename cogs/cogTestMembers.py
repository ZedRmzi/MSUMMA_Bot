import discord
from discord.ext import commands

class MainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx : commands.Context):
        print("cog worked!")

def setup(bot):
    bot.add_cog(MainCog(bot))