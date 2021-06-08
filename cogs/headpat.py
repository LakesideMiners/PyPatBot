import discord
import OS
from discord.ext import commands
import requests #Imports the requests library
import random #Imports the random library
USERAGENTSTRING = os.environ.get("UA")
HEADERS = {'user-agent': USERAGENTSTRING}
class headpat(commands.Cog):
    """Head Pats!"""
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='headpat', aliases=['headpats', 'pats', 'pat'], help="Get a random headpat image from r/headpats!")
    async def headpat(self, ctx):
        f = open("./headpatoff.txt", 'r')
        serversoff = f.read().splitlines()
        currentid = str(ctx.message.guild.id)
        if currentid in serversoff:
          await ctx.send("Sorry! This Command is disabled in this server! If you think this is an error, get an admin to bug LakesideMiners about it! UwU!")
          f.close()
          return
        else:
          f.close()
          hr = requests.get('https://reddit.com//r/headpats/random.json', headers=HEADERS, timeout=5)
          if (hr.status_code == requests.codes.ok):
            headpatjson = hr.json()
            imagevar = headpatjson[0]["data"]["children"][0]["data"]['url']
            #print(imagevar)
            permalinkredditpart = headpatjson[0]["data"]["children"][0]["data"]['permalink']
            #print(permalinkredditpart)
            saucevar = 'https://reddit.com/' + permalinkredditpart
            #print(saucevar)
            embed=discord.Embed(title="Headpats!",description="Headpats!" + "\n" + "[Sauce](" + saucevar + ")" )
            embed.set_image(url=imagevar)
            embed.set_footer(text="Powered by the Reddit API!")
            await ctx.send(embed=embed)   
          else:
            await ctx.send("Error! The site returned the status code: " + str(hr.status_code))


        
# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case SimpleCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(headpat(bot))
