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

    @cog_ext.cog_slash(name="About",
                       description="About !",  # fill in
                       options=[manage_commands.create_option(
                           name="Chose",
                           description="Chose what you want to know about !",  # fill in
                           option_type=3,
                           required=True,
                           choices=[
                               {
                                   "name": "",  # fill in
                                   "value": "about"
                               },
                               {
                                   "name": "Website link",
                                   "value": "link"
                               }
                           ]
                       )],
                       guild_ids=guild_ids
                       )
    async def _about(self, ctx, Chose):
        if ctx.channel_id == self.bot_commands or ctx.guild is None:
            await ctx.respond()
            if Chose == 'about':
                e = discord.Embed(title=f"**About **",  # fill in
                                  color=discord.Color.blurple(), description='')
                e.add_field(name="**Made By:**",
                            value=f"`OreoDivision#0001 (647959906170699776)`", inline=False)

                e.add_field(name="**Upgrades:**",
                            value=f"`Premium | /premium`", inline=False)

                e.add_field(name="**Level Cap:**",
                            value=f"`25`", inline=False)

                e.add_field(name="**Version:**",
                            value=f"`{self.version}`", inline=False)

                e.add_field(name="**Ping:**",
                            value=f"`{self.bot.latency * 1000:.2f}`", inline=False)

                e.add_field(name="**Prefix:**",
                            value=f"`gg!` and `/`", inline=False)

                e.add_field(name="**Play command:**",
                            value=f"`/play`", inline=False)

                e.add_field(name="**Server:**",
                            value=f"``", inline=False)  # fill in

                e.set_footer(text='Have Fun!')
            elif Chose == 'link':
                e = discord.Embed(title=f"**Link to our website:**", color=discord.Color.blurple(),
                                  description='')  # fill in
            await ctx.send(embed=e)
        else:
            await ctx.respond(eat=True)
            await wrong.wrong(ctx)


def setup(bot):
    bot.add_cog(Slash(bot))
