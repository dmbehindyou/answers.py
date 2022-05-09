import discord
from config_dc import TOKEN
import asyncio


class YLBotClient(discord.Client):
    async def on_message(self, message):
        if message.author == self.user:
            return
        try:
            hours = int(message.content.split()[2])
            minutes = int(message.content.split()[5])
            await message.channel.send(f"The timer should start in {hours} hours and {minutes} minutes")
            await asyncio.sleep(minutes * 60 + hours * 60 * 60)
            await message.channel.send("Time X has come!")
        except:
            await message.channel.send(f"Please write your message in the format:\n"
                                       f"set_timer in <number> hours and <number> minutes")


intents = discord.Intents.default()
intents.members = True
client = YLBotClient(intents=intents)
client.run(TOKEN)
