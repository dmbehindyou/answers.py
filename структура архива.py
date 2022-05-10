from config_dc import TOKEN, API_KEY
import discord
from discord.ext import commands
from requests import request
from pprint import pprint
intents = discord.Intents.default()
intents.members = True
places = dict()


class RandomThings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help_bot')
    async def help_bot(self, ctx):
        await ctx.send('Commands:\n'
                       '"#!place" for change weather forecast location\n'
                       '"#!current" for give a now weather forecast\n'
                       '"#!forecast <day>" to get weather forecast for several days')

    @commands.command(name='place')
    async def set_place(self, ctx, place):
        places[str(ctx.author)] = place
        await ctx.send(f'Place changed to {place}')

    @commands.command(name='current')
    async def current(self, ctx):
        if str(ctx.author) not in places:
            await ctx.send("Please, select the location of the weather forecast")
        else:
            response = request(
                method='GET',
                url='http://api.weatherstack.com/current',
                params={
                    'access_key': API_KEY,
                    'query': places[str(ctx.author)]
                }
            )
            if response.status_code == 200:
                response = response.json()
                d, t = response["location"]["localtime"].split()
                await ctx.send(f'Current weather in {response["location"]["name"]} today {d} at time {t}:\n'
                               f'Temperature: {response["current"]["temperature"]},\n'
                               f'Pressure: {response["current"]["pressure"]},\n'
                               f'Humidity: {response["current"]["humidity"]},\n'
                               f'{response["current"]["weather_descriptions"][0]},\n'
                               f'Wind {response["current"]["wind_dir"]}, {response["current"]["wind_speed"]} m/s.')
            else:
                await ctx.send("Please select the existing location")

    @commands.command(name='forecast')
    async def forecast(self, ctx, days):
        if str(ctx.author) not in places:
            await ctx.send("Please, select the location of the weather forecast")
        else:
            response = request(
                method='GET',
                url='http://api.weatherstack.com/current',
                params={
                    'access_key': API_KEY,
                    'query': places[str(ctx.author)],
                    'forecast_days': int(days),
                    'hourly': 1
                }
            )
            if response.status_code == 200:
                response = response.json()
                ans = ''
                pprint(response)
                for i in response["forecast"]:
                    ans += f'Weather forecast in {response["location"]["name"]} for {response["forecast"][i]["date"]}:\n' + \
                           f'Temperature: {response["forecast"][i]["avgtemp"]},\n' + \
                           f'Pressure: {response["forecast"][i]["hourly"][0]["pressure"]},\n' + \
                           f'Humidity: {response["forecast"][i]["hourly"][0]["humidity"]},\n' + \
                           f'{response["forecast"][i]["hourly"][0]["weather_descriptions"][0]},\n' + \
                           f'Wind {response["forecast"][i]["hourly"][0]["wind_dir"]}, {response["forecast"][i]["hourly"][0]["wind_speed"]} m/s.\n\n'
                await ctx.send(ans)
            else:
                await ctx.send("Please select the existing location")


bot = commands.Bot(command_prefix='#!', intents=intents)
bot.add_cog(RandomThings(bot))
bot.run(TOKEN)
