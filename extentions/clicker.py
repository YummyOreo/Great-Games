import json
import discord
from discord.ext import commands
import random
import asyncio
import time
import requests


async def clicker(message, channelSend, client, level):
    mytime = time.asctime(time.localtime(time.time()))
    await channelSend.send(f'**[{mytime}]** 🎮 **{message.author.display_name}** Has **played the game clicker**: \n > `Channel: {message.channel}`\n > `Success:` <a:tick:811218936875319316>')
    msgEmbed = discord.Embed(title="The Game is loading...", color=discord.Color.blue(
    ), description="Once the game loads, the bot will react with :frog: :hatched_chick: :heart: and :blue_circle:. In a random amount of time, one of the emojis will pop up. React with the emoji shown as fast as you can. Then you'll get your score.")
    msgEmbed.set_footer(text="Discord Version - Lag is expected")
    msg = await message.channel.send(embed=msgEmbed)
    emojie_list = ["🐸", "🐥", "❤", '🔵']
    time_OUT = 0
    time_Score = 0
    popup = random.randrange(1, 31)
    await asyncio.sleep(popup)
    popup_emoji = random.choice(emojie_list)
    for emoji in emojie_list:
        await msg.add_reaction(emoji)
    msgEmbed = discord.Embed(
        title="", color=discord.Color.blurple(), description=popup_emoji)
    await msg.edit(embed=msgEmbed)
    while True:
        time_OUT += 1
        if time_OUT == 200:
            await msg.clear_reactions()
            await msg.add_reaction("🔴")
            await msg.edit(embed=discord.Embed(title="Error", color=discord.Color.red(
            ), description=f'User <@{message.author.id}> has timed out!'))
            break

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == popup_emoji

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=.1, check=check)
        except asyncio.TimeoutError:
            time_Score += 0.10
            pass
        else:
            await msg.clear_reactions()
            await msg.add_reaction("🎉")
            print(1)
            levels = requests.put(f"http://127.0.0.1:5000/level/{message.author.id}",
                                  {"Type": "level", "Add": 100})
            levels = levels.json()
            print(levels)
            score = time_Score * 100
            if levels['highScore'] > score and levels['highScore'] != 0:
                highScore = requests.put(f"http://127.0.0.1:5000/highScore/{message.author.id}",
                                         {"Type": "level", "Add": int(score)})
            elif levels['highScore'] == 0:
                highScore = requests.put(f"http://127.0.0.1:5000/highScore/{message.author.id}",
                                         {"Type": "level", "Add": int(score)})
            else:
                highScore = requests.get(f"http://127.0.0.1:5000/highScore/{message.author.id}",
                                         {"Type": "level"})

            highScore = highScore.json()
            print(highScore)
            hShow = highScore['highScore']
            levelShow = level.api(levels['exp'])
            print(6)
            msgEmbed = discord.Embed(
                title="Here are you statistics:", color=discord.Color.green())
            msgEmbed.add_field(
                name="**Score**", value=f'`{score:.0f}`', inline=True)
            msgEmbed.add_field(
                name="**Level**", value=f"`{levelShow}`", inline=True)
            msgEmbed.add_field(
                name="**Bets Score** \n (Low score better)", value=f'`{hShow:.0f}`', inline=True)
            msgEmbed.add_field(
                name="**Emoji**", value=f'`{popup_emoji}`', inline=True)
            msgEmbed.set_footer(text=f'Your time was \n {time_Score:.2f}')
            print(7)

            role = discord.utils.find(
                lambda r: r.name == 'Premium', message.guild.roles)
            if role in message.author.roles:
                msgEmbed.add_field(
                    name="**To play again click the:**", value=f'`▶`', inline=True)
                await msg.edit(embed=msgEmbed)
                await msg.add_reaction("▶")

                def check2(reaction, user):
                    return user == message.author and str(reaction.emoji) == '▶'

                try:
                    reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check2)
                except asyncio.TimeoutError:
                    await msg.clear_reactions()
                    break
                else:
                    await msg.clear_reactions()
                    mytime = time.asctime(time.localtime(time.time()))
                    await channelSend.send(f'**[{mytime}]** 🎮 **{message.author.display_name}** Has **played the game clicker**: \n > `Channel: {message.channel}`\n > `Success:` <a:tick:811218936875319316>')
                    msgEmbed = discord.Embed(title="The Game is loading...", color=discord.Color.blue(
                    ), description="Once the game loads, the bot will react with :frog: :hatched_chick: :heart: and :blue_circle:. In a random amount of time, one of the emojis will pop up. React with the emoji shown as fast as you can. Then you'll get your score.")
                    msgEmbed.set_footer(
                        text="Discord Version - Lag is expected")
                    await msg.edit(embed=msgEmbed)
                    emojie_list = ["🐸", "🐥", "❤", '🔵']
                    time_OUT = 0
                    time_Score = 0
                    popup = random.randrange(1, 31)
                    await asyncio.sleep(popup)
                    popup_emoji = random.choice(emojie_list)
                    for emoji in emojie_list:
                        await msg.add_reaction(emoji)
                    msgEmbed = discord.Embed(
                        title="", color=discord.Color.blurple(), description=popup_emoji)
                    await msg.edit(embed=msgEmbed)
            else:
                await msg.edit(embed=msgEmbed)
                break


async def wrong(message, channelSend):
    mytime = time.asctime(time.localtime(time.time()))
    await channelSend.send(f'**[{mytime}]** 🎮 **{message.author.display_name}** Has **played the game clicker**: \n > `Channel: {message.channel}`\n > `Success:` <a:reject:811218936452349986>')
