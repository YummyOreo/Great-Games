import random
import asyncio
import time
import requests
import discord
from discord.ext import commands
from discord_slash.utils import manage_commands
from discord_slash import cog_ext, SlashContext

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
                    await msg.delete()
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

async def wrong(message, channelSend, game):
	await message.author.send(embed=discord.Embed(title=f"<a:reject:811218936452349986> | You cannot use that command in {message.channel}.", color=discord.Color.red(), description="<a:tick:811218936875319316> | You can use that command in: <#801084004748099589>."))
	localtime = time.asctime(time.localtime(time.time()))
	await channelSend.send(f'**[{localtime}]** 🎮 **{message.author.display_name}** Has **played the game {game}**: \n > `Channel: {message.channel}`\n > `Success:` <a:reject:811218936452349986>')

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
                    await msg.delete()
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
    await asyncio.sleep(60)
    await msg.delete()


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
                    await msg.delete()
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
                    await msg.delete()
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
                    await msg.delete()
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