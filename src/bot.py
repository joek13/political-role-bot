import discord
import config
import logging
from discord.ext import commands
from cogs import roles, error, welcome, mod

cfg = config.load_config(config_path="./config.toml")

bot = commands.Bot(command_prefix=cfg["command_prefix"])

COGS = [roles.Roles, error.CommandErrorHandler,
        welcome.Welcome, mod.Moderation]


def add_cogs():
    for cog in COGS:
        logging.info(f"Enabling cog {cog.__module__}...")
        bot.add_cog(cog(bot, cfg))  # initialize cog with bot and config


@bot.event
async def on_ready():
    logging.info(f"Logged in as {bot.user.name}")


@bot.event
async def on_guild_join(guild):
    if guild.id != cfg["guild_id"]:  # leave other guilds
        logging.info(f"Added to guild ID {guild.id}. Leaving...")
        await guild.leave()


def run():
    add_cogs()
    bot.run(cfg["token"])
