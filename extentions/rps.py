import json
import discord
from discord.ext import commands
import random
import asyncio
import time
import requests


async def rps(message, channelSend, client, level):
    rpsCheck = 1
    localtime = time.asctime(time.localtime(time.time()))
    await channelSend.send(f'**[{localtime}]** 🎮 **{message.author.display_name}** Has **played the game rps**: \n > `Channel: {message.channel}`\n > `Success:` <a:tick:811218936875319316>')
    msgEmbed = discord.Embed(title="The Game is loading...", color=discord.Color.blue(),
                             description="Once the game loads, you chose, rock, paper, or scissors. Now see if you win!")
    msgEmbed.set_footer(text="Discord Version - Lag is expected")
    msg = await message.channel.send(embed=msgEmbed)
    await asyncio.sleep(10)
    while True:
        await msg.edit(embed=discord.Embed(title="Rock!", color=discord.Color.blurple(),
                                           description="Click 🪨 to chose rock."))
        await msg.add_reaction("🪨")

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == "🪨"

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=3, check=check)
        except asyncio.TimeoutError:
            await msg.clear_reactions()
            await msg.add_reaction("📄")
            rpsCheck = 2
            await msg.edit(embed=discord.Embed(title="Paper!", color=discord.Color.blurple(),
                                               description="Click 📄 to chose paper."))
        else:
            chose = 1

        if rpsCheck == 2:
            def check(reaction, user):
                return user == message.author and str(reaction.emoji) == "📄"

            try:
                reaction, user = await client.wait_for('reaction_add', timeout=3, check=check)
            except asyncio.TimeoutError:

                await msg.clear_reactions()
                await msg.add_reaction("✂")
                rpsCheck = 3
                await msg.edit(embed=discord.Embed(title="Scissors!", color=discord.Color.blurple(),
                                                   description="Click ✂ to chose scissors."))
            else:
                chose = 2
        else:
            pass
        if rpsCheck == 3:
            def check(reaction, user):
                return user == message.author and str(reaction.emoji) == "✂"

            try:
                reaction, user = await client.wait_for('reaction_add', timeout=3, check=check)
            except asyncio.TimeoutError:
                await msg.clear_reactions()
                await msg.add_reaction("🔴")
                await msg.edit(embed=discord.Embed(title="Error", color=discord.Color.red(), description=f'User <@{message.author.id}> has timed out!'))
                return
            else:
                chose = 2
        if chose != 0:
            print("oh no")
            levels = requests.put(f"http://127.0.0.1:5000/level/{message.author.id}",
                                  {"Type": "level", "Add": 200})
            levels = levels.json()
            rock = "📄"
            paper = "✂"
            scissors = ":rock:"
            WL = random.randint(1, 2)
            print(WL)
            if WL == 1:
                await msg.clear_reactions()
                await msg.add_reaction("🎉")
                if chose == 1:
                    e = discord.Embed(
                        title="You WON!", color=discord.Color.green())
                    e.add_field(name="**Your chose**",
                                value=f"{scissors}", inline=True)
                    e.add_field(name="**Bot's chose**",
                                value=f"{paper}", inline=True)
                    await msg.edit(embed=e)
                elif chose == 2:
                    # scissors
                    e = discord.Embed(
                        title="You WON!", color=discord.Color.green())
                    e.add_field(name="**Your chose**",
                                value=f"{rock}", inline=True)
                    e.add_field(name="**Bot's chose**",
                                value=f"{scissors}", inline=True)
                    await msg.edit(embed=e)
                else:
                    e = discord.Embed(
                        title="You WON!", color=discord.Color.green())
                    e.add_field(name="**Your chose**",
                                value=f"{paper}", inline=True)
                    e.add_field(name="**Bot's chose**",
                                value=f"{rock}", inline=True)
                    await msg.edit(embed=e)
                    # rock
                print(levels)
                print(levels['exp'])
                levelShow = level.api(levels['exp'])
                e.add_field(name="**Level**",
                            value=f"{levelShow}", inline=True)
                await msg.edit(embed=e)
            elif WL == 2 or WL == 3:
                levels = requests.put(f"http://127.0.0.1:5000/level/{message.author.id}",
                                      {"Type": "level", "Add": 100})
                levels = levels.json()
                await msg.clear_reactions()
                await msg.add_reaction("😭")
                if chose == 1:
                    # rock
                    e = discord.Embed(
                        title="You losed \:(", color=discord.Color.red())
                    e.add_field(name="**Your chose**",
                                value=f"{scissors}", inline=True)
                    e.add_field(name="**Bot's chose**",
                                value=f"{rock}", inline=True)

                elif chose == 2:
                    # paper
                    e = discord.Embed(
                        title="You losed \:(", color=discord.Color.red())
                    e.add_field(name="**Your chose**",
                                value=f"{rock}", inline=True)
                    e.add_field(name="**Bot's chose**",
                                value=f"{paper}", inline=True)

                else:
                    e = discord.Embed(
                        title="You losed \:(", color=discord.Color.red())
                    e.add_field(name="**Your chose**",
                                value=f"{paper}", inline=True)
                    e.add_field(name="**Bot's chose**",
                                value=f"{scissors}", inline=True)
                print(levels)
                print(levels['exp'])
                levelShow = level.api(levels['exp'])
                e.add_field(name="**Level**",
                            value=f"{levelShow}", inline=True)
            role = discord.utils.find(
                lambda r: r.name == 'Premium', message.guild.roles)
            if role in message.author.roles:
                e.add_field(
                    name="**To play again click the:**", value=f'`🟢`', inline=True)
                await msg.edit(embed=e)
                await msg.add_reaction("🟢")

                def check2(reaction, user):
                    return user == message.author and str(reaction.emoji) == '🟢'

                try:
                    reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check2)
                except asyncio.TimeoutError:
                    await msg.clear_reactions()
                    break
                else:
                    await msg.clear_reactions()
                    rpsCheck = 1
                    localtime = time.asctime(time.localtime(time.time()))
                    await channelSend.send(f'**[{localtime}]** 🎮 **{message.author.display_name}** Has **played the game rps**: \n > `Channel: {message.channel}`\n > `Success:` <a:tick:811218936875319316>')
                    msgEmbed = discord.Embed(title="The Game is loading...", color=discord.Color.blue(),
                                             description="Once the game loads, you chose, rock, paper, or scissors. Now see if you win!")
                    msgEmbed.set_footer(
                        text="Discord Version - Lag is expected")
                    await msg.edit(embed=msgEmbed)
                    await asyncio.sleep(5)
            else:
                await msg.edit(embed=e)
                break


async def wrong(message, channelSend):
    localtime = time.asctime(time.localtime(time.time()))
    await channelSend.send(f'**[{localtime}]** 🎮 **{message.author.display_name}** Has **played the game rps**: \n > `Channel: {message.channel}`\n > `Success:` <a:reject:811218936452349986>')
