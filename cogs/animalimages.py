## add other endpoints, bunny, cat, wolf, etc.
## make process of getting the URLs and making the embed a funcion? (just to make code look nicer and easer to manage)
## 
import discord
from discord.ext import commands
from SheriAPI import SheriAPI
HEADERS = {'user-agent': 'RedsHeadPatBot/1.3.0'}
class animalimages(commands.Cog):
    """Animal Images"""
    
    def __init__(self, bot):
        self.bot = bot
    
    # Fox
    @commands.command(name='fox', aliases=['foxo', 'foxes'], help='Get A Fox Picture!')
    async def foximage(self, ctx):
      async with ctx.typing():
        await ctx.send(embed=await getsheimage(str('fox')))

    # Wolf
    @commands.command(name='wolf', help='Get A Wolf Picture!')
    async def wolfimage(self, ctx):
      async with ctx.typing():
        await ctx.send(embed=await getsheimage(str('wolves')))

    # Bunny
    @commands.command(name='bunny', help='Get A Bunny Picture!')
    async def bunnyimage(self, ctx):
      async with ctx.typing():
        await ctx.send(embed=await getsheimage(str('bunny')))

    # Cat
    @commands.command(name='cat', help='Get A Cat Picture!')
    async def catimage(self, ctx):
      async with ctx.typing():
        await ctx.send(embed=await getsheimage(str('cat')))

    # Husky
    @commands.command(name='husky', help='Get A Husky Picture!')
    async def huskyimage(self, ctx):
      async with ctx.typing():
        await ctx.send(embed=await getsheimage(str('husky')))
## Api Function
async def getsheimage(kind):
  sapi = SheriAPI()
  imageres = await sapi.get(kind)
  embed=discord.Embed(title=str(kind) + "!", description="[Direct Link to image on API]("+ imageres.url + ")\n" + "[Report Image to API Devs](" + imageres.report_url + ")")
  # Set the image
  embed.set_image(url=imageres.url)
  # API Credit
  embed.set_footer(text="Powered by the Sheri Blossom API!")
  return embed
  pass
# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case SimpleCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(animalimages(bot))
