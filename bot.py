import discord
import responses
from discord.ext import commands

#stuff below is for the counter
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
KEYWORD = 'nigger'
KEYWORD2 = '!count'
count = 28

async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'MTEyOTYxOTQyODk1MTIwODA0Ng.G48DVf.MbJ41GZqL3n74FkphUTCQ0I_VdcoyZwqEkr1mA'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)
        
        if message.author.bot:
            return

        if KEYWORD in message.content:
            global count
            count += 1

        if KEYWORD2 in message.content:
            await message.channel.send(f'Nigger has been said for {count} times')

        await bot.process_commands(message)

    client.run(TOKEN)
