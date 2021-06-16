import wrong
import discord
from discord.ext import commands


async def help(ctx, bot_commands):
    if ctx.channel_id == bot_commands or ctx.guild is None:
        await ctx.respond()
        e = discord.Embed(title=f"**All Commands**", color=discord.Color.blurple(),
                          description='')
        e.add_field(name="**▬▬▬▬Games▬▬▬▬**",
                    value="These are all of the games in <@>!", inline=False)  # fill in

        e.add_field(name="**Ball Game (`/play ball`)**",
                    value="Once you start the game, the bot will react with :white_medium_small_square:, reacting with it allows you to hit the ball into the goal.", inline=False)

        e.add_field(name="**Clicker Game (`/play clicker`)**",
                    value="Once you start the game, the bot will react with :frog: :hatched_chick: :heart: and :blue_circle:. In a random amount of time, one of the emojis will pop up. React with the emoji shown as fast as you can. Then youll get your score.", inline=False)

        e.add_field(name="**Gamble Game (`/play gamble`)**",
                    value="Once you start the game, youll see if you win the gamble or lose!", inline=False)

        e.add_field(name="**Shooter Game (`/play shooter`)**",
                    value="Once you start the game, the bot will react with ⚪, reacting with it allows you to shoot the gun, your goal is to kill the :person_frowning:.", inline=False)

        e.add_field(name="**Hole Game (`/play hole`)**",
                    value="Once the game loads, youll a hole and a ball, youll need to press :baseball: to trow the ball into the hole when it lines up!", inline=False)

        e.add_field(name="**Type Game (`/premium games type`)**",
                    value="Only for premium!", inline=False)

        e.add_field(name="**RPS Game (`/play rps`)**",
                    value="Once the game loads, you chose, rock, paper, or scissors. Now see if you win!", inline=False)

        e.add_field(name="**▬▬▬▬Everyone▬▬▬▬**",
                    value="These are commands that can be used by @everyone!", inline=False)
        e.add_field(name="**About command (`/about`)**",
                    value="Shows info about this bot.", inline=False)
        # Not Done
        e.add_field(name="**Link command (`/about link`)**",
                    value="See the lates update!", inline=False)
        # Done
        e.add_field(name="**Stats command (`/stats`)**",
                    value="Shows your stats for our games!", inline=False)
        # Not Done
        e.add_field(name="**Leaderboard command (`/leaderboard`)**",
                    value="Coming soon!", inline=False)

        e.add_field(name='▬▬▬▬To see a full list of command▬▬▬▬',
                    value='')  # fill in
        await ctx.author.send(embed=e)
    else:
        await ctx.respond(eat=True)
        await wrong.wrong(ctx)
