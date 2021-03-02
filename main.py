import discord
import os
import time

from keep_alive import keep_alive
from discord.ext import commands
from discord import ChannelType


client = commands.Bot(command_prefix="$")


@client.event
async def on_ready():
    print('Pouelep ? {}'.format(client))
    
@client.command(pass_context=True)
async def pouelep(ctx, *, channel_name):
  # channels = (c.name for c in ctx.server.channels if c.type==ChannelType.voice)
  for chann in ctx.guild.voice_channels:
    if str(chann) == channel_name:
      try:
        vc = await chann.connect()
        vc.play(discord.FFmpegPCMAudio("pouelep.mp3"))
        time.sleep(1.5)
        await vc.disconnect()
      except discord.errors.ClientException:
        pass
      
      return
  

@client.listen('on_message')
async def poueleping(message):
  try:
    if message.author == client.user:
        return
    if 'pouelep' in str.lower(message.content):
      await message.channel.send('POUELEP')

      try:
        voice_state = message.author.voice
        if voice_state is not None :
            channel = message.author.voice.channel
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio("pouelep.mp3"))
            time.sleep(1.5)
            await vc.disconnect()
      except discord.errors.ClientException:
        pass
  except Exception:
    pass

keep_alive()
client.run(os.getenv('TOKEN'))