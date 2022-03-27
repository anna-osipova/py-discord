import os

import discord
from decouple import config
import help
import read_words

TOKEN = config('DISCORD_TOKEN')
GUILD = config('DISCORD_GUILD')

client = discord.Client()

words = read_words.read_words()


@client.event
async def on_ready():
    for g in client.guilds:
        guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content[0:5] == '/help':
        suggestions = help.give_help(words, message.content[5:].strip())
        await message.channel.send(', '.join(suggestions))

client.run(TOKEN)

client.run(TOKEN)
