import discord
from discord.ext import commands
import random

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix=commands.when_mentioned, description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def exit():
    await bot.logout()

@bot.command()
async def roll(dice : str):
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('Format has to be in NdN!')
        return

    result += roll for r in range(rolls))

    await bot.say(str(result))

bot.run('NDEwMTI4OTE4ODQ3NDIyNDc1.DVo84w.fuGi0d5IYNmefHNc6wD2lZeBSUo')
