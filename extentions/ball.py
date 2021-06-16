import json
import discord
from discord.ext import commands
import random
import asyncio
import time
import requests


async def ball(message, channelSend, client, level):
    time_OUT = 0
    localtime = time.asctime(time.localtime(time.time()))
    await channelSend.send(f'**[{localtime}]** 🎮 **{message.author.display_name}** Has **played the game ball**: \n > `Channel: {message.channel}`\n > `Success:` <a:tick:811218936875319316>')
    msgEmbed = discord.Embed(title="The Game is loading...", color=discord.Color.blue(),
                             description="Once the game loads, the bot will react with :white_medium_small_square:, reacting with it allows you to hit the ball into the goal.")
    msgEmbed.set_footer(text="Discord Version - Lag is expected")
    msg = await message.channel.send(embed=msgEmbed)
    await asyncio.sleep(10)
    await msg.add_reaction('◻')
    while True:
        time_OUT += 1
        if time_OUT == 20:
            await msg.clear_reactions()
            await msg.add_reaction("🔴")
            await msg.edit(embed=discord.Embed(title="Error", color=discord.Color.red(), description=f'User <@{message.author.id}> has timed out!'))
            break
        content = ':goal: :goal: :goal:'
        ball = random.randrange(1, 4)
        head = random.randrange(1, 4)
        if head == 1:
            content = content + '\n :person_bald: '
        elif head == 2:
            content = content + '\n <:Capture:803747883236589600> :person_bald: '
        elif head == 3:
            content = content + \
                '\n <:Capture:803747883236589600> <:Capture:803747883236589600> :person_bald: '
        if ball == 1:
            content = content + '\n :soccer:'
        elif ball == 2:
            content = content + '\n <:Capture:803747883236589600> :soccer:'
        elif ball == 3:
            content = content + '\n <:Capture:803747883236589600> <:Capture:803747883236589600> :soccer:'
        e = discord.Embed(
            title="", color=discord.Color.blurple(), description=content)
        await msg.edit(embed=e)

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '◻'

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=1.0, check=check)
        except asyncio.TimeoutError:
            pass
        else:
            await msg.clear_reactions()
            if ball == head:
                await msg.add_reaction('😢')
                lw = discord.Embed(title="Oh No!", color=discord.Color.red(),
                                   description='You have lost.')
                ball = requests.put(f"http://127.0.0.1:5000/ballL/{message.author.id}",
                                    {"Type": "ballL", "Add": 1})
                levels = requests.put(f"http://127.0.0.1:5000/level/{message.author.id}",
                                      {"Type": "level", "Add": 50})
                levels = levels.json()
                ball = ball.json()

            else:
                await msg.add_reaction('🎉')
                lw = discord.Embed(title=" Congrats!", color=discord.Color.green(),
                                   description="You have won.")
                levels = requests.put(f"http://127.0.0.1:5000/level/{message.author.id}",
                                      {"Type": "level", "Add": 100})
                ball = requests.put(f"http://127.0.0.1:5000/ballW/{message.author.id}",
                                    {"Type": "ballW", "Add": 1})
                levels = levels.json()
                ball = ball.json()
            ball_L = ball['ballL']
            ball_W = ball['ballW']
            levelShow = level.api(levels['exp'])
            lw.add_field(name="**Level**",
                         value=f"`{levelShow}`", inline=False)
            lw.add_field(
                name="**Wins**", value=f"`{ball_W}`", inline=False)
            lw.add_field(
                name="**Loses**", value=f"`{ball_L}`", inline=False)

            role = discord.utils.find(
                lambda r: r.name == 'Premium', message.guild.roles)
            if role in message.author.roles:
                lw.add_field(
                    name="**To play again click the:**", value=f'`🔹`', inline=True)
                await msg.edit(embed=lw)
                await msg.add_reaction("🔹")

                def check2(reaction, user):
                    return user == message.author and str(reaction.emoji) == '🔹'

                try:
                    reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check2)
                except asyncio.TimeoutError:
                    await msg.clear_reactions()
                    break
                else:
                    await msg.clear_reactions()
                    time_OUT = 0
                    localtime = time.asctime(time.localtime(time.time()))
                    await channelSend.send(f'**[{localtime}]** 🎮 **{message.author.display_name}** Has **played the game ball**: \n > `Channel: {message.channel}`\n > `Success:` <a:tick:811218936875319316>')
                    msgEmbed = discord.Embed(title="The Game is loading...", color=discord.Color.blue(),
                                             description="Once the game loads, the bot will react with :white_medium_small_square:, reacting with it allows you to hit the ball into the goal.")
                    msgEmbed.set_footer(
                        text="Discord Version - Lag is expected")
                    await msg.edit(embed=msgEmbed)
                    await asyncio.sleep(5)
                    await msg.add_reaction('◻')
            else:
                await msg.edit(embed=lw)
                break


async def wrong(message, channelSend):
    localtime = time.asctime(time.localtime(time.time()))
    await channelSend.send(f'**[{localtime}]** 🎮 **{message.author.display_name}** Has **played the game ball**: \n > `Channel: {message.channel}`\n > `Success:` <a:reject:811218936452349986>')
