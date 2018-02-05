import discord
import asyncio

client = discord.Client()
user = discord.User()
token = 'NDEwMTI4OTE4ODQ3NDIyNDc1.DVop5Q.j3jFteV-w0Z3KeBmdUFGF8C7HYU'

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!exit'):
        await client.logout()
    elif user.mentioned_in(message):
        await client.send_message(message.channel, 'Cinnamon Roll')

client.run(token)
