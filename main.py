import discord
import asyncio
import datetime
import random
import os

bot = discord.Client()


@bot.event
async def on_ready():
    print(f'봇연결이 완료되었습니다. {bot.user}')




#@bot.event
#async def on_message_edit(before, after):
	#await before.channel.send(before.content + "->" + after.content)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    elif message.content == '!경험치':
        if message.channel.id == 755429961652764794:
            await message.channel.send(
                '{0.author.mention} https://cdn.discordapp.com/attachments/739137911735189635/812829704398700584/8d61033d72b6fe2475cf8847a0e786c5.jpg'.format(
                    message))  # 명령어 쓴사람 태그후 메시지 표시
        else:
            await message.channel.send('```해당 명령어는 봇채널에서만 사용이 가능합니다.```'.format(message), delete_after=3.0)
            await message.delete()

    elif message.content == '!기무1':
        await message.channel.send(
            '{0.author.mention} https://discordapp.com/channels/689001345898119170/739137911735189635/739138087162216539'.format(
                message))  # 명령어 쓴사람 태그후 메시지 표시
    elif message.content == '!기무2':
        await message.channel.send(
            '{0.author.mention} https://discordapp.com/channels/689001345898119170/739137911735189635/739144917963636736'.format(
                message))  # 명령어 쓴사람 태그후 메시지 표시
    elif message.content == '!기무3':
        await message.channel.send(
            '{0.author.mention} https://discordapp.com/channels/689001345898119170/739137911735189635/739144936485552260'.format(
                message))  # 명령어 쓴사람 태그후 메시지 표시
    elif message.content == '!기무4':
        await message.channel.send(
            '{0.author.mention} https://discordapp.com/channels/689001345898119170/739137911735189635/739144951774052422'.format(
                message))  # 명령어 쓴사람 태그후 메시지 표시
    elif message.content == '!기무5':
        await message.channel.send(
            '{0.author.mention} https://discordapp.com/channels/689001345898119170/739137911735189635/739144962079195148'.format(
                message))  # 명령어 쓴사람 태그후 메시지 표시
    elif message.content == '!테로노돈':
        await message.channel.send(
            '{0.author.mention} https://discordapp.com/channels/689001345898119170/739137911735189635/739145587382943815'.format(
                message))  # 명령어 쓴사람 태그후 메시지 표시
    elif message.content == '!메피노':
        await message.channel.send(
            '{0.author.mention} https://discordapp.com/channels/689001345898119170/739137911735189635/739145977474318367'.format(
                message))  # 명령어 쓴사람 태그후 메시지 표시
    elif message.content == '!흑룡':
        await message.channel.send(
            '{0.author.mention} https://discordapp.com/channels/689001345898119170/739137911735189635/739146048962035804'.format(
                message))  # 명령어 쓴사람 태그후 메시지 표시
    elif message.content == '!헤티아':
        await message.channel.send(
            '{0.author.mention} https://discordapp.com/channels/689001345898119170/739137911735189635/739146081371160646'.format(
                message))  # 명령어 쓴사람 태그후 메시지 표시
    elif message.content == '!활티아':
        await message.channel.send(
            '{0.author.mention} https://discordapp.com/channels/689001345898119170/739137911735189635/739146081371160646'.format(
                message))  # 명령어 쓴사람 태그후 메시지 표시
    elif message.content == '!암티아':
        await message.channel.send(
            '{0.author.mention} https://discordapp.com/channels/689001345898119170/739137911735189635/739146117861605466'.format(
                message))  # 명령어 쓴사람 태그후 메시지 표시
    elif message.content == '!암흑헤티아':
        await message.channel.send(
            '{0.author.mention} https://discordapp.com/channels/689001345898119170/739137911735189635/739146117861605466'.format(
                message))  # 명령어 쓴사람 태그후 메시지 표시
    elif message.content == '!헤깃방':
        await message.channel.send(
            '{0.author.mention} https://discordapp.com/channels/689001345898119170/739137911735189635/739146145393279101'.format(
                message))  # 명령어 쓴사람 태그후 메시지 표시
    elif message.content == '!보물방':
        await message.channel.send(
            '{0.author.mention} https://discordapp.com/channels/689001345898119170/739137911735189635/739146145393279101'.format(
                message))  # 명령어 쓴사람 태그후 메시지 표시
    elif message.content == '!마을레이드':
        await message.channel.send(
            '{0.author.mention} https://discord.com/channels/689001345898119170/739137911735189635/741085328835739749'.format(
                message))  # 명령어 쓴사람 태그후 메시지 표시
    elif message.content == '!타임레이드':
        await message.channel.send(
            '{0.author.mention} https://discordapp.com/channels/689001345898119170/739137911735189635/741085390949318736'.format(
                message))  # 명령어 쓴사람 태그후 메시지 표시
    elif message.content == '!칠흑':
        await message.channel.send(
            '{0.author.mention} https://discordapp.com/channels/689001345898119170/739137911735189635/741085390949318736'.format(
                message))  # 명령어 쓴사람 태그후 메시지 표시
    elif message.content == '!칠흑의정령':
        await message.channel.send(
            '{0.author.mention} https://discordapp.com/channels/689001345898119170/739137911735189635/741085390949318736'.format(
                message))  # 명령어 쓴사람 태그후 메시지 표시
    elif message.content == '!필드레이드':
        await message.channel.send(
            '{0.author.mention} https://discordapp.com/channels/689001345898119170/739137911735189635/741085439263506584'.format(
                message))  # 명령어 쓴사람 태그후 메시지 표시
    elif message.content == '!10층':
        await message.channel.send(
            '{0.author.mention} https://discord.com/channels/689001345898119170/739137911735189635/792404840860352542'.format(
                message))  # 명령어 쓴사람 태그후 메시지 표시
    elif message.content == '!20층':
        await message.channel.send(
            '{0.author.mention} https://discord.com/channels/689001345898119170/739137911735189635/792404860548808714'.format(
                message))
    elif message.content == '!30층':
        await message.channel.send(
            '{0.author.mention} https://discord.com/channels/689001345898119170/739137911735189635/792404877954908160'.format(
                message))

    elif message.content == '!H코스':
        await message.channel.send(
            '{0.author.mention} https://discord.com/channels/689001345898119170/739137911735189635/752165883291500585'.format(
                message))
    elif message.content == '!강화':
        await message.channel.send(
            '{0.author.mention} https://cdn.discordapp.com/attachments/739137911735189635/796358968079286293/12.PNG'.format(
                message))
    elif message.content == '!합성':
        await message.channel.send(
            '{0.author.mention}\n[클릭후 보세요] https://cdn.discordapp.com/attachments/739137911735189635/815374449746378812/7f8715d6e52c26e9.png'.format(
                message))
    elif message.content == '!진화':
        await message.channel.send(
            '{0.author.mention} https://cdn.discordapp.com/attachments/739137911735189635/820219411855179776/5d7f6b950c3ab0ae.PNG'.format(
                message))
    elif message.content == '!환생':
        await message.channel.send(
            '{0.author.mention} https://cdn.discordapp.com/attachments/739137911735189635/820219411855179776/5d7f6b950c3ab0ae.PNG'.format(
                message))

    elif message.content == '!수룡':
        await message.channel.send('{0.author.mention} ```준비중```')  # 명령어 쓴사람 태그후 메시지 표시



    elif message.content == '!갠듀':
        await message.channel.send('@everyone ```갠듀타임!\n'
                                   '듀얼채널에서 입장가능 [개인듀얼포인트로 경구구매가능]\n'
                                   '갠듀입장후 동61 , 남61 부족원 모이는장소!```')  # 명령어 쓴사람 태그후 메시지 표시

    elif message.content == "!듀얼신청":
        channel = 749288380327526441
        msg = "<@{}>님이 듀얼신청하였습니다.".format(message.author.id)
        await bot.get_channel(int(channel)).send(msg)
        await message.channel.send('```정규듀얼 신청이 완료되었습니다.```')
        return None
    elif message.content == "!정보":
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="봇명령어", value="!타이머\n", inline=False)
        await message.channel.send(embed=embed)

    elif message.content == "!정보 환가라":
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="닉네임", value="환가라", inline=False)
        embed.add_field(name="역할", value="순캐", inline=False)
        await message.channel.send(embed=embed)

    elif message.content == "!정보 어필":
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="닉네임", value="어필", inline=False)
        embed.add_field(name="역할", value="완캐", inline=False)
        await message.channel.send(embed=embed)

    elif message.content == "!정보 Lara★":
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="닉네임", value="Lara★", inline=False)
        embed.add_field(name="역할", value="완캐", inline=False)
        await message.channel.send(embed=embed)

    elif message.content == "!정보 썸데이":
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="닉네임", value="썸데이 / 물안개 / 물이슬", inline=False)
        embed.add_field(name="역할", value="품번마스터 / 부두술사", inline=False)
        await message.channel.send(embed=embed)
    elif message.content == "!추첨":
        await message.delete()
        await message.channel.send('```첫번째 숫자```')
        await message.channel.send(random.randint(0, 9))
        await asyncio.sleep(5)
        await message.channel.send('```두번째 숫자```')
        await message.channel.send(random.randint(0, 9))
        await asyncio.sleep(5)
        await message.channel.send('```세번째 숫자```')
        await message.channel.send(random.randint(0, 9))

    elif message.content == "!타이머":
        await message.channel.send('```초단위 설정가능\n'
                                   '예제[20초설정시] - !타이머 20```')
    elif message.content.startswith("!타이머"):
        ch = int(message.content.split(" ")[1])
        await message.channel.send("설정하신 시간이 지나면 알려드릴게요!", delete_after=5.0)
        await asyncio.sleep(ch)
        await message.channel.send(
            '{0.author.mention} 시간지났어요!'.format(
                message))

access_token = os.environ["BOT_TOKEN"]
bot.run("access_token")
