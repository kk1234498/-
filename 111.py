import discord, asyncio

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bg_task = self.loop.create_task(self.my_background_task())

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('공지용봇')


    async def my_background_task(self):
        await self.wait_until_ready()
        counter = 0
        channel = self.get_channel(691643060127400030)  # channel ID goes here
        while not self.is_closed():

            await channel.send('```[백화난만 채팅공지사항]\n'
                               '매너있는 채팅부탁드립니다.\n\n'
                               '봇사용은 봇채널에서 이용해주시기 바랍니다.\n\n'
                               '해당 공지사항은 한시간에 한번씩 출력됩니다.\n\n'
                               '거래파기 & 혐사 & 비매너에 주의해주세요.```', delete_after=60.0)

            await asyncio.sleep(3600) # ??초마다 메시지전송


client = MyClient()
@client.event

async def on_message(message):
        if message.author == client.user:
            return
        if message.content == ("!갠듀"):
            await message.channel.send('@everyone\n '
                                       '```개인듀얼시간입니다.\n'
                                       '개인듀얼은 참여만해도 개인듀얼포인트 3포인트 지급\n'
                                       '부족원 모이는장소 : 동61 , 남61\n'
                                       '개인듀얼 입장방법 : 듀얼채널 - 사람들 우르르가는곳```')
        elif message.content.startswith("!만월"):
            msg = await message.channel.send('바보', delete_after=2.0)
            await asyncio.sleep(2)
            await msg.delete()
            await message.channel.send('아이고! 놀려버렸네! 이를어쩌지!!!', delete_after=2.0)
            await asyncio.sleep(2)
            await message.delete()
        elif message.content.startswith("!유진"):
                await message.channel.send('날개없는 천사', delete_after=2.0)
                await asyncio.sleep(2)
                await message.delete()
        elif message.content.startswith("!연재"):
            msg =  await message.channel.send('그놈의 셀지개 지겹지 않습니까? 휴먼', delete_after=2.0)
            await asyncio.sleep(2)
            await msg.delete()
            await message.channel.send('죽는것또한 지겹지 않습니까? 휴먼', delete_after=2.0)
            await asyncio.sleep(2)
            await message.delete()
        elif message.content.startswith("!문별"):
            await message.channel.send('별이 빛나는 밤', delete_after=2.0)
            await asyncio.sleep(2)
            await message.delete()
        elif message.content.startswith("!가라"):
            await message.channel.send('가라가라 펫잡으러가라', delete_after=2.0)
            await asyncio.sleep(2)
            await message.delete()
        elif message.content.startswith("!소다"):
            await message.channel.send('터프 물-개', delete_after=2.0)
            await asyncio.sleep(2)
            await message.delete()
        elif message.content.startswith("!용복치"):
            await message.channel.send('우리들의 족장님', delete_after=2.0)
            await asyncio.sleep(2)
            await message.delete()
        elif message.content.startswith("!썸데이"):
            await message.channel.send('주작 ㅊㅋㅊㅋ', delete_after=2.0)
            await asyncio.sleep(2)
            await message.channel.send('백룡 ㅊㅋㅊㅋ', delete_after=2.0)
            await asyncio.sleep(2)
            await message.channel.send('노득의 기운이!!', delete_after=2.0)
            await asyncio.sleep(2)
            await message.delete()
        elif message.content.startswith("!다미"):
            await message.channel.send('아니에오!!! 덜렁이에오!!!', delete_after=2.0)
            await asyncio.sleep(2)
            await message.delete()
        elif message.content.startswith("물-개"):
            await message.channel.send('사조직을 쳐냅시다!!', delete_after=2.0)
            await asyncio.sleep(2)
            await message.delete()
        elif message.content.startswith("!뀨잇"):
            await message.channel.send('내 꿈은 DJ', delete_after=2.0)
            await asyncio.sleep(2)
            await message.delete()
        elif message.content.startswith("!헥사쿤"):
            await message.channel.send('섹시한 사람', delete_after=2.0)
            await asyncio.sleep(2)
            await message.delete()
        elif message.content.startswith("삽니다"):
            await message.channel.send('```[안내]\n'
                                       '장사는 가족장터를 이용해주세요\n'
                                       '해당글은 10초뒤 삭제됩니다.```', delete_after=10.0)
            await asyncio.sleep(0)
            await message.delete()
        elif message.content.startswith("살게요"):
            await message.channel.send('```[안내]\n'
                                       '장사는 가족장터를 이용해주세요\n'
                                       '해당글은 10초뒤 삭제됩니다.```', delete_after=10.0)
            await asyncio.sleep(0)
            await message.delete()
        elif message.content.startswith("살게여"):
            await message.channel.send('```[안내]\n'
                                       '장사는 가족장터를 이용해주세요\n'
                                       '해당글은 10초뒤 삭제됩니다.```', delete_after=10.0)
            await asyncio.sleep(0)
            await message.delete()
        elif message.content.startswith("사요"):
            await message.channel.send('```[안내]\n'
                                       '장사는 가족장터를 이용해주세요\n'
                                       '해당글은 10초뒤 삭제됩니다.```', delete_after=10.0)
            await asyncio.sleep(0)
            await message.delete()
        elif message.content.startswith("사여"):
            await message.channel.send('```[안내]\n'
                                       '장사는 가족장터를 이용해주세요\n'
                                       '해당글은 10초뒤 삭제됩니다.```', delete_after=10.0)
            await asyncio.sleep(0)
            await message.delete()
        elif message.content.startswith("팝니다"):
            await message.channel.send('```[안내]\n'
                                       '장사는 가족장터를 이용해주세요\n'
                                       '해당글은 10초뒤 삭제됩니다.```', delete_after=10.0)
            await asyncio.sleep(0)
            await message.delete()
        elif message.content.startswith("팔게요"):
            await message.channel.send('```[안내]\n'
                                       '장사는 가족장터를 이용해주세요\n'
                                       '해당글은 10초뒤 삭제됩니다.```', delete_after=10.0)
            await asyncio.sleep(0)
            await message.delete()
        elif message.content.startswith("팔게여"):
            await message.channel.send('```[안내]\n'
                                       '장사는 가족장터를 이용해주세요\n'
                                       '해당글은 10초뒤 삭제됩니다.```', delete_after=10.0)
            await asyncio.sleep(0)
            await message.delete()
        elif message.content.startswith("팔아요"):
            await message.channel.send('```[안내]\n'
                                       '장사는 가족장터를 이용해주세요\n'
                                       '해당글은 10초뒤 삭제됩니다.```', delete_after=10.0)
            await asyncio.sleep(0)
            await message.delete()
        elif message.content.startswith("팔아여"):
            await message.channel.send('```[안내]\n'
                                       '장사는 가족장터를 이용해주세요\n'
                                       '해당글은 10초뒤 삭제됩니다.```', delete_after=10.0)
            await asyncio.sleep(0)
            await message.delete()
        elif message.content.startswith("[판매]"):
            await message.channel.send('```[안내]\n'
                                       '장사는 가족장터를 이용해주세요\n'
                                       '해당글은 10초뒤 삭제됩니다.```', delete_after=10.0)
            await asyncio.sleep(0)
            await message.delete()
        elif message.content.startswith("[구매]"):
            await message.channel.send('```[안내]\n'
                                       '장사는 가족장터를 이용해주세요\n'
                                       '해당글은 10초뒤 삭제됩니다.```', delete_after=10.0)
            await asyncio.sleep(0)
            await message.delete()
client.run("NjY0MTA2Nzk2MTc2Mzc1ODA5.XqGk-w.4Y86-h18uHg_JzBXBcFgIdkvZzQ")