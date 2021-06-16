import json
import discord
from discord.ext import commands
import random
import asyncio
import time


async def wrong(message):
    # fill in
    await message.author.send(embed=discord.Embed(title=f"<a:reject:811218936452349986> | You cannot use that command in {message.channel}.", color=discord.Color.red(), description="<a:tick:811218936875319316> | You can use that command in: <#>."))
