from config_dc import TOKEN
import discord
from discord.ext import commands
import requests

intents = discord.Intents.default()
intents.members = True
peoples = dict()


class RandomThings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help_bot')
    async def help_bot(self, ctx):
        await ctx.send('Commands:\n'
                       '"!!set_lang" for change languages, default: en-ru\n'
                       '"!!text" for give translated text')

    @commands.command(name='set_lang')
    async def set_lang(self, ctx, languages):
        peoples[str(ctx.author)] = "|".join(languages.split('-'))
        await ctx.send(f'Type "!!text" and text for translate')

    @commands.command(name='text')
    async def mor(self, ctx, *words):
        if str(ctx.author) not in peoples:
            url = "https://translated-mymemory---translation-memory.p.rapidapi.com/api/get"
            querystring = {"langpair": "en|ru", "q": " ".join(words), "mt": "1", "onlyprivate": "0", "de": "a@b.c"}
            headers = {
                "X-RapidAPI-Host": "translated-mymemory---translation-memory.p.rapidapi.com",
                "X-RapidAPI-Key": "a4a800dbfcmsh5109ca6d95d73e7p1cef61jsnbeee0db76130"
            }
            response = requests.request("GET", url, headers=headers, params=querystring).json()
            await ctx.send(response["responseData"]['translatedText'])
        else:
            url = "https://translated-mymemory---translation-memory.p.rapidapi.com/api/get"
            querystring = {"langpair": peoples[str(ctx.author)], "q": " ".join(words), "mt": "1", "onlyprivate": "0", "de": "a@b.c"}
            headers = {
                "X-RapidAPI-Host": "translated-mymemory---translation-memory.p.rapidapi.com",
                "X-RapidAPI-Key": "a4a800dbfcmsh5109ca6d95d73e7p1cef61jsnbeee0db76130"
            }
            response = requests.request("GET", url, headers=headers, params=querystring).json()
            await ctx.send(response["responseData"]['translatedText'])


bot = commands.Bot(command_prefix='!!', intents=intents)
bot.add_cog(RandomThings(bot))
bot.run(TOKEN)
