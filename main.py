import discord
import os
from os import environ as fetchsecret
import Core as system
from discord.ext import commands
from datetime import datetime
timestamp = datetime.now()

token = fetchsecret['TOKEN']
bot = commands.Bot(command_prefix='m!')
client = discord.Client()
bot.remove_command('help')

async def is_owner(ctx):
    return ctx.author.id == 479642404216111124

@bot.event
async def on_ready():
  myAct = discord.Activity(name='Digimon Universe App Monster | '+str(datetime.now())[:-15]+' | g!', type=discord.ActivityType.watching)
  await bot.change_presence(status=discord.Status.idle, activity=myAct,)
  print('bot online')
 
@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def say(ctx, arg):
  await ctx.send(arg)

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def ping(ctx):
    embed = discord.Embed(title='Pong!', description="Client latency is "+str(round(client.latency * 1000))+"ms", color=0xf0455a)
    embed.set_footer(text='by '+str(ctx.author))
    await ctx.send(embed=embed)
  
@bot.command()
@commands.cooldown(1, 12, commands.BucketType.user)
async def serverinfo(ctx):
    server = ctx.guild
    roles = len(server.roles)
    channel_count = len([x for x in server.channels if type(x) == discord.channel.TextChannel])
    embed = discord.Embed(title='Guild info of '+server.name, color=server.owner.color)
    embed.set_thumbnail(url=server.icon_url)
    embed.set_image(url=server.banner_url)
    embed.add_field(name='General info', value='Owner= '+str(server.owner)+'\nMembers= '+str(server.member_count)+'\nChannels= '+str(channel_count)+'\nServerID= '+str(server.id)+'\nRegion= '+str(server.region)+'\nCreated at= '+server.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S')+'\nRole count= '+str(roles)+'\nBoost tier= '+str(server.premium_tier)+'\nMember has boost= '+str(server.premium_subscription_count)+' Boosts', inline=True)
    embed.add_field(name='Moderation', value='Verificaton levels= '+str(server.verification_level)+'\n 2FA level= '+str(server.mfa_level)+'\nExplicit content filter= '+str(server.explicit_content_filter), inline=True)
    embed.add_field(name="AFK", value='AFK Channel= '+str(server.afk_channel)+'\nAFK timeout= '+str(server.afk_timeout), inline=True)
    embed.add_field(name='Limits', value='Emoji limit= '+str(server.emoji_limit)+'\nBitrate limit='+str(server.bitrate_limit)+'Bps''\nFilesize limit= '+str(server.filesize_limit)+'B', inline=True)
    await ctx.send(embed=embed)

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def about(ctx):
    embed = discord.Embed(title="<a:dj_blob:723714370462416966> Gatchmon Biodata <a:dj_blob:723714370462416966>", description=(random.choice(['this is fun fact?', 'also try username601', 'what is this?', 'also try Nezumi Yui', 'you know? who is Vladimir Putin', 'press Alt+F4', 'you know? who is Ash Kentchum', 'You eat Nugget everyday?', 'You like Digimon?', 'The first climber a Mount Everest is Edmund Hillary', 'Globemon', 'also try Doppio', 'Willo has more friends', 'Wow Yankee with no Brim', 'Rick Astley - Never Gonna Give You Up', 'No anime', 'We need to build a wall', 'Do you know Da Wae', "<a:dj_blob:723714370462416966> Gatchmon Biodata <a:dj_blob:723714370462416966> <a:dj_blob:723714370462416966> Gatchmon Biodata <a:dj_blob:723714370462416966> <a:dj_blob:723714370462416966> Gatchmon Biodata <a:dj_blob:723714370462416966>", 'Everybody Gangsta First time Todoroki Shouto ツ#6379 got token leak', "this bot has 100% no NSFW"])), colour=0xf0455a)
    embed.add_field(name='Bot Biodata', value='Library= discord.py\nBot Created:June 12 2020\nCreated by: ||<@479642404216111124> or someball45#2588||\nDefault Prefix: g!\nCommands: 42 cmds')
    embed.add_field(name='Programer biodata', value='Favorite game=Terraria,Minecraft,From The Depths, Pc Buidling Simulator\nFavorite Language:Python,HTML,Javascript\nName:Willoizcitron\nSocial Media:\n[Github](https://github.com/WilloIzCitron)\n[Repl.It](https://repl.it/@SomeBall45)\n[BFD](https://botsfordiscord.com/user/479642404216111124)')
    embed.add_field(name='Versions', value='Discord.py = 1.3.3\nPython= 3.8.3\nBot Version = '+system.Version.version+'\nChangelog = '+system.Version.changelog+'')
    embed.add_field(name='Links', value='[Donate A Hacker Plan](https://repl.it/upgrade/SomeBall45)\n[Join Support Server](https://discord.gg/Y3YaFHF)')
    embed.add_field(name='APIs', value="Useless-api by VieroFernando, nekobot api by hibikidesu, shibe.online, randomfox.ca, random-d.uk")
    embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/721025249050624112/04c346e44a48763420f2b87f1a27789a.png?size=1024')
    embed.set_footer(text='Copyright (c) 2020 WilloIzCitron')
    await ctx.send(embed=embed)
    
@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def search(ctx,arg):
    keyword = system.urlify(arg)
    i = 1
    text = arg
    searches = [ "[YouTube](https://m.youtube.com/results?search_query="+str(keyword), "[Google](https://www.google.com/search?q="+str(keyword), "[Fandom](https://www.fandom.com/?s="+str(keyword), "[Google Image](https://www.google.com/search?tbm=isch&q="+str(keyword), "[Github](https://github.com/search?q="+str(keyword), "[Twitter](https://twitter.com/search?q="+str(keyword), "[Wikihow](https://www.wikihow.com/wikiHowTo?search="+str(keyword)]
    total = ''
    for i in range(0, len(searches)): total += str(i+1) + '. **' + searches[i] + ')**\n'
    embed = discord.Embed(color=0xf0455a)
    embed.add_field(name="Searches for "+str(text), value=total)
    await ctx.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    await ctx.send('this command under cooldown')
  
bot.run(token)
