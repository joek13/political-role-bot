from discord.ext import commands
import discord

class Moderation:
    """Various commands to aid in moderating the server."""
    def __init__(self, bot, config):
        self.bot = bot
        self.config = config

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clean(self, ctx, number: int):
        """Removes some number of messages from chat."""
        if number > 100:
            number = 100
        elif number <= 0:
            return
        await ctx.channel.purge(limit=number, before=ctx.message)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def censor(self, ctx, user: discord.User):
        """Removes recent messages from an individual user."""
        await ctx.channel.purge(check=lambda message: message.author == user, before=ctx.message)
