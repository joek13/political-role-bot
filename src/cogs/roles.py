from discord.ext import commands
import logging

class Roles:
    """Commands that help with managing user roles."""
    
    def __init__(self, bot, config):
        self.bot = bot
        self.config = config

    async def on_ready(self):
        try:
            self.guild = next(x for x in self.bot.guilds if x.id == int(self.config["guild_id"]))
        except StopIteration as e:
            raise RuntimeError("The bot does not appear to be in a guild with the ID in config. Please either add the bot to this guild or change the guild ID.")

    def _get_role(self, role_name):
        role = next((x for x in self.config["roles"].keys() if x == role_name), None)
        if role != None:
            return int(self.config["roles"][role])
        else:
            return None

    @commands.command(aliases=["roleadd"])
    async def add(self, ctx, role):
        """Assigns `role` to this user."""
        role = role.lower().strip()
        role_id = self._get_role(role)
        if role_id != None:
            role = self.guild.get_role(role_id)
            member = self.guild.get_member(ctx.author.id)
            await member.add_roles(role)
            await ctx.send(f"You have been added to role `{role}`.")
        else:
            raise commands.CommandError(f"That role doesn't exist. Use `{self.bot.command_prefix}roles` for a list of roles.")

    @commands.command(aliases=["roledel"])
    async def remove(self, ctx, role):
        """Removes `role` from this user."""
        role = role.lower().strip()
        role_id = self._get_role(role)
        if role_id != None:
            role = self.guild.get_role(role_id)
            member = self.guild.get_member(ctx.author.id)
            await member.remove_roles(role)
            await ctx.send(f"You have been removed from role `{role}`.")
        else:
            raise commands.CommandError(f"That role doesn't exist. Use `{self.bot.command_prefix}roles` for a list of roles.")

    @commands.command()
    async def roles(self, ctx):
        """Lists available roles to take on."""
        roles = "\n".join(self.config["roles"].keys())
        await ctx.send(f"Here's a list of roles you can use:\n```md\n{roles}```")

