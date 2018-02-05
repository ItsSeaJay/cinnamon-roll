import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!logout'):
        await client.logout()

client.run('NDEwMTI4OTE4ODQ3NDIyNDc1.DVop5Q.j3jFteV-w0Z3KeBmdUFGF8C7HYU')
