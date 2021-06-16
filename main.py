import discord
from discord.ext import commands
from os import system
import time
import wrong
import discord_slash
from discord_slash import SlashCommand
from discord_slash.utils import manage_commands
import requests
import level
import type

bot = commands.Bot(command_prefix="gg!")
bot.remove_command("help")
slash = SlashCommand(bot, sync_commands=True)
guild_ids = []  # fill in
bot.guild_ids = guild_ids
levelsCount = [100, 300, 600, 1000, 1500, 2100, 2850, 3850, 4000, 5900, 7500, 8050, 10000,
               15000, 30000, 55000, 70000, 95000, 100000, 110000, 122000, 145000, 159000, 200000, 250000, 400000, 800000, 1300000, 1750000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000]
bot.levelCount = levelsCount

global game
global word
# fill in
bot_commands =
bot.bot_commands = bot_commands
game = ''
word = None
version = '1.0.1.4'
bot.version = version


@bot.event
async def on_ready():
    # await discord_slash.utils.manage_commands.remove_slash_command(
    #    bot id, 'Token', guild, cmd id)
    localtime = time.asctime(time.localtime(time.time()))
    channelSend = bot.get_channel()  # fill in
    await channelSend.send(f"**[{localtime}]** The **Main** file is __Online__ \n > <a:tick:811218936875319316>\n > `Staus: /help | Version {version} | By OreoDivision#0001`")
    await bot.change_presence(activity=discord.Game(name=f"/help | Version {version} | By OreoDivision#0001"))


@slash.slash(
    name="Premium",
    description="A Premium version of !",  # fill in
    options=[manage_commands.create_option(
        name="Games",
        description="Chose your game (Only For Premium People!)",
        option_type=3,
        required=False,
        choices=[
                {
                    "name": "Type",
                    "value": "type"
                }
        ]
    ), manage_commands.create_option(
        name="ReType",
        description="(Type Game) Retype the phrase!",
        option_type=3,
        required=False
    )],

    guild_ids=guild_ids,
)
async def _Premium(ctx, games=None, ReType=None):
    global word
    print(ctx.command_id)
    if ctx.channel_id == bot_commands or ctx.guild is None:
        role = discord.utils.find(
            lambda r: r.name == 'Premium', ctx.guild.roles)
        if role in ctx.author.roles:
            if games == None:
                await ctx.respond()
                e = discord.Embed(title=f"** Premium!!!**", color=discord.Color.blurple(),
                                  description='')
                e.add_field(name="**🎉 You have Premium 🎉**",
                            value=f"`Now go and enjoy it!`", inline=False)
                e.add_field(name="**What You Get:**",
                            value=f"`- Play again reaction \n - Beta games (/premium games) \n - Early access (/premium) \n - Access to the /Leaderboard command!`", inline=False)
                await ctx.send(embed=e)
            elif games == 'type' and ReType == None and game == '':
                await ctx.respond()
                word = await type.first(ctx, bot)
                return

            if ReType == word:
                await ctx.respond()
                game == ''
                word == None
                await type.second(ctx, bot)
            else:
                print(ReType)
                print(word)
                await ctx.respond(eat=True)
                await ctx.send("Try Again", hidden=True)
        else:
            await ctx.respond()
            e = discord.Embed(title=f"** Premium**",  # fill in
                              color=discord.Color.blurple())
            e.add_field(name="**How to Get Premium:**",
                        value=f"`Buy it from LogiBot! +p rewards`", inline=False)
            e.add_field(name="**What You Get:**",
                        value=f"`- Play again reaction \n - Beta games (/premium games) \n - Early access (/premium) \n - Access to the /Leaderboard command!`", inline=False)
            await ctx.send(embed=e)
    else:
        await ctx.respond(eat=True)
        await wrong.wrong(ctx)

bot.load_extension("cogs.leaderboard")
bot.load_extension("cogs.about")
bot.load_extension("cogs.game")
bot.load_extension("cogs.help")
bot.load_extension("cogs.stats")
bot.load_extension("cogs.ping")
bot.run("")  # fill in
