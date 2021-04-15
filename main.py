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
   
    elif message.content == '!수룡':
        await message.channel.send('{0.author.mention} ```준비중```')  # 명령어 쓴사람 태그후 메시지 표시
  

access_token = os.environ['BOT_TOKEN']
bot.run("access_token")
