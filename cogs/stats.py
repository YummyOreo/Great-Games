import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils import manage_commands
from extentions import wrong
import requests
import time
import level

guild_ids = []  # fill in


class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.guild_ids = bot.guild_ids
        self.version = bot.version
        self.bot_commands = bot.bot_commands

    @cog_ext.cog_slash(name="stats",
                       description="This shows your stats",
                       # 6

                       options=[manage_commands.create_option(
                           name="Choice",
                           description="Chose what stats you want!",
                           option_type=3,
                           required=True,
                           choices=[
                               {
                                   "name": "All",
                                   "value": "all"
                               },
                               {
                                   "name": "Level",
                                   "value": "level"
                               },
                               {
                                   "name": "Ball (Game)",
                                   "value": "ball"
                               },
                               {
                                   "name": "Shooter (Game)",
                                   "value": "shooter"
                               },
                               {
                                   "name": "Clicker (Game)",
                                   "value": "clicker"
                               },
                               {
                                   "name": "Type (Game)",
                                   "value": "type"
                               }
                           ]

                       ), manage_commands.create_option(
                           name="user",
                           description="Chose what user to get",
                           option_type=6,
                           required=False
                       )],
                       guild_ids=guild_ids,)
    async def _stats(self, ctx, Choice=None, user=None):
        print(ctx.command_id)
        print(Choice)
        if ctx.channel_id == self.bot_commands or ctx.guild is None:
            await ctx.respond()
            localtime = time.asctime(time.localtime(time.time()))
            command_Log = self.bot.get_channel()  # fill in
            await command_Log.send(f'**[{localtime}]** 📈 **{ctx.author.display_name}** Has **used the command stats**: \n > `Channel: {ctx.channel}`\n > `Choice: {Choice}`\n > `Success:` <a:tick:811218936875319316>')
            if user == None:
                levels = requests.get(f"http://127.0.0.1:5000/level/{ctx.author.id}",
                                      {"Type": "exp"})
            else:
                levels = requests.get(f"http://127.0.0.1:5000/level/{user.id}",
                                      {"Type": "exp"})
            levels = levels.json()
            exp = levels['exp']
            highScore = levels['highScore']
            ballW = levels['ballW']
            ballL = levels['ballL']
            shooterW = levels['shooterW']
            shooterL = levels['shooterL']
            typeW = levels['typeW']
            levelShow = level.api(levels["exp"])
            if Choice == "all":
                if user == None:
                    e = discord.Embed(title=f"**{ctx.author.display_name}'s stats**", color=discord.Color.blurple(),
                                      description='')
                else:
                    e = discord.Embed(title=f"**{user}'s stats**", color=discord.Color.blurple(),
                                      description='')
                e.add_field(name="**Level (All Games)**",
                            value=f"`{levelShow}`", inline=False)
                e.add_field(name="**EXP (All Games)**", value=f"`{exp}/{levelsCount[levelShow]}`",
                            inline=False)
                if levels["highScore"] == 0:
                    e.add_field(name="**Best Score (Clicker Game)**",
                                value=f"`Play to get a score`", inline=False)
                else:
                    e.add_field(name="**Best Score in clicker**",
                                value=f"`{highScore}`", inline=False)
                e.add_field(name="**Wins (Ball Game)**",
                            value=f"`{ballW}`", inline=False)
                e.add_field(name="**Loses (Ball Game)**",
                            value=f"`{ballL}`", inline=False)
                e.add_field(name="**Wins (Shooter Game)**",
                            value=f"`{shooterW}`", inline=False)
                e.add_field(name="**Loses (Shooter Game)**",
                            value=f"`{shooterL}`", inline=False)
                e.add_field(name="**Wins (Type Game)**",
                            value=f"`{typeW}`", inline=False)
                e.set_footer(text="Made by OreoDivision.")
                # sends the embed
            elif Choice == 'level':
                if user == None:
                    e = discord.Embed(title=f"**{ctx.author.display_name}'s stats**", color=discord.Color.blurple(),
                                      description='')
                else:
                    e = discord.Embed(title=f"**{user}'s stats**", color=discord.Color.blurple(),
                                      description='')
                e.add_field(name="**Level (All Games)**",
                            value=f"`{levelShow}`", inline=False)
                e.add_field(name="**EXP (All Games)**", value=f"`{exp}/{levelsCount[levelShow]}`",
                            inline=False)
                e.set_footer(text="Made by OreoDivision.")
            elif Choice == 'ball':
                e = discord.Embed(title=f"**{ctx.author.display_name}'s stats (Ball)**", color=discord.Color.blurple(),
                                  description='')
                e.add_field(name="**Wins (Ball Game)**",
                            value=f"`{ballW}`", inline=False)
                e.add_field(name="**Loses (Ball Game)**",
                            value=f"`{ballL}`", inline=False)
                e.set_footer(text="Made by OreoDivision.")
            elif Choice == 'shooter':
                if user == None:
                    e = discord.Embed(title=f"**{ctx.author.display_name}'s stats**", color=discord.Color.blurple(),
                                      description='')
                else:
                    e = discord.Embed(title=f"**{user}'s stats**", color=discord.Color.blurple(),
                                      description='')
                e.add_field(name="**Wins (Shooter Game)**",
                            value=f"`{shooterW}`", inline=False)
                e.add_field(name="**Loses (Shooter Game)**",
                            value=f"`{shooterL}`", inline=False)
                e.set_footer(text="Made by OreoDivision.")
            elif Choice == "clicker":
                if user == None:
                    e = discord.Embed(title=f"**{ctx.author.display_name}'s stats**", color=discord.Color.blurple(),
                                      description='')
                else:
                    e = discord.Embed(title=f"**{user}'s stats**", color=discord.Color.blurple(),
                                      description='')
                if levels["highScore"] == 0:
                    e.add_field(name="**Best Score (Clicker Game)**",
                                value=f"`Play to get a score`", inline=False)
                else:
                    e.add_field(name="**Best Score in clicker**",
                                value=f"`{highScore:.0f}`", inline=False)
                e.set_footer(text="Made by OreoDivision.")
            elif Choice == 'type':
                if user == None:
                    e = discord.Embed(title=f"**{ctx.author.display_name}'s stats**", color=discord.Color.blurple(),
                                      description='')
                else:
                    e = discord.Embed(title=f"**{user}'s stats**", color=discord.Color.blurple(),
                                      description='')
                e.add_field(name="**Wins (Type Game)**",
                            value=f"`{typeW}`", inline=False)
                e.set_footer(text="Made by OreoDivision.")
            await ctx.send(embed=e)
        else:
            await ctx.respond(eat=True)
            await wrong.wrong(ctx)
            localtime = time.asctime(time.localtime(time.time()))
            await channelSend.send(f'**[{localtime}]** 📈 **{ctx.author.display_name}** Has **used the command stats**: \n > `Channel: {ctx.channel}`\n > `Choice: {Choice}`\n > `Success:` <a:reject:811218936452349986>')


def setup(bot):
    bot.add_cog(Slash(bot))
