import discord
from discord.ext import commands
class credits(commands.Cog):
    """da credits"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='credits', help='Credits')
    async def credits(self, ctx):
      embed=discord.Embed(title="Credits", description="The Credits!", color=0x00ff91)
      embed.add_field(name="Bot Creator!", value="<@820921656129486909>", inline=False)
      embed.add_field(name="Sheri API", value="https://sheri.bot/", inline=True)
      embed.add_field(name="Headpats Source", value="https://reddit.com/r/headpats", inline=True)
      embed.add_field(name="COVID-19 API", value="https://rapidapi.com/Gramzivi/api/covid-19-data", inline=True)
      await ctx.send(embed=embed)
      

def setup(bot):
    bot.add_cog(credits(bot))