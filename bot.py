"""
@author Anthony Eid

Code for the discord bot goes here
"""

import discord

TOKEN = 'OTM2ODU2MDY1NDE5NjQ5MDQ1.YfTRMw.g-qFQIEC_TK4yD8IkmdnwHQuI1s'

import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()
client.run(TOKEN)