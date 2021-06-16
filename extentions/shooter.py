import json
import discord
from discord.ext import commands
import random
import asyncio
import time
import requests


async def shooter(message, channelSend, bot, level):
    time_OUT = 0
    localtime = time.asctime(time.localtime(time.time()))
    await channelSend.send(f'**[{localtime}]** 🎮 **{message.author.display_name}** Has **plaed the game shooter**: \n > `Channel: {message.channel}`\n > `Success:` <a:tick:811218936875319316>')
    msg_EMBED = discord.Embed(title="The Game is loading...", color=discord.Color.blue(),
                              description="Once the game loads, the bot will react with ⚪, reacting with it allows you to shoot the gun, your goal is to kill the :person_frowning:.")
    msg_EMBED.set_footer(text="Discord Version - Lag is expected")
    msg = await message.channel.send(embed=msg_EMBED)
    await asyncio.sleep(10)
    await msg.add_reaction('⚪')
    while True:
        time_OUT += 1
        if time_OUT == 20:
            await msg.clear_reactions()
            await msg.add_reaction("🔴")
            await msg.edit(embed=discord.Embed(title="Error", color=discord.Color.red(), description=f'User <@{message.author.id}> has timed out!'))
            break
        head = random.randint(1, 3)
        gun = random.randint(1, 3)
        if head == 1:
            content = '\n :person_frowning: <:Capture:803747883236589600> <:Capture:803747883236589600>'
        elif head == 2:
            content = '\n <:Capture:803747883236589600> :person_frowning: <:Capture:803747883236589600>'
        elif head == 3:
            content = '\n <:Capture:803747883236589600> <:Capture:803747883236589600> :person_frowning: '
        if gun == 1:
            content = content + \
                '\n <:gun:802085107212222504> <:Capture:803747883236589600> <:Capture:803747883236589600>'
        elif gun == 2:
            content = content + \
                '\n <:Capture:803747883236589600> <:gun:802085107212222504> <:Capture:803747883236589600>'
        elif gun == 3:
            content = content + \
                '\n <:Capture:803747883236589600> <:Capture:803747883236589600> <:gun:802085107212222504>  '
        e = discord.Embed(
            title="", color=discord.Color.blurple(), description=content)
        await msg.edit(embed=e)

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '⚪'
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=1.0, check=check)
        except asyncio.TimeoutError:
            pass
        else:
            await msg.clear_reactions()
            if head == gun:
                lw = discord.Embed(title=" Congrats!", color=discord.Color.green(),
                                   description="You have won.")
                await msg.add_reaction('🎉')
                levels = requests.put(f"http://127.0.0.1:5000/level/{message.author.id}",
                                      {"Type": "level", "Add": 100})
                shooter = requests.put(f"http://127.0.0.1:5000/shooterW/{message.author.id}",
                                       {"Type": "shooterW", "Add": 1})
            else:
                lw = discord.Embed(title="Oh No!", color=discord.Color.red(),
                                   description='You have lost.')
                await msg.add_reaction('😢')
                shooter = requests.put(f"http://127.0.0.1:5000/shooterL/{message.author.id}",
                                       {"Type": "shooterL", "Add": 1})
                levels = requests.put(f"http://127.0.0.1:5000/level/{message.author.id}",
                                      {"Type": "level", "Add": 50})
            shooter = shooter.json()
            levels = levels.json()
            levelShow = level.api(levels['exp'])
            shooterW = shooter["shooterW"]
            shooterL = shooter["shooterL"]
            lw.add_field(name="**Level**",
                         value=f"`{levelShow}`", inline=False)
            lw.add_field(
                name="**Wins**", value=f"`{shooterW}`", inline=False)
            lw.add_field(
                name="**Loses**", value=f"`{shooterL}`", inline=False)
            role = discord.utils.find(
                lambda r: r.name == 'Premium', message.guild.roles)
            if role in message.author.roles:
                lw.add_field(
                    name="**To play again click the:**", value=f'`⏯`', inline=True)
                await msg.edit(embed=lw)
                await msg.add_reaction("⏯")

                def check2(reaction, user):
                    return user == message.author and str(reaction.emoji) == '⏯'

                try:
                    reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check2)
                except asyncio.TimeoutError:
                    await msg.clear_reactions()
                    break
                else:
                    await msg.clear_reactions()
                    time_OUT = 0
                    localtime = time.asctime(time.localtime(time.time()))
                    await channelSend.send(f'**[{localtime}]** 🎮 **{message.author.display_name}** Has **plaed the game shooter**: \n > `Channel: {message.channel}`\n > `Success:` <a:tick:811218936875319316>')
                    msg_EMBED = discord.Embed(title="The Game is loading...", color=discord.Color.blue(),
                                              description="Once the game loads, the bot will react with ⚪, reacting with it allows you to shoot the gun, your goal is to kill the :person_frowning:.")
                    msg_EMBED.set_footer(
                        text="Discord Version - Lag is expected")
                    await msg.edit(embed=msg_EMBED)
                    await asyncio.sleep(5)
                    await msg.add_reaction('⚪')
            else:
                await msg.edit(embed=lw)
                break


async def wrong(message, channelSend):
    localtime = time.asctime(time.localtime(time.time()))
    await channelSend.send(f'**[{localtime}]** 🎮 **{message.author.display_name}** Has **played the game shooter**: \n > `Channel: {message.channel}`\n > `Success:` <a:reject:811218936452349986>')
