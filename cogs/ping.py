import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils import manage_commands
from extentions import wrong

guild_ids = []  # fill in


class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.guild_ids = bot.guild_ids
        self.version = bot.version
        self.bot_commands = bot.bot_commands

    @cog_ext.cog_slash(name="ping",
                       description="This will ping you when there is a new  relese",  # fill in
                       guild_ids=guild_ids,)
    async def _ping(self, ctx):
        await ctx.respond(eat=True)
        member = ctx.author
        role = discord.utils.get(ctx.guild.roles, name="")  # fill in
        roleCheck = discord.utils.find(
            lambda r: r.name == '', ctx.guild.roles)  # fill in
        if roleCheck not in ctx.author.roles:
            await ctx.author.add_roles(role)
            await ctx.send('Adds <@&> to you!', hidden=True)  # fill in
            return
        await self.bot.remove_roles(member, role)


def setup(bot):
    bot.add_cog(Slash(bot))
