import discord
import config
import logging
from discord.ext import commands
from cogs import roles, error

cfg = config.load_config(config_path="./config.toml")

bot = commands.Bot(command_prefix=cfg["command_prefix"])

COGS = [roles.Roles, error.CommandErrorHandler]

def add_cogs():
    for cog in COGS:
        logging.info(f"Enabling cog {cog.__module__}...")
        bot.add_cog(cog(bot, cfg)) # initialize cog with bot and config

def run():
    add_cogs()
    bot.run(cfg["token"])
