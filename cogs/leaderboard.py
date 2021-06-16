import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils import manage_commands
import requests
from extentions import level

guild_ids = []  # fill in


class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.guild_ids = bot.guild_ids
        self.bot_commands = bot.bot_commands

    @cog_ext.cog_slash(name="Leaderboard",
                       description="Coming Soon! (Premium Only)",
                       guild_ids=guild_ids)
    async def _Leaderboard(self, ctx):
        if ctx.channel_id == self.bot_commands or ctx.guild is None:
            role = discord.utils.find(
                lambda r: r.name == 'Premium', ctx.guild.roles)
            if role in ctx.author.roles:
                levels = requests.get(f"http://127.0.0.1:5000/lb/exp")
                levels = levels.json()
                levelShow = level.api(levels['exp'])
                e = discord.Embed(title=f"**Leaderboard**", color=discord.Color.blurple(),
                                  description='')
                e.add_field(name="**Level**",
                            value=f"<@{levels['id']}> at `{levelShow}`", inline=False)
                await ctx.respond()
                await ctx.send(embed=e)
            else:
                await ctx.respond(eat=True)
                await ctx.send("Coming Soon", hidden=True)
        else:
            await ctx.respond(eat=True)
            await ctx.send("Coming Soon", hidden=True)


def setup(bot):
    bot.add_cog(Slash(bot))
