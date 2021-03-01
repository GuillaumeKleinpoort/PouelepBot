import discord
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
    print('Pouelep ? {}'.format(client))
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if str.lowercase(message.content) == 'pouelep':
      await message.channel.send('POUELEP')