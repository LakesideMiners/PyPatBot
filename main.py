import discord
import os 
import requests
import random
from discord.ext import commands
from dotenv import load_dotenv
from datetime import datetime
now = datetime.now()
from pythonping import ping
load_dotenv()
#sets the bot prefix to "$" and set the bots presence
bot = commands.Bot(command_prefix='$', activity=discord.Game('UwU'))
@bot.event
async def on_ready():
    print("I'm in and ready!") 

@bot.event
async def on_command_error(ctx, error):
  await ctx.send(f"An error occured: {str(error)}")

#Cogs to load
initial_extensions = ['cogs.headpat', 'cogs.animalimages', 'cogs.credits', 'cogs.covid']
if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)
token = os.environ.get("DISCORD_BOT_SECRET")
bot.run(token)

