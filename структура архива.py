import discord
from config_dc import TOKEN
import requests


class YLBotClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} подключился и готов показать случайного котика (или пёсика!)')


    async def on_message(self, message):
        if message.author == self.user:
            return
        if 'кот' in message.content.lower() or 'кошка' in message.content.lower():
            response = requests.get("https://api.thecatapi.com/v1/images/search").json()
            await message.channel.send(f"{response[0]['url']}")
        elif 'пёс' in message.content.lower() or 'собач' in message.content.lower() or 'собак' in message.content.lower():
            response = requests.get("https://dog.ceo/api/breeds/image/random").json()
            await message.channel.send(f"{response['message']}")


intents = discord.Intents.default()
intents.members = True
client = YLBotClient(intents=intents)
client.run(TOKEN)
