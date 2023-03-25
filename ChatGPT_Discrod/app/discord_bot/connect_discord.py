from dotenv import load_dotenv
import os
import discord

from app.chatgpt_ai.connect_openai import chatgpt_response
load_dotenv()
discord_token=os.getenv('DISCORD_TOKEN')



class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as: ', self.user)

    async def on_message(self, message):
        print(message.content)
        if message.author == self.user:
             return
        await message.channel.send(f"You said: {message.content} \n {chatgpt_response(message.content)}")
intents=discord.Intents.default()
intents = discord.Intents(messages = True, guilds = True)
client=MyClient(intents=intents)
client.run(discord_token)