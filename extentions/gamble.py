import json
import discord
from discord.ext import commands
import random
import asyncio
import time
import requests


async def gamble(message, channelSend, level):
    localtime = time.asctime(time.localtime(time.time()))
    await channelSend.send(f'**[{localtime}]** :game_die: **{message.author.display_name}** Has **played the game gamble**: \n > `Channel: {message.channel}`\n > `Success:` <a:tick:811218936875319316>')
    msgEmbed = discord.Embed(title="The Game is loading...", color=discord.Color.blue(),
                             description="When the game loads, youll see if you win the gamble or lose!")
    msgEmbed.set_footer(text="Discord Version - Lag is expected")
    msg = await message.channel.send(embed=msgEmbed)
    await asyncio.sleep(10)
    userRoll = random.randrange(1, 6)
    botRoll = random.randrange(1, 6)
    if botRoll > userRoll:
        msgEmbed = discord.Embed(
            title="You lost.", color=discord.Color.red())
        await msg.add_reaction('😢')
        levels = requests.put(f"http://127.0.0.1:5000/level/{message.author.id}",
                              {"Type": "level", "Add": 50})
    elif botRoll == userRoll:
        msgEmbed = discord.Embed(
            title="Tie!", color=discord.Color.blurple())
        await msg.add_reaction("😑")
        levels = requests.put(f"http://127.0.0.1:5000/level/{message.author.id}",
                              {"Type": "level", "Add": 70})
    else:
        msgEmbed = discord.Embed(
            title="You won!", color=discord.Color.green())
        await msg.add_reaction('🎉')
        levels = requests.put(f"http://127.0.0.1:5000/level/{message.author.id}",
                              {"Type": "level", "Add": 100})
    msgEmbed.add_field(
        name=f"**{message.author.display_name}'s roll**", value=f'`{userRoll}`', inline=True)
    msgEmbed.add_field(name=f"**Great Game's roll**",
                       value=f'`{botRoll}`', inline=True)
    await msg.edit(embed=msgEmbed)


async def wrong(message, channelSend):
    localtime = time.asctime(time.localtime(time.time()))
    await channelSend.send(f'**[{localtime}]** :game_die: **{message.author.display_name}** Has **played the game gamble**: \n > `Channel: {message.channel}`\n > `Success:` <a:reject:811218936452349986>')
