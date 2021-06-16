import discord
import json
import asyncio
from discord.ext import commands
import random
from os import system
import time

bot = commands.Bot(command_prefix='gg!')
bot.remove_command('help')


@bot.event
async def on_ready():
    localtime = time.asctime(time.localtime(time.time()))
    channelSend = bot.get_channel()  # fill in
    await channelSend.send(f"**[{localtime}]** The **Slowmode** file is __Online__ \n > <a:tick:811218936875319316>")
    while 1 == 1:
        channelSlow = bot.get_channel()  # fill in
        channelLogs = bot.get_channel()  # fill in
        ranWait = random.randint(21600, 86400)
        ranSlow = random.randint(1, 21600)
        await channelSlow.edit(slowmode_delay=ranSlow)
        await channelLogs.send(f"> Slowmode changed to: **{ranSlow} seconds** and will be changed again in **{ranWait} seconds**. Have fun!")
        await channelSlow.send(f"> Slowmode changed to: **{ranSlow} seconds** and will be changed again in **{ranWait} seconds**. Have fun!")
        await asyncio.sleep(ranWait)

try:
    bot.run('')  # fill in
except:
    print("error")
