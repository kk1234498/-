import discord,asyncio
from discord.ext.commands import Bot

bot = discord.Client()



@bot.event
async def on_ready():
    print(f'봇연결이 완료되었습니다. {bot.user}')


@bot.event

async def on_message(message):
    
    if '시발' in message.content:
        await message.channel.send('매너채팅 부탁드립니다.\n\n', delete_after=2.0)
        await asyncio.sleep(0)
        await message.delete()

    elif '씨발' in message.content:
        await message.channel.send('매너채팅 부탁드립니다.\n\n', delete_after=2.0)
        await asyncio.sleep(0)
        await message.delete()
    elif '좆' in message.content:
        await message.channel.send('매너채팅 부탁드립니다.\n\n', delete_after=2.0)
        await asyncio.sleep(0)
        await message.delete()
    elif '니엄' in message.content:
        await message.channel.send('매너채팅 부탁드립니다.\n\n', delete_after=2.0)
        await asyncio.sleep(0)
        await message.delete()
    elif '개새끼' in message.content:
        await message.channel.send('매너채팅 부탁드립니다.\n\n', delete_after=2.0)
        await asyncio.sleep(0)
        await message.delete()
    elif 'ㅅㅣ발' in message.content:
        await message.channel.send('매너채팅 부탁드립니다.\n\n', delete_after=2.0)
        await asyncio.sleep(0)
        await message.delete()

bot.run("")
