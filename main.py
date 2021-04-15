import discord
import os

bot = discord.Client()


@bot.event
async def on_ready():
    print(f'봇연결이 완료되었습니다. {bot.user}')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
   
  

access_token = os.environ['BOT_TOKEN']
bot.run("access_token")
