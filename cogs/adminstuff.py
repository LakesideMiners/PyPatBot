## DO NOT USE THIS COG RIGHT NOW! ITS BROKEN!
import discord
from discord.ext import commands

class adminstuff(commands.Cog):
    """Admin Stuff!"""
    
    def __init__(self, bot):
        self.bot = bot
    
    # Am I Admin
    @commands.command(name='amiadmin', help='Checks if you have the administrator perm serverwide, if its only in a channel, it wont count.')
    @commands.has_guild_permissions(administrator=True)
    async def amiadmin(self, ctx):
      try:
        await ctx.send("You have serverwide administrator perms")
      except discord.MissingPermissions:
        await ctx.send("You do not have serverwide administrator perms")

    # Headpat Off
    @commands.command(name='headpatoff', help="Disables The Headpat command in the server, else, will say its already disabled")
    @commands.has_guild_permissions(administrator=True)
    async def headpatoff(self, ctx):
      try:
        f = open("./headpatoff.txt", 'r')
        serversoff = f.read().splitlines()
        currentid = str(ctx.message.guild.id)
        f.close()
        if currentid in serversoff:
          await ctx.send("The Headpat command is already disabled!")          
        else:
          f = open('./headpatoff.txt', 'a+')
          currentid = str(ctx.message.guild.id)
          f.write('\n' + currentid)
          f.close()
          await ctx.send("Disabled")
      except discord.MissingPermissions:
        await ctx.send("You do not have serverwide administrator perms")

    # Headpat on
    @commands.command(name='headpaton', help="Enables  The Headpat command in the server, else, will say its already enabled")
    @commands.has_guild_permissions(administrator=True)
    async def headpaton(self, ctx):
      try:
        f = open("./headpatoff.txt", 'r')
        serversoff = f.read().splitlines()
        currentid = str(ctx.message.guild.id)
        f.close()
        if currentid not in serversoff:
          await ctx.send("The Headpat command is already enabled!")          
        else:
          f = open('./headpatoff.txt', 'r+')
          currentid = str(ctx.message.guild.id)
          for line in f:
            line = line.replace(currentid, "")
          f.close()

          await ctx.send("Enabled")
      except discord.MissingPermissions:
        await ctx.send("You do not have serverwide administrator perms")
        
        
# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case SimpleCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(adminstuff(bot))