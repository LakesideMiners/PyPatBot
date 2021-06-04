import discord
import requests
from discord.ext import commands
import os
from datetime import datetime

apikey = os.environ.get("x_rapidapi_key")
headers = {
  'x-rapidapi-key' : apikey,
  'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
}
class covid(commands.Cog):
    """Covid Related Data"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='covid', help='Get covid data for a country')
    async def covid(self, ctx, arg):
      f = open("./validcountrycodes.txt", 'r')
      validcodes = f.read().splitlines()
      f.close()
      if arg.upper() in validcodes:
        url = "https://covid-19-data.p.rapidapi.com/country/code?code=" + str(arg)
        print(url)
        r = requests.get(url, headers=headers)
        print(r.text)
        covid_data = r.json()
        print(covid_data)
        country_var = covid_data[0]["country"]
        print(country_var)
        confirmed_var = covid_data[0]["confirmed"]
        recovered_var = covid_data[0]["recovered"]
        critical_var = covid_data[0]["critical"]
        deaths_var = covid_data[0]["deaths"]
        last_change_var = covid_data[0]["lastChange"]
        last_update_var = covid_data[0]["lastUpdate"]
        embed=discord.Embed(title="Covid Data for " + str(country_var), description="Last change was at " + str(last_change_var))
        embed.add_field(name="Confirmed cases", value=confirmed_var, inline=True)
        embed.add_field(name="Recovered", value=recovered_var, inline=True)
        embed.add_field(name="Critical", value=critical_var, inline=True)
        embed.add_field(name="Deaths", value=deaths_var, inline=True)
        embed.add_field(name="Last Change In Data", value=last_change_var, inline=True)
        embed.set_footer(text="Last Refreshed At: " + str(last_update_var) )
        await ctx.send(embed=embed)
      else:
        await ctx.send("Invalid Alpha 2 County Code! for a list of valid codes. Please see https://www.nationsonline.org/oneworld/country_code_list.htm and look under the Alpha 2 column!")

# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(covid(bot))

          