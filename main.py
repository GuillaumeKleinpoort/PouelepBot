import discord
import os
import time

from keep_alive import keep_alive


client = discord.Client()

@client.event
async def on_ready():
    print('Pouelep ? {}'.format(client))
    

@client.event
async def on_message(message):
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