import discord
import os
from os import environ as fetchsecret
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
  await ctx.send(arg)

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def ping(ctx):
    embed = discord.Embed(title='Pong!',description="Client latency is " + str(round(client.latency * 1000)) + "ms", color=0xf0455a)
    embed.set_footer(text='by '+str(ctx.author))
    await ctx.send(embed=embed)
        
@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    await ctx.send('this command under cooldown')
  
bot.run(token)
