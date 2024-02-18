import random
import time
import discord

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")

    elif message.content.startswith('$coin'):
        num = random.randint(0, 1)
        await message.channel.send('Бросаем монетку...')
        time.sleep(2)
        if num == 0:
            await message.channel.send('Орёл!')
        else:
            await message.channel.send('Решка!')

    elif message.content.startswith('$pass'):
        elements = "+-/*!&$#?=@<>"
        password = ""
        for i in range(10):
            password += random.choice(elements)
        await message.channel.send(password)
        

    else:
        await message.channel.send(message.content)

client.run("token")
