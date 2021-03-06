from discord.ext import commands
import logging


class Roles:
    """Commands that help with managing user roles."""

    def __init__(self, bot, config):
        self.bot = bot
        self.config = config

    async def on_ready(self):
        try:
            self.guild = next(x for x in self.bot.guilds if x.id == int(
                self.config["guild_id"]))
        except StopIteration as e:
            raise RuntimeError(
                "The bot does not appear to be in a guild with the ID in config. Please either add the bot to this guild or change the guild ID.")

    def _get_role(self, role_name):
        role = next(
            (x for x in self.config["roles"].keys() if x == role_name), None)
        if role != None:
            return int(self.config["roles"][role])
        else:
            return None

    @commands.group()
    async def role(self, ctx):
        """Commands for adding/removing roles."""
        if ctx.invoked_subcommand is None:
            roles = list(self.config["roles"].keys())
            roles_text = "\n".join(roles)
            await ctx.send(f"Available roles:\n```md\n{roles_text}```\nYou can add a role like this:\n```md\n{self.bot.command_prefix}role add {roles[0]}```\nSee `{self.bot.command_prefix}help role` for help.")

    @role.command()
    async def add(self, ctx, *roles):
        """Assigns `roles` to this user."""
        roles_processed = []
        for role in roles:  # iterate over each role, verify it, and add its Role object to a list
            role = role.lower().strip()
            role_id = self._get_role(role)
            if role_id != None:
                role = self.guild.get_role(role_id)
                roles_processed.append(role)
            else:
                raise commands.CommandError(
                    f"Role `{role}` doesn't exist. Use `{self.bot.command_prefix}roles` for a list of roles.")

        member = self.guild.get_member(ctx.author.id)
        await member.add_roles(*roles_processed)
        await ctx.send(f"You have been added to role(s) `{', '.join([x.name for x in roles_processed])}`.")

    @role.command()
    async def remove(self, ctx, *roles):
        """Removes `roles` from this user."""
        roles_processed = []
        for role in roles:  # iterate over each role, verify it, and add its Role object to a list
            role = role.lower().strip()
            role_id = self._get_role(role)
            if role_id != None:
                role = self.guild.get_role(role_id)
                roles_processed.append(role)
            else:
                raise commands.CommandError(
                    f"Role `{role}` doesn't exist. Use `{self.bot.command_prefix}roles` for a list of roles.")

        member = self.guild.get_member(ctx.author.id)
        await member.remove_roles(*roles_processed)
        await ctx.send(f"You have been removed from role(s) `{', '.join([x.name for x in roles_processed])}`.")

    @role.command()
    @commands.has_permissions(administrator=True)
    @commands.guild_only()
    async def generate_config(self, ctx):
        """Generates a config file with all roles on the server. For admin use only."""
        roles = ctx.guild.roles
        config_text = "[roles]\n" + \
            "\n".join(
                [f"\"{role.name.lower()}\"=\"{role.id}\"" for role in roles])  # ignore this mess pls
        await ctx.send(f"Here you go, fresh from the oven:\n```md\n{config_text}```")

    @role.command()
    async def list(self, ctx):
        """Lists available roles to take on."""
        roles = "\n".join(self.config["roles"].keys())
        await ctx.send(f"Here's a list of roles you can use:\n```md\n{roles}```")
