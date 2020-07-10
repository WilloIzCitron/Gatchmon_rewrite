import discord
import os
from os import environ as fetchsecret
import dotenv
from discord.ext import commands
from datetime import datetime
timestamp = datetime.now()

token = fetchsecret['TOKEN']
bot = commands.Bot(command_prefix='g!')
client = discord.Client()

async def is_owner(ctx):
    return ctx.author.id == 479642404216111124

@bot.event
async def on_ready():
  myAct = discord.Activity(name='Digimon Universe App Monster | '+str(datetime.now())[:-15]+' | g!', type=discord.ActivityType.watching)
  await bot.change_presence(status=discord.Status.idle, activity=myAct,)
  print('bot online')
 
@bot.command()
@commands.cooldown(1, 12, commands.BucketType.user)
async def say(ctx, arg):
  await ctx.message.delete
  await ctx.send(arg)

@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    await ctx.send('this command under cooldown')
  
bot.run(token)
