from discord.ext import commands


class Welcome:
    """Welcomes users to the guild with a helpful message."""

    def __init__(self, bot, config):
        self.bot = bot
        self.config = config

    async def _send_welcome_message(self, member):
        roles = "\n".join(self.config["roles"].keys())
        await member.send(f"Hello {member.name}, welcome to {member.guild.name}!\nPlease make sure you read through the rules over in <#{self.config['rules_channel_id']}>.\nBefore you join in the conversation, you might wish to add a couple roles as political identifiers. This is totally optional, so feel free to skip this step.\n\nHere are the available roles:```md\n{roles}```You can add them like this:```md\n^add {list(self.config['roles'].keys())[0]}```If you think a role is missing, please DM <@{self.config['owner_id']}>.\nThat's all for now! Have fun!")

    async def on_member_join(self, member):
        await self._send_welcome_message(member)

    @commands.command()
    @commands.guild_only()
    async def welcome(self, ctx):
        """Re-sends the guild welcome message, just in case you need it."""
        await self._send_welcome_message(ctx.author)
