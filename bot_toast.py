# Python 3.6
import discord

from bot_token import imtoken

TOKEN = imtoken

print(TOKEN)

client = discord.Client()

@client.event
async def on_message(message):
    # prevent bot replying to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-------')

client.run(TOKEN)