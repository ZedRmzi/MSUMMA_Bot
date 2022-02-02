import discord
from discord.ext import commands
from data.globalVariables import bot_command_prefix

class HelpCog( commands.Cog ):
    def __init__( self, bot ):
        self.bot = bot

    @commands.command()
    async def help( self, ctx : commands.Context, *args : str ):

        #base help command
        if not len(args):
            embed = discord.Embed(
                title="Help",
                description="Need some help? Here are a list of commands you can get help on!\n\
                just type \"{}help [option]\" to learn more about a specific command.".format(bot_command_prefix))

            for command in self.bot.commands:
                if command == help:
                    continue
                embed.add_field( name = command, value = command, inline = False )

        await ctx.send( embed=embed )


def setup( bot ):
    bot.add_cog( HelpCog( bot ) )