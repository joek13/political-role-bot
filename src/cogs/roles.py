from discord.ext import commands

class Roles:
    """Commands that help with managing user roles."""
    
    def __init__(self, bot, config):
        self.bot = bot
        self.config = config

    @commands.command(aliases=["roleadd"])
    async def add(self, ctx, role):
        """Assigns a role to this user."""
        pass

    @commands.command(aliases=["roledel"])
    async def remove(self, ctx, role):
        """Removes a role from this user."""
        pass
