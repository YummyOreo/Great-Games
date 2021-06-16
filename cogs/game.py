import discord
from discord.ext import commands
from discord_slash.utils import manage_commands
from discord_slash import cog_ext, SlashContext
import requests
import time
import extentions
from extentions import level
import extentionsV2
from extentionsV2 import game as g


guild_ids = [801084003301982219]


class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.guild_ids = bot.guild_ids
        self.levelCount = bot.levelCount
        self.bot_commands = bot.bot_commands

    @cog_ext.cog_slash(name="Play",
                       description="Play the game of your choice!",
                       options=[manage_commands.create_option(
                           name="Game",
                           description="Chose your game!",
                           option_type=3,
                           required=True,
                           choices=[
                               {
                                   "name": "Ball",
                                   "value": "ball"
                               },
                               {
                                   "name": "Shooter",
                                   "value": "shooter"
                               },
                               {
                                   "name": "Hole",
                                   "value": "hole"
                               },
                               {
                                   "name": "Clicker",
                                   "value": "clicker"
                               },
                               {
                                   "name": "Gamble",
                                   "value": "gamble"
                               },
                               {
                                   "name": "RPS",
                                   "value": "rps"
                               }
                           ]
                       )],
                       guild_ids=guild_ids
                       )
    async def _play(self, ctx, game):
        game_Log = self.bot.get_channel()  # fill in
        if ctx.channel_id == self.bot_commands:
            await ctx.respond()
            if game == 'ball':
                # API DONE
                await g.ball(ctx, game_Log, self.bot, level)
            elif game == 'shooter':
                # API DONE
                await g.shooter(ctx, game_Log, self.bot, level)
            elif game == 'hole':
                # API DONE
                await g.hole(ctx, game_Log, self.bot, level)
            elif game == 'clicker':
                # API DONE
                await g.clicker(ctx, game_Log, self.bot, level)
            elif game == 'gamble':
                # API DONE
                await g.gamble(ctx, game_Log, self.bot, level)
            elif game == 'rps':
                # API DONE
                await g.rps(ctx, game_Log, self.bot, level)
        else:
            await ctx.respond(eat=True)
            await g.wrong(ctx, game_Log, game)


def setup(bot):
    bot.add_cog(Slash(bot))
