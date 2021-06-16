import json
import discord
from discord.ext import commands
import random
import asyncio
import time
import level
import requests

global word_List
word_List = ["Dont copy!", "Hello, why are you here?", "Are you here?", "Where are you?", "Bob went to the pool.", "Youtube is fun!", "Playing with Great Games is fun!", "Invite me in dms.", "Are you bobs friend?", "I cant spell.", "lol", "Why are you copying and pasting?", "Ai coming soon!!!", "I like to code",
             "Do you like to code?", "I cant come up with all of these :(", "Can you come up with 25 things?", "Why do I have to do this?", "Im having fun!", "Am i haveing fun?", "Are you human?", "What age are you?", "Lag is here", "Almost there!", "Great Times is the best", "All bot are good *wink*"]

levelsCount = [100, 300, 600, 1000, 1500, 2100, 2850, 3850, 4000, 5900, 7500, 8050, 10000,
               15000, 30000, 55000, 70000, 95000, 100000, 110000, 122000, 145000, 159000, 200000, 250000]


async def first(ctx, client):
    word_List = ["Dont copy!", "Hello, why are you here?", "Are you here?", "Where are you?", "Bob went to the pool.", "Youtube is fun!", "Playing with Great Games is fun!", "Invite me in dms.", "Are you bobs friend?", "I cant spell.", "lol", "Why are you copying and pasting?", "Ai coming soon!!!", "I like to code",
                 "Do you like to code?", "I cant come up with all of these :(", "Can you come up with 25 things?", "Why do I have to do this?", "Im having fun!", "Am i haveing fun?", "Are you human?", "What age are you?", "Lag is here", "Almost there!", "Great Times is the best", "All bot are good *wink*"]
    localtime = time.asctime(time.localtime(time.time()))
    channelSend = client.get_channel()  # fill in
    await channelSend.send(f'**[{localtime}]** 💬 **{ctx.author.display_name}** Has **played the game type**: \n > `Channel: {ctx.channel}`\n > `Success:` <a:tick:811218936875319316>')
    ran = random.randrange(0, 25)
    msgEmbed = discord.Embed(title="The Game is loading...", color=discord.Color.blue(),
                             description="Once the game loads, it will show you a message! To retype it do `/premium game: type retype`! The first person to type it into the chat wins!")
    msgEmbed.set_footer(text="Beta Version - Lag is expected")
    msg = await ctx.send(embed=msgEmbed)
    await asyncio.sleep(10)
    msgEmbed = discord.Embed(title="Your message is:", color=discord.Color.blurple(),
                             description=f"`‎{word_List[ran]}‎`")
    msgEmbed.set_footer(text="These words are randomly genorated!")
    await msg.edit(embed=msgEmbed)
    return word_List[ran]


async def second(ctx, client):
    msgEmbed = discord.Embed(title="Done!", color=discord.Color.green(),
                             description=f"**`The person was:`** \n <@{ctx.author.id}>")
    msgEmbed.set_footer(text="Beta Version - Lag is expected")
    await ctx.send(embed=msgEmbed)
    levels = requests.put(f"http://127.0.0.1:5000/level/{ctx.author.id}",
                          {"Type": "level", "Add": 200})
    requests.put(f"http://127.0.0.1:5000/type/{ctx.author.id}",
                 {"Type": "level", "Add": 1})
