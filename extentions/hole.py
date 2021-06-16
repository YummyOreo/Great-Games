import json
import discord
from discord.ext import commands
import random
import asyncio
import time
import requests


async def hole(message, channelSend, bot, level):
    time_out = 0
    localtime = time.asctime(time.localtime(time.time()))
    await channelSend.send(f'**[{localtime}]** 🎮 **{message.author.display_name}** Has **played the game hole**: \n > `Channel: {message.channel}`\n > `Success:` <a:tick:811218936875319316>')
    msgEmbed = discord.Embed(title="The Game is loading...", color=discord.Color.blue(),
                             description="Once the game loads, youll a hole and a ball, youll need to press :baseball: to trow the ball into the hole when it lines up!")
    msgEmbed.set_footer(text="Discord Version - Lag is expected")
    msg = await message.channel.send(embed=msgEmbed)
    await asyncio.sleep(10)
    await msg.add_reaction("⚾")
    while True:
        time_out += 1
        if time_out == 50:
            await msg.clear_reactions()
            await msg.add_reaction("🔴")
            await msg.edit(embed=discord.Embed(title="Error", color=discord.Color.red(), description=f'User <@{message.author.id}> has timed out!'))
            break
        ranBall = random.randint(1, 3)
        ranHole = random.randint(1, 3)
        if ranHole == 1:
            content = '⬛ :green_square: :green_square: \n'
        elif ranHole == 2:
            content = ':green_square: ⬛ :green_square: \n'
        elif ranHole == 3:
            content = ':green_square: :green_square: ⬛ \n'
        if ranBall == 1:
            content = content + '⚾ <:Capture:803747883236589600> <:Capture:803747883236589600>'
        elif ranBall == 2:
            content = content + '<:Capture:803747883236589600> ⚾ <:Capture:803747883236589600>'
        elif ranBall == 3:
            content = content + '<:Capture:803747883236589600> <:Capture:803747883236589600> ⚾'
        embed_MSG = discord.Embed(
            title="", color=discord.Color.blurple(), description=content)
        await msg.edit(embed=embed_MSG)

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == "⚾"

        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=1, check=check)
        except asyncio.TimeoutError:
            pass
        else:
            await msg.clear_reactions()

            if ranBall == ranHole:
                levels = requests.put(f"http://127.0.0.1:5000/level/{message.author.id}",
                                      {"Type": "level", "Add": 100})
                lw = discord.Embed(
                    title="You Have Won!", color=discord.Color.green())
                await msg.add_reaction('🎉')
            else:
                levels = requests.put(f"http://127.0.0.1:5000/level/{message.author.id}",
                                      {"Type": "level", "Add": 50})
                lw = discord.Embed(
                    title="You lose.", color=discord.Color.red())
                await msg.add_reaction('😢')
            levels = levels.json()
            levelShow = level.api(levels['exp'])
            lw.add_field(name='`Level`', value=f"`{levelShow}`")
            role = discord.utils.find(
                lambda r: r.name == 'Premium', message.guild.roles)
            if role in message.author.roles:
                lw.add_field(
                    name="**To play again click the:**", value=f'`🟩`', inline=True)
                await msg.edit(embed=lw)
                await msg.add_reaction("🟩")

                def check2(reaction, user):
                    return user == message.author and str(reaction.emoji) == '🟩'

                try:
                    reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check2)
                except asyncio.TimeoutError:
                    await msg.clear_reactions()
                    break
                else:
                    await msg.clear_reactions()
                    time_out = 0
                    localtime = time.asctime(time.localtime(time.time()))
                    await channelSend.send(f'**[{localtime}]** 🎮 **{message.author.display_name}** Has **played the game hole**: \n > `Channel: {message.channel}`\n > `Success:` <a:tick:811218936875319316>')
                    msgEmbed = discord.Embed(title="The Game is loading...", color=discord.Color.blue(),
                                             description="Once the game loads, youll a hole and a ball, youll need to press :baseball: to trow the ball into the hole when it lines up!")
                    msgEmbed.set_footer(
                        text="Discord Version - Lag is expected")
                    await msg.edit(embed=msgEmbed)
                    await asyncio.sleep(5)
                    await msg.add_reaction("⚾")
            else:
                await msg.edit(embed=lw)
                break


async def wrong(message, channelSend):
    localtime = time.asctime(time.localtime(time.time()))
    await channelSend.send(f'**[{localtime}]** 🎮 **{message.author.display_name}** Has **played the game hole**: \n > `Channel: {message.channel}`\n > `Success:` <a:reject:811218936452349986>')
