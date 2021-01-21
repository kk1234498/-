import discord
import asyncio
import random



bot = discord.Client()


@bot.event
async def on_ready():
    print(f'봇연결이 완료되었습니다. {bot.user}')

@bot.event
async def on_member_join(member):
    await member.guild.get_channel(752185990239748168).send('@everyone\n' + member.mention + '님이 새롭게 가입했습니다. 환영해주세요!\n'
                                                            '새로가입하신분은 공지사항 읽어보시고 역할부여가 된후부터 채팅이 가능합니다.')
    await member.add_roles(bot.get_guild(689001345898119170).get_role(692330007326097418), reason="가입대기자")
    return
@bot.event
async def on_member_remove(member):
    await member.guild.get_channel(752185990239748168).send(member.mention + "님이 부족에서 탈퇴&추방 당하였습니다.")
    return

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    elif message.content == '!경험치':
        if message.channel.id == 755429961652764794:
            await message.channel.send('{0.author.mention} https://fresh01.net/files/attach/images/387452/581/387/60f15f9b1b2e3147de335db134d76969.jpg'.format(message))  # 명령어 쓴사람 태그후 메시지 표시
        else:
            await message.channel.send('```해당 명령어는 봇채널에서만 사용이 가능합니다.```'.format(message), delete_after=3.0)
            await message.delete()

    elif message.content == '!기무1':
        await message.channel.send('{0.author.mention} https://discordapp.com/channels/689001345898119170/739137911735189635/739138087162216539'.format(message))  # 명령어 쓴사람 태그후 메시지 표시
    elif message.content == '!기무2':
        await message.channel.send('{0.author.mention} https://discordapp.com/channels/689001345898119170/739137911735189635/739144917963636736'.format(message))  # 명령어 쓴사람 태그후 메시지 표시
    elif message.content == '!기무3':
        await message.channel.send('{0.author.mention} https://discordapp.com/channels/689001345898119170/739137911735189635/739144936485552260'.format(message))  # 명령어 쓴사람 태그후 메시지 표시
    elif message.content == '!기무4':
        await message.channel.send('{0.author.mention} https://discordapp.com/channels/689001345898119170/739137911735189635/739144951774052422'.format(message))  # 명령어 쓴사람 태그후 메시지 표시
    elif message.content == '!기무5':
        await message.channel.send('{0.author.mention} https://discordapp.com/channels/689001345898119170/739137911735189635/739144962079195148'.format(message))  # 명령어 쓴사람 태그후 메시지 표시
    elif message.content == '!테로노돈':
        await message.channel.send('{0.author.mention} https://discordapp.com/channels/689001345898119170/739137911735189635/739145587382943815'.format(message))  # 명령어 쓴사람 태그후 메시지 표시
    elif message.content == '!메피노':
        await message.channel.send('{0.author.mention} https://discordapp.com/channels/689001345898119170/739137911735189635/739145977474318367'.format(message))  # 명령어 쓴사람 태그후 메시지 표시
    elif message.content == '!흑룡':
        await message.channel.send('{0.author.mention} https://discordapp.com/channels/689001345898119170/739137911735189635/739146048962035804'.format(message))  # 명령어 쓴사람 태그후 메시지 표시
    elif message.content == '!헤티아':
        await message.channel.send('{0.author.mention} https://discordapp.com/channels/689001345898119170/739137911735189635/739146081371160646'.format(message))  # 명령어 쓴사람 태그후 메시지 표시
    elif message.content == '!활티아':
        await message.channel.send('{0.author.mention} https://discordapp.com/channels/689001345898119170/739137911735189635/739146081371160646'.format(message))  # 명령어 쓴사람 태그후 메시지 표시
    elif message.content == '!암티아':
        await message.channel.send('{0.author.mention} https://discordapp.com/channels/689001345898119170/739137911735189635/739146117861605466'.format(message))  # 명령어 쓴사람 태그후 메시지 표시
    elif message.content == '!암흑헤티아':
        await message.channel.send('{0.author.mention} https://discordapp.com/channels/689001345898119170/739137911735189635/739146117861605466'.format(message))  # 명령어 쓴사람 태그후 메시지 표시
    elif message.content == '!헤깃방':
        await message.channel.send('{0.author.mention} https://discordapp.com/channels/689001345898119170/739137911735189635/739146145393279101'.format(message))  # 명령어 쓴사람 태그후 메시지 표시
    elif message.content == '!보물방':
        await message.channel.send('{0.author.mention} https://discordapp.com/channels/689001345898119170/739137911735189635/739146145393279101'.format(message))  # 명령어 쓴사람 태그후 메시지 표시
    elif message.content == '!마을레이드':
        await message.channel.send('{0.author.mention} https://discord.com/channels/689001345898119170/739137911735189635/741085328835739749'.format(message))  # 명령어 쓴사람 태그후 메시지 표시
    elif message.content == '!타임레이드':
        await message.channel.send('{0.author.mention} https://discordapp.com/channels/689001345898119170/739137911735189635/741085390949318736'.format(message))  # 명령어 쓴사람 태그후 메시지 표시
    elif message.content == '!칠흑':
        await message.channel.send('{0.author.mention} https://discordapp.com/channels/689001345898119170/739137911735189635/741085390949318736'.format(message))  # 명령어 쓴사람 태그후 메시지 표시
    elif message.content == '!칠흑의정령':
        await message.channel.send('{0.author.mention} https://discordapp.com/channels/689001345898119170/739137911735189635/741085390949318736'.format(message))  # 명령어 쓴사람 태그후 메시지 표시
    elif message.content == '!필드레이드':
        await message.channel.send('{0.author.mention} https://discordapp.com/channels/689001345898119170/739137911735189635/741085439263506584'.format(message))  # 명령어 쓴사람 태그후 메시지 표시
    elif message.content == '!10층':
        await message.channel.send('{0.author.mention} https://discord.com/channels/689001345898119170/739137911735189635/792404840860352542'.format(message))  # 명령어 쓴사람 태그후 메시지 표시
    elif message.content == '!20층':
        await message.channel.send('{0.author.mention} https://discord.com/channels/689001345898119170/739137911735189635/792404860548808714'.format(message))
    elif message.content == '!30층':
        await message.channel.send('{0.author.mention} https://discord.com/channels/689001345898119170/739137911735189635/792404877954908160'.format(message))

    elif message.content == '!H코스':
        await message.channel.send('{0.author.mention} https://discord.com/channels/689001345898119170/739137911735189635/752165883291500585'.format(message))
    elif message.content == '!강화':
        await message.channel.send('{0.author.mention} https://cdn.discordapp.com/attachments/739137911735189635/796358968079286293/12.PNG'.format(message))

    elif message.content == '!친선듀얼신청':
        channel = 796312206190968844
        msg = "<@{}>님 친선듀얼 신청하였습니다.".format(message.author.id)
        await bot.get_channel(int(channel)).send(msg)
        await message.channel.send('```친선듀얼 신청이 완료되었습니다.\n'
                                   '취소시 족장에게 쿼리주세요```')
        return None

    elif message.content == '!갠듀':
        await message.channel.send('@everyone ```갠듀타임!\n'
                                   '듀얼채널에서 입장가능 [개인듀얼포인트로 경구구매가능]\n'
                                   '갠듀입장후 동61 , 남61 부족원 모이는장소!```')  # 명령어 쓴사람 태그후 메시지 표시
    elif message.content == '!수룡':
        await message.channel.send('{0.author.mention} ```준비중```')  # 명령어 쓴사람 태그후 메시지 표시

    elif message.content == "!듀얼신청":
                channel = 749288380327526441
                msg = "<@{}>님이 듀얼신청하였습니다.".format(message.author.id)
                await bot.get_channel(int(channel)).send(msg)
                await message.channel.send('```정규듀얼 신청이 완료되었습니다.```')
                return None
    elif message.content == "!이벤듀":
                channel = 749288380327526441
                msg = "<@{}>님이 이벤트듀얼신청하였습니다.".format(message.author.id)
                await bot.get_channel(int(channel)).send(msg)
                await message.channel.send('```이벤트듀얼 신청이 완료되었습니다.```')
                return None




    elif message.content == ('!가위바위보'):
        rsp = ["가위", "바위", "보"]
        embed = discord.Embed(title="가위바위보", description="가위바위보를 합니다 3초내로 (가위/바위/보)를 써주세요!", color=0x00aaaa)
        channel = message.channel

        msg1 = await message.channel.send(embed=embed)

        def check(m):
            return m.author == message.author and m.channel == channel
        try:
            msg2 = await bot.wait_for('message', timeout=3.0, check=check)

        except asyncio.TimeoutError:
            await msg1.delete()
            embed = discord.Embed(title="가위바위보", description="앗 3초가 지났네요...!", color=0x00aaaa)
            await message.channel.send(embed=embed)
            return
        else:
            await msg1.delete()
            bot_rsp = str(random.choice(rsp))
            user_rsp = str(msg2.content)
            answer = ""
            if bot_rsp == user_rsp:
                answer = "저는 " + bot_rsp + "을 냈고, 당신은 " + user_rsp + "을 내셨내요.\n\n" + "아~ 정말 아깝게 비겻네요!"
            elif (bot_rsp == "가위" and user_rsp == "바위") or (bot_rsp == "보" and user_rsp == "가위") or (
                bot_rsp == "바위" and user_rsp == "보"):
                answer = "저는 " + bot_rsp + "을 냈고, 당신은 " + user_rsp + "을 내셨내요.\n\n" + "분하지만 패배를 인정하죠"
            elif (bot_rsp == "바위" and user_rsp == "가위") or (bot_rsp == "가위" and user_rsp == "보") or (
                bot_rsp == "보" and user_rsp == "바위"):
                answer = "저는 " + bot_rsp + "을 냈고, 당신은 " + user_rsp + "을 내셨내요.\n\n" + "좀더 연습하고오세요~^^"
            else:
                embed = discord.Embed(title="가위바위보", description="앗, 가위, 바위, 보 중에서만 내셔야죠... 다시!!", color=0x00aaaa)
                await message.channel.send(embed=embed)
                return
            embed = discord.Embed(title="가위바위보", description=answer, color=0x00aaaa)
            await message.channel.send(embed=embed)
            return

access_token = os.environ["BOT_TOKEN"]
bot.run("access_token")
