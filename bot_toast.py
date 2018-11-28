#python3.6 required
import random
import asyncio
import aiohttp
import json

#import discord
from discord.ext.commands import Bot
from bot_token import imtoken

TOKEN = imtoken

#client = discord.Client()
BOT_PREFIX = ("?", "!")
client = Bot(command_prefix=BOT_PREFIX)


@client.event
async def on_message(message):
    # prevent bot replying to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('!bot'):
        await client.send_message(message.channel, "You summoned?")

    await client.process_commands(message)

@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'That. Is a no.',
        'Mmm. Really not looking likely mate',
        'Wee too hard to say',
        'It is a possibility',
        'Most certainly so',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)

@client.command()
async def square(num):
    squared_value = int(num) * int(num)
    await client.say(str(num) + " squared is " + str(squared_value))

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-------')

async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)

client.loop.create_task(list_servers())
client.run(TOKEN)
