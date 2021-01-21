import discord
import asyncio

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # create the background task and run it in the background
        self.bg_task = self.loop.create_task(self.my_background_task())

    async def on_ready(self):
        print(f'공지용소스작동이 완료되었습니다. {self.user}')

    async def my_background_task(self):
        await self.wait_until_ready()
        counter = 0
        channel = self.get_channel(752185990239748168) # channel ID goes here
        while not self.is_closed():
            await channel.send('```[채팅방 공지사항]\n'
                            
                               '매너채팅 부탁드립니다.\n\n'
                               '매주듀얼신청은 [!듀얼신청]명령어로 신청가능 취소시 쿼리주세요\n'
                               '매주 경구팀으로 운영되며 참여는 누구나 가능합니다\n\n'
                               '각종 이벤트개최문의 & 채널신설문의는 족장 및 간부에게 쿼리주시면됩니다.'
                               '```')
            await asyncio.sleep(10800) # task runs every 60 seconds


client = MyClient()
client.run("NjY0MTA2Nzk2MTc2Mzc1ODA5.XhSPpg.rmDTSYcHorEoOHn1c9rMjiGm13s")