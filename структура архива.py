from config_dc import TOKEN
import discord, pymorphy2
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True


class RandomThings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help_bot')
    async def help_bot(self, ctx):
        await ctx.send('Commands:\n'
                       '"#!numerals" for agreement with numerals\n'
                       '"#!alive" for define alive or not alive\n'
                       '"#!noun" for noun case (nomn, gent, datv, accs, ablt, loct) and number state (single, plural)\n'
                       '"#!inf" for infinitive state\n'
                       '"#!morph" for full morphological analysis')


    @commands.command(name='numerals')
    async def numerals(self, ctx, first, second):
        if first.isdigit():
            first, second = second, first
        morph = pymorphy2.MorphAnalyzer()
        comment = morph.parse(first)[0]
        await ctx.send(f"{second} {comment.make_agree_with_number(int(second)).word}")


    @commands.command(name='alive')
    async def alive(self, ctx, word):
        def sprgivoy():
            if words.tag.number == 'plur':
                return 'Живые'
            elif words.tag.gender == 'masc':
                return 'Живой'
            elif words.tag.gender == 'femn':
                return 'Живая'
            elif words.tag.gender == 'neut':
                return 'Живое'

        m = pymorphy2.MorphAnalyzer()
        words = m.parse(word)[0]
        if "NOUN" not in words.tag:
            await ctx.send('Не существительное')
        else:
            if words.tag.animacy == 'anim':
                await ctx.send(f"{word.capitalize()} {sprgivoy().lower()}")
            else:
                await ctx.send(f"{word.capitalize()} не {sprgivoy().lower()}")

    @commands.command(name='noun')
    async def noun(self, ctx, word, case, number):
        m = pymorphy2.MorphAnalyzer()
        await ctx.send(m.parse(word)[0].inflect({number[:-2], case}).word)

    @commands.command(name='inf')
    async def inf(self, ctx, word):
        m = pymorphy2.MorphAnalyzer()
        await ctx.send(m.parse(word)[0].normal_form)

    @commands.command(name='morph')
    async def mor(self, ctx, word):
        m = pymorphy2.MorphAnalyzer()
        await ctx.send(m.parse(word)[0])


bot = commands.Bot(command_prefix='#!', intents=intents)
bot.add_cog(RandomThings(bot))
bot.run(TOKEN)
