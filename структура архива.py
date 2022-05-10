from config_dc import TOKEN, API_KEY
import discord
from discord.ext import commands
from requests import request
import emoji, random
intents = discord.Intents.default()
intents.members = True
ans = set()
emodjies = emoji.EMOJI_UNICODE_ENGLISH
for k, v in emodjies.items():
    ans.add(v[0])
ans = list(ans)
users = dict()


class RandomThings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='start')
    async def start(self, ctx):
        random.shuffle(ans)
        smiles_in_game = ans[:random.randrange(50, 150)]
        users[str(ctx.author)] = [smiles_in_game, 0, 0]
        await ctx.send(f'The game started')

    @commands.command(name='stop')
    async def forecast(self, ctx):
        del users[str(ctx.author)]
        await ctx.send("You can play again")

    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        try:
            y = users[str(message.author)][1]
            b = users[str(message.author)][2]
            if len(users[str(message.author)][0]) <= 1:
                await message.dm_channel.send(f"Emoticons are over\n"
                                              f"Score: You {y} Bot {b}\n"
                                              f"{'You' if y > b else 'Bot'} win!")
                del users[str(message.author)]
            else:
                number = int(message.content)
                if number >= len(users[str(message.author)][0]):
                    your_emoji = users[str(message.author)][0][len(users[str(message.author)][0]) % number]
                    bot_emoji = random.randrange(len(users[str(message.author)][0]))
                    if your_emoji > users[str(message.author)][0][bot_emoji]:
                        users[str(message.author)][1] += 1
                    else:
                        users[str(message.author)][2] += 1
                    y = users[str(message.author)][1]
                    b = users[str(message.author)][2]
                    await message.dm_channel.send(f"Your emoji {your_emoji}\n"
                                                  f"Bot emoji {users[str(message.author)][0][bot_emoji]}\n"
                                                  f"Score: You {y} Bot {b}\n")
                    del users[str(message.author)][0][len(users[str(message.author)][0]) % number]
                    del users[str(message.author)][0][bot_emoji - 1]
                else:
                    your_emoji = users[str(message.author)][0][number]
                    bot_emoji = random.randrange(len(users[str(message.author)][0]))
                    if your_emoji > users[str(message.author)][0][bot_emoji]:
                        users[str(message.author)][1] += 1
                    else:
                        users[str(message.author)][2] += 1
                    y = users[str(message.author)][1]
                    b = users[str(message.author)][2]
                    await message.dm_channel.send(f"Your emoji {your_emoji}\n"
                                                  f"Bot emoji {users[str(message.author)][0][bot_emoji]}\n"
                                                  f"Score: You {y} Bot {b}\n")
                    del users[str(message.author)][0][number]
                    del users[str(message.author)][0][bot_emoji - 1]
        except:
            await message.dm_channel.send("Please, send correct number")


bot = commands.Bot(command_prefix='#!', intents=intents)
bot.add_cog(RandomThings(bot))
bot.run(TOKEN)
