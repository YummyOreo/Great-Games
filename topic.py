import os
import discord
import json
import asyncio
from discord.ext import commands
import random
from os import system

# set client
client = commands.Bot(command_prefix='gg!')
client.remove_command('help')

global list
try:
    list = json.load(open('topicList.josn'))
except:
    list = ["Whats your favorite video game?", "Do you like books?"]


allStaff = '• Chief of Staff'
# On start


@client.event
async def on_ready():
    channelSend = client.get_channel()  # fill in
    await channelSend.send(f'__Topic__ is **online** ✔')


@client.group()
async def topic(ctx):
    await ctx.message.delete()
    channelSend = client.get_channel()  # fill in
    global list
    if ctx.invoked_subcommand is None:
        await channelSend.send(f'**{ctx.author.display_name} has used a command** \n > **`Command` topic `[general]`** \n > **`Channel {ctx.message.channel}`** \n > 👍')
        e = discord.Embed(title=f"**The new topic is..**",
                          color=discord.Color.blurple())
        e.add_field(name=f"**{random.choice(list)}**",
                    value=f"Have a good time talking", inline=False)
        await ctx.channel.send(embed=e)


@topic.command()
@commands.has_any_role(allStaff)
async def add(ctx, *, x=""):
    if x == '':
        return
    else:
        channelSend = client.get_channel()  # fill in
        list.append(x)
        print(list)
        j = json.dumps(list)
        with open('topicList.josn', 'w') as f:
            f.write(j)
            f.close()
        await channelSend.send(f'**{ctx.author.display_name} has used a command** \n > **`Command` topic `[general]`** \n > **`Channel {ctx.message.channel}`** \n > `Changed to {x}` \n > **`List:`** `{list}` \n > 👍')
try:
    client.run('')  # fill in
except:
    print("error")
