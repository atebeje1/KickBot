import discord
import random
import sys
import os

from discord.ext import commands

# initializes the bot as the client
client = commands.Bot(command_prefix = '$')

# Recognizes bot is online and prints version
@client.event
async def on_ready():
  versionNum = 0
  version_src = open('version.txt', 'r')
  for line in version_src:
    if line[:8]=='version=':
      versionNum = line[8:]
  version_src.close()
  print('{0.user} version {1} went online.'.format(client, versionNum))

# kicks user on command '$kick @user'
@client.command()
async def kick(ctx, member : discord.Member,*, reason = None):
  if reason == None:
    await ctx.send('{0} has been kicked.'.format(member))
  else:
    await ctx.send('{0} has been kicked {1}.'.format(member, reason))
  await member.kick(reason = reason)

# @client.command()
# async def add_roles()

client.run(os.getenv('TOKEN'))

