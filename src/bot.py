import discord
import config
from discord.ext import commands

cfg = config.load_config(config_path="./config.toml")

bot = commands.Bot(command_prefix=cfg["command_prefix"])

def run():
    bot.run(cfg["token"])
