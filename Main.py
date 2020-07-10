import discord
import os
import dotenv
from discord.ext import commands
from datetime import datetime
timestamp = datetime.now()

token = os.getenv('TOKEN')
bot = commands.Bot(command_prefix='g!')
client = discord.Client()

@bot.event
async def on_ready():
  print('bot online')
  
@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    await ctx.send('this command under cooldown')
  
bot.run(token)