import random
import time
import discord
import asyncio

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'Welcome {member.mention} to {guild.name}!'
            await guild.system_channel.send(to_send)
            
    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('$guess'):
            await message.channel.send('Guess a number between 1 and 10.')

            def is_correct(m):
                return m.author == message.author and m.content.isdigit()

            answer = random.randint(1, 10)

            try:
                guess = await self.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send(f'Sorry, you took too long it was {answer}.')

            if int(guess.content) == answer:
                await message.channel.send('You are right!')
            else:
                await message.channel.send(f'Oops. It is actually {answer}.')
        elif message.content.startswith('$hello'):
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

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('token')
