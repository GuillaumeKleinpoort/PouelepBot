import discord
import os

from keep_alive import keep_alive


client = discord.Client()

@client.event
async def on_ready():
    print('Pouelep ? {}'.format(client))
    

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if str.lower(message.content) == 'pouelep':
      await message.channel.send('POUELEP')

keep_alive()
client.run("ODE2MDQ5OTkxNTg3NTk0MjQx.YD1Txw.hylWBAc1mlF40fa755ZNcnx1vUc")