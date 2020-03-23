import discord
import random
import os
client = discord.Client()

@client.event


async def on_ready():
    print(client.user.id)
    print("봇가동이 완료되었습니다.")

    game = discord.Game("!명령어 로 명령어확인가능")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def my_background_task():
        await client.wait_until_ready()
        channel = discord.Object(id='685441685844525097')
        while not client.is_closed:
            await client.send_message(channel, "hi")
            await asyncio.sleep(5) 


async def on_message(message):
    if  message.content == ("!명령어"):
        embed = discord.Embed(title="명령어모음집", description="!아이템이름 (레이드템만가능 아이템풀네임입력)\n!듀얼신청\n\n!주사위\n!가위바위보\n\n!홈피 / !돈페트 / !레이드 / "
                                                          "!마을레이드\n!흑룡 / !헤티아 / !창티아 / !활티아 / !보물방활 / !보물방창\n! / !기무2 / !기무3 / !수룡 / "
                                                          "!칠흑 / !지옥문\n!공식듀얼 / !개인듀얼 / !허환작 / !독뎀\n!환포퀘 / !강화 / !경험치테이블 / !합성재료 / !합성토템 / !페트푸드\n"
                                                          "!환포계산기 / !압물",
                              color=0xFF0000)
        await message.channel.send(embed=embed)






    elif message.content == ("!주사위"):
        randomNum = random.randrange(1, 7)  # 1~6까지 랜덤수
        print(randomNum)
        if randomNum == 1:
            await message.channel.send(message.channel, embed=discord.Embed(description=':one:'))
        if randomNum == 2:
            await message.channel.send(message.channel, embed=discord.Embed(description=':two:'))
        if randomNum == 3:
            await message.channel.send(message.channel, embed=discord.Embed(description=':three:'))
        if randomNum == 4:
            await message.channel.send(message.channel, embed=discord.Embed(description=':four:'))
        if randomNum == 5:
            await message.channel.send(message.channel, embed=discord.Embed(description=':five:'))
        if randomNum == 6:
            await message.channel.send(message.channel, embed=discord.Embed(description= ':six: '))
    elif message.content == ("!가위바위보"):
        randomNum = random.randrange(1, 7)  # 1~6까지 랜덤수
        print(randomNum)
        if randomNum == 1:
            await message.channel.send(message.channel, embed=discord.Embed(description=':hand_splayed::skin-tone-2:'))
        if randomNum == 2:
            await message.channel.send(message.channel, embed=discord.Embed(description=':v:'))
        if randomNum == 3:
            await message.channel.send(message.channel, embed=discord.Embed(description=':fist:'))
        if randomNum == 4:
            await message.channel.send(message.channel, embed=discord.Embed(description=':hand_splayed::skin-tone-2:'))
        if randomNum == 5:
            await message.channel.send(message.channel, embed=discord.Embed(description=':v:'))
        if randomNum == 6:
            await message.channel.send(message.channel, embed=discord.Embed(description=':fist:'))


    elif message.content == ("!홈피"):
        await message.channel.send("https://fresh01.net/main")

    elif message.content.startswith("물이슬"):
        await message.channel.send("나의 세상 나의 빛 아이즈원")
    elif message.content == ("!골드볼라"):
        await message.channel.send("```회긔펫을 잡기위해 필요하다\n추가정보 작성중```")


    elif message.content == ("!합성토템"):
        await message.channel.send("```합성 토템 정보\n\n"
                                   "합성 토템 1 : 전투 종료 HP 30 회복\n"
                                   "합성 토템 2 : 전투 종료 HP 40 회복\n"
                                   "합성 토템 3 : 전투 종료 HP 50 회복 + 기습 방지\n\n"
                                   "합성 토템 만드는법\n\n"
                                   "합성 토템 1 : [가죽 9] + [뼈 9] + [석상 1]\n"
                                   "합성 토템 2 : [가죽 9] + [뼈 9] + [석상 2]\n"
                                   "합성 토템 3 : [가죽 9] + [뼈 9] + [석상 3]\n\n"
                                   "합성소재 판매지\n"
                                   "정령의 마을[동80 남22]에 위치한 편의점\n"
                                   "석상3 소재는 소재보따리에서 랜덤으로만 획득 가능\n\n"
                                   "가공 추천 페트\n"
                                   "무기류 - 케이비\n"
                                   "방어구 - 북이 / 돌북이\n"
                                   "악세사리 - 골드부비```")

    elif message.content == ("!돈페트"):
            await message.channel.send("```돈페트 정보 \n최상급 페트 - 1등급\n상급페트 - 2등급\n초보자 두리 육성 퀘스트 - 우리스타(상급)\n루니/베르가 포획 퀘스트 "
                                       "- 쿠보(상급), 노보(상급)\n채석장의 비밀 - 모나시프(상급), 라나프(상급), 프이토(상급)\n카난 이벤트 - 휴보(상급)\n퀴즈 "
                                       "마스터 - 골드부비(상급), 얼룩부이비(상급)\n마쥬의 우편배달 - 차이혼(상급), 파라프(상급)\n밤미를 갖고싶어 - 알테로스("
                                       "상급)\n환생 이벤트 - 환생얼룩우리(최상급), 투이(상급), 골로스(최상급)\n다섯가지의 관문(6환생) - 파르체(최상급), "
                                       "슈발리(최상급), 지발리(최상급), 샤르체(최상급)\n복권 페트 - 크루거상급), 프리토스(상급), 실버우리(상급), 노르노르(상급), "
                                       "베라라(상급), 베르마루(상급), 헤르마루(상급)\n개인듀얼 페트병 - 황금복덩이(상급)\n이벤트 페트 - 복우리(상급), "
                                       "로라미우스(상급), 고로(상급)\n페트 자판기(아이템 자판기) - 라이혼(최상급), 타이혼(최상급)\n140보상페트 - 다크울프 (상급), "
                                       "막쿠마(상급), 디사크(상급), 문울프(상급)```")

    elif message.content == ("!레이드"):
        await message.channel.send("```레이드는 일주일에 계정마다 20(15회기본 5회 구입)회 진행 가능하며, 매주 일요일 0시에 초기화됩니다.\n"
                                   "레이드 클리어시에 보스마다 전리품을 각 플레이어에게 지급해줍니다. 여기서 기본으로 1 레이드포인트가 뜨고, 레어템은 각 전리품마다 낮은 확률로 뜰수가 "
                                   "있습니다.\n\n레이드의 종류\n[마을 레이드]\n[얼음성 레이드]\n[기계무덤 레이드]\n[용 소탕 레이드]\n[칠흑의 정령 레이드]\n[지옥문 레이드] ```")
        #완료
    elif message.content == ("!마을레이드"):
        await message.channel.send("```각 마을별로 존재하는 레이드 하루1회가능 00시 초기화\n\n"
                                   "샴기르마을 : 동76,남77 NPC동상지킴이에서 입장\n"
                                   "마리너스 마을 : 동62,남120 NPC감염된 액체에서 입장\n"
                                   "쟈쟈 마을 : 동99,남63 우물안 동6,남10 NPC도적기리에서 입장\n"
                                   "카루타나 마을 : 카루타나 목장 앞 쟈루(동328, 남650) 부근에서 전투시 일정 확률로 문울프가 등장합니다. 문울프를 처치시완료\n\n레이드중 가장쉽다.```")
        #완료
    elif message.content == ("!수룡"):
        await message.channel.send("```※ 본문은 완캐 위주로 설명이 되어있으며, 파티 마다 요구 스펙이 다를 수 있습니다.\n\n"
                                   "보상 : [수룡의 비늘] [수룡의 발톱] [수룡의 가죽]\n\n"
                                   "수룡 준비물 - 쟈쟈 촌장댁에서 피리(물)구매 ["
                                   "팀원 중 1인만 구매]\n보상 교환처 - 쟈쟈마을 용의 전사\n수롱 레이드(水) - 주 1회\n레이드 인원 : 완케4명 / 순캐 1명\n\n"
                                   "레이드 스팩\n"
                                   "속성 : [수속성]\n"
                                   "순캐 : [체력] ???이상 / [탑순] 300이상 / [주술1] 은혜의정령 Lv.6 / [주술2] 오로라의 정령\n"
                                   "완캐 : [체력] ???이상 / [활탑공] 380이상\n페트 : [수속성]Lv.120이상\n\n"
                                   "공략방법\n[리더] 스펙에따라 2~4마리 죽을때까지 가드\n[활캐] 메갈로돈 AI순서대로 공격\n[순캐] 첫턴 상대몹에 오로라 /  두번째턴 수우대\n[페트] 수우대걸릴때까지 충견 이후 배진\n\n"
                                   "플레이중 혼란에걸리면 반드시 로그아웃후 재입장하셔야합니다.```")
        #완료
    elif message.content == ("!흑룡"):
        await message.channel.send("```※ 본문은 완캐 위주로 설명이 되어있으며, 파티 마다 요구 스펙이 다를 수 있습니다.\n\n"
                                   "사전 필수 퀘스트 : 얼음의 균열 퀘스트\n\n"
                                   "보상 : [바르의 바람] [흑룡의 발톱] [어린흑룡 펫병] [흑기린 펫병]\n\n"
                                   "흑룡 레이드(水) : [레이드횟수 15회 공유]\n"
                                   "레이드 인원 : [완캐4명 / 순캐1명]\n\n"
                                   "레이드 스팩\n"
                                   "속성 : [수속성]"
                                   "리더 : [찍완이 가장높은사람]\n"
                                   "완캐 : [체력] 최소600이상 [탑활공] 380이상 / 6강활 / 네메목 있으면 장착\n"
                                   "순캐 : [체력] 최소600이상 [탑순] 300이상 [주술1] 은혜의정령 Lv.6 [주술2] 수속성 우대\n"
                                   "페트 : [수속성] Lv.120이상\n\n" 
                                   "AI\n흑룡(보스) 지2풍8 - [리더 우선 공격]\n흑기린(잡몹) 수1화9 - [플레이어 우선 공격][완력 높은 플레이어 공격]\n\n"
                                   "공략\n[리더] - 스팩에따라 앞줄죽을때까지 가드 이후 공격\n"
                                   "[활캐] - 1번흑기린부터 공격\n"
                                   "[순캐] - 첫턴 수우대 / 힐반복"
                                   "[페트] - 배수의 진 1번흑기린부터\n\n"
                                   "흑룡은 가장나중에 공격합니다.```")
        #완료
    elif message.content == ("!헤티아"):
        await message.channel.send("```!창티아 & !활티아를 이용해주세요.```")

    elif message.content == ("!창티아"):
        await message.channel.send("```※ 본문은 완캐 위주로 설명이 되어있으며, 파티 마다 요구 스펙이 다를 수 있습니다.\n\n"
                                   "사전 필수 퀘스트 : 얼음의 균열 퀘스트\n\n"
                                   "보상 : [이라의 불꽃] [적색 큐브] [삼위일체의 구슬] [어린백룡 펫병]\n\n"
                                   "레이드 인원 : [완캐4명 / 순캐1명]\n\n"
                                   "레이드 스팩\n"
                                   "속성 : [화속성]\n"
                                   "리더 : [체력이 가장 높은사람]\n"
                                   "완캐 : [체력] 최소 700이상 [탑공] 460이상\n"
                                   "순캐 : [체력] 최소 700이상 [탑순] 400이상 [주술1] 은혜의 정령Lv.6\n"
                                   "페트 : [화속성] Lv.130이상 바우트\n\n"
                                   "AI\n"
                                   "헤티아(보스) 수10 - [리더우선공격]\n"
                                   "언딘 수2화8 - [플레이어 우선 공격] [스피드 높은 플레이어 공격]\n"
                                   "흑룡 지2풍8 - [리더 우선 공격]\n\n"
                                   "공략방법 [리더제외 완캐는 미리 무지개 걸 대상 결정]\n"
                                   "첫턴\n리더완캐 : 가드 / 페트 배진2 앞줄 흑룡 두번쨰\n"
                                   "완캐 : 언딘2마리와 헤티아 무지개 / 페트 충견 옆페트공격\n"
                                   "순캐 : 화우대 / 힐 반복 / 페트 충견 옆페트공격\n\n"
                                   "잡는순서\n"
                                   "앞줄 AI순서 흑룡부터 순서대로 처치후 언딘 -> 헤티아 / 페트 일공```")
        #완료
    elif message.content == ("!활티아"): #완료
        await message.channel.send("```※ 본문은 완캐 위주로 설명이 되어있으며, 파티 마다 요구 스펙이 다를 수 있으니 출발전 확인하시기 바랍니다.\n\n"
                                   "사전 필수 퀘스트 : 얼음의 균열 퀘스트\n\n"
                                   "보상 : [이라의 불꽃] [적색 큐브] [삼위일체의 구슬] [어린백룡 펫병]\n\n"
                                   "레이드 인원 : [완캐4명 / 순캐1명]\n\n"
                                   "레이드 스팩\n"
                                   "속성 : [화속성]\n"
                                   "리더 : [체력이 가장 높은사람]\n"
                                   "완캐 : [체력] 최소 700 ↑ [노탑활공] 500 ↑ / 6강활 / 네메목 있으면 장착\n"
                                   "순캐 : [체력] 최소 700 ↑ [탑순] 400 ↑ [주술1] 은혜의 정령Lv.6\n"
                                   "페트 : [화속성] Lv.130 ↑ 저순x\n\n"
                                   "AI\n"
                                   "헤티아(보스) 수10 - [리더우선공격]\n"
                                   "언딘 수2화8 - [플레이어 우선 공격] [스피드 높은 플레이어 공격]\n"
                                   "흑룡 지2풍8 - [리더 우선 공격]\n\n"
                                   "공략방법 [리더제외 완캐는 미리 무지개 걸 대상 결정]\n"
                                   "첫턴\n리더완캐 : 가드 / 페트 배진2 앞줄 흑룡 두번쨰\n"
                                   "완캐 : 언딘2마리와 헤티아 무지개 / 페트 충견 옆페트공격\n"
                                   "순캐 : 화우대 / 힐 반복 / 페트 배진2\n\n"
                                   "잡는순서\n"
                                   "활은 AI순서대로 공격 / 페트 배진2 윗언딘먼저 그다음 아랫언딘```")
    elif message.content == ("!보물방활"):
        await message.channel.send("```※ 본문은 완캐 위주로 설명이 되어있으며, 파티 마다 요구 스펙이 다를 수 있으니 출발전 확인하시기 바랍니다.\n\n"
                                   "*보물방[활팟] - 화속성\n"
"완캐 4명, 순캐 1명\n"
"완캐: 탑활공 500 ↑ 체력 700 ↑\n"
"순캐: 탑순 400 ↑ 체력 700 ↑\n\n"
"<플레이정보>\n"
"전원탑승\n\n"
"[리더]\n"
"체력이 제일 높은 완캐\n\n"

"[순캐릭터 템셋팅]\n"
"흑룡의 발톱, 화우대\n\n"

"[완캐릭터 템셋팅]\n"
"무지개, 전체회복아이템 [스테이크등], 활 + 6 ↑\n\n"

"[페트]\n"
"순성 높은 화8이상 [Lv.140 ↑]\n\n"

"[공략]\n"
"완캐 - 백룡-청룡-주작-헤티아-풍백-현무 순서 공격\n"
"순캐 - 우대, 힐반복\n\n"

"첫턴\n"
"[완캐3명] 헤티아, 주작 청룡 무지개\n"
                                   "[완캐1명] 전체힐 / 페트 충견 옆페트\n"
"[순캐] 우대 / 페트 충견 옆페트\n\n"

"첫턴 이후\n"
"[완캐] - 백룡-청룡-주작-헤티아-풍백-현무 순서 / 페트 배진\n"
"[순캐] - 우대, 힐반복 / 페트 배진 @우대안끊어지도록 주의```")
    elif message.content == ("!보물방창"):
        await message.channel.send("```솔직히 활팟이 더좋은거같음 굳이 적어야해요?```")
    elif message.content == ("!기무1"):
        await message.channel.send("```※ 본문은 완캐 위주로 설명이 되어있으며, 파티 마다 요구 스펙이 다를 수 있습니다.(활팟기준)\n\n"
                                   "사전 필수 퀘스트 : 기계 무덤 탐색\n\n"
                                   "보상 : [골로스의 심장] [영혼의 서약] [어린 레드드래곤의 영혼]\n\n"
                                   "레이드 인원 : [완캐3명 / 순캐2명 (중순 / 고순)]\n\n"
                                   "레이드 스팩\n"
                                   "리더 : [정보수집중]\n"
                                   "완캐 : [체력] 최소 650 ↑ [탑활공] 430 ↑ / 6강활 / 네메목 있으면 장착\n"
                                   "중순 : [체력] 최소 650 ↑ [탑순] 260 [주술1] 은혜의정령 Lv.6 [주술2] 수속성 우대\n"
                                   "고순 : [체력] 최소 650 ↑ [탑순] 390  ↑ [주술1] 은혜의정령 Lv.6 [주술2] 수속성 우대\n"
                                   "페트 : [수속성] Lv.130 ↑\n\n"
                                   "AI\n"
                                   "원숭이(드리오쿠스) : [화우대 사용]\n\n"
                                   "공략방법\n"
                                   "완캐 : 원숭이(드리오쿠스) 뒷줄 역AI순으로 공격\n"
                                   "중순 : 원숭이(드리오쿠스) 죽기전까지 수우대사용\n"
                                   "고순 : 첫턴 수우대 이후 힐 반복\n"
                                   "페트 : 원숭이(드리오쿠스) 뒷줄 역AI순으로 배수의진2 \n"
                                   "이후 흑귀 -> 골로스순 처치```")
    elif message.content == ("!기무2"):
        await message.channel.send("```※ 본문은 완캐 위주로 설명이 되어있으며, 파티 마다 요구 스펙이 다를 수 있으니 출발전 확인하시기 바랍니다.\n\n"
                                   "사전 필수 퀘스트 : 기계 무덤 탐색\n"
                                   "보상 : [기계 파편] [적색 큐브] [어린 주작의 영혼]\n"
                                   "레이드 인원 : [완캐 3명 / 중순 1명 / 고순 1명]\n\n"
                                   "레이드 스팩\n"
                                   "완캐 : [체력] 750 ↑ [노탑활공] 520 ↑ [탑창공] 510 ↑ [주술1] 무지개의 정령\n"
                                   "중순 : [체력] 750 ↑ [탑순] 120 [주술1] 水속성 우대\n"
                                   "고순 : [체력] 750 ↑ [탑순] 400 ↑ [주술1] Lv.6 은혜의정령 [주술2] 오로라의 정령\n"
                                   "페트 : [수속성] Lv.130 ↑\n\n"
                                   "공략방법 [첫턴]\n"
                                   "탑창완캐1 : [위 닉스 - 무지개사용]\n"
                                   "탑창완캐2 : [아래 닉스 - 무지개사용]\n"
                                   "탑창완캐3 : [스테이크 - 팀 전체 체력회복]\n"
                                   "중순 : [水우대 사용]\n"
                                   "고순 : [상대편 - 오로라의 정령]\n"
                                   "페트 : [충견진돗개 - 옆에페트 공격]\n\n"
                                   "공략방법 [두번째턴 & 세번째턴]\n"
                                   "탑창완캐들 : [위 닉스 - 공격]\n"
                                   "고순 페트 : [위 닉스 - 배수의 진2]\n"
                                   "저순 페트 : [위 닉스 - 일반 공격]\n"
                                   "고순 : [은혜의정령 사용] [끝날때까지 동일]\n"
                                   "중순 : [水우대 사용] [끝날때까지 동일]\n\n"
                                   "공략방법 [위 닉스 죽은이후]\n"
                                   "[아래 닉스도 위 닉스 잡을때와 동일하게 플레이]\n\n"
                                   "공략방법 [닉스가 모두 죽은후]\n"
                                   "완캐들 : [로그아웃 이후 노탑활로 바꿔서 빠르게 들어옵니다.]\n"
                                   "그후 뒷줄 원숭이부터 공격```")
    elif message.content == ("!기무3"):
        await message.channel.send("```※ 파티마다 잡는 방법이 다른 경우가 많으니 레이드 시작 전에 어떻게 잡을지 물어보세요.\n\n"
            "사전 필수 퀘스트 : 기계 무덤 탐색\n\n"
            "보상 : [기계파편(暗]] [불꽃장궁] [적색큐브] [암흑골로스의영혼]\n\n"
            "레이드 인원 : [완캐 4명 / 순캐 1명]\n\n"
            "레이드 스팩\n"
            "리더 : [체력] 850 ↑ [찍순 0] 혼란목걸이 필수\n"
            "완캐 : [체력] 850 ↑ [찍순 1이상] [찍완 520 ↑] 지속성 탱펫\n"
            "고순 : [체력] 900 ↑ [탑순460 노탑순480 ↑] [주술1] 은혜의정령Lv.6 [주술2] 지속성우대 / [고급호화생선회 필수]\n"
            "페트 : [지속성] Lv.140이상\n\n"
            "AI\n"
            "암흑의사자(중간) : [마비공격]\n"
            "암흑의사자(양옆) : [낙마술]\n"
            "암흑골로스 : [마비공격] [혼란공격]\n"
            "테르가 : [일격필살] [배수의진]\n"
            "메가쟈그 : [일격필살] [석화공격]\n\n"
            "공략방법\n"
            "리더 탱완캐(찍순0) : 테르가 2마리 남을 때까지 가드 이후 충견 활공격\n"
            "완캐 : AI 순서대로 활공격\n"
            "고순 : 첫턴 지우대 이후 생선회 사용 (기무3은 딜이 쎄서 기타임을 갖지 않습니다)\n"
            "페트 리더 : 1) 오른쪽 골로스 배진 2) 왼쪽 골로스 배진 3) 테르가 2마리 이하 남으면 충견\n"
            "완캐 : 충견진돗개\n"
            "고순 : 1) 오른쪽 골로스 배진 2) 왼쪽 골로스 배진 3) 테르가 배진\n\n"
            "정보제공자 - 참이슬```")

        #완료

    elif message.content == ("!지옥문"):
        await message.channel.send("```사전 필수 퀘스트 : 에레보스 진입 퀘스트\n\n"
                                    "※ 입장에 입장 문서(3만 스톤)가 소모되며, 보상으로 레이드포인트를 지급하지 않습니다.\n\n"
                                    "※ 지옥문1은 진행하지 않으며 지옥문2와 지옥문3만 진행합니다.\n\n"
                                    "보상\n"
                                    "지옥문2 : [암석 1개] [지옥의전리품] [삼수정곤봉] [바이론페트병]\n"
                                    "지옥문3 : [암석 2개] [지옥의반지] [지옥견털옷] [지옥의창] [적색큐브] [헬베로스 페트병]\n\n"
                                    "레이드 인원 : [완캐 4명 / 순캐 1명]\n\n"
                                    "레이드 스팩\n"
                                    "리더 : [체력] 800 ↑ [찍완이 가장 높은 캐릭터] 혼란목걸이 필수\n"
                                    "완캐 : [체력] 800 ↑ [찍완 500이 ↑] 무지개 2명 / 스테이크, 수우대 1명 (찍완 낮은 캐릭)\n"
                                    "고순 : [체력] 800 ↑ [탑순 420] [주술1] 은혜의정령 Lv.6 [주술2] 지속성, 수속성 우대\n"
                                    "페트 : [지속성, 수속성] Lv.130이상\n\n"
                                    "-지옥문2 AI-\n"
                                    "헬 바이론 : [마비공격] [낙마술]\n"
                                    "다크론(앞줄) : [혼란공격] [마비공격]\n"
                                    "다크론(뒷줄) : [맹독공격]\n\n"
                                    "공략방법\n"
                                    "완캐 : AI 순서대로 활공격\n"
                                    "고순 : 첫턴 지우대 이후 힐\n"
                                    "페트 : 앞줄 오른쪽 다크론부터 배수의진\n\n"
                                   "-지옥문3 AI-\n"
                                   "지옥문 수호자(헬베로스) : [마비공격] [낙마술]\n"
                                   "갈푸스 : [혼란공격]\n"
                                   "울푸스, 델푸스 : [혼란공격]\n"
                                   "사이록스, 가이록스, 볼프 :　[낙마술]\n\n"
                                   "공략방법\n"
                                   "1턴\n"
                                   "리더(찍완이 가장 높은 캐릭) : 갈푸스가 죽을 때까지 가드\n"
                                   "완캐 2명 : 델푸스, 울푸스 무지개\n"
                                   "완캐 1명 :　스테이크 사용\n"
                                   "고순 : 수우대\n"
                                   "페트 : 리더, 고순 – 헬베로스 배수의진 / 완캐 3명 – 충견진돗개\n\n"
                                   "2턴\n"
                                   "리더(찍완이 가장 높은 캐릭) : 갈푸스가 죽을 때까지 가드 이후 충견 활공격\n"
                                   "완캐 2명 : 볼프, 가이록스 무지개\n"
                                   "완캐 1명 :　활공격\n"
                                   "고순 : 힐\n"
                                   "페트 : 리더, 고순, 활공격 완캐 – 헬베로스 배수의진 / 무지개 완캐 2명 – 충견진돗개\n\n"
                                   "3턴\n"
                                   "리더(찍완이 가장 높은 캐릭) : 갈푸스가 죽을 때까지 가드 이후 충견 활공격\n"
                                   "완캐 : 활공격\n"
                                   "고순 : 힐\n"
                                   "페트 :　헬베로스 – 갈푸스 – 델푸스 – 울푸스 – 베르푸스 순서대로 제거\n\n"
                                   "4턴\n"
                                   "리더(찍완이 가장 높은 캐릭) : 갈푸스가 죽을 때까지 가드 이후 충견 활공격\n"
                                   "완캐 2명 : 활공격완캐(찍완이 가장 낮은 캐릭) : 고순에게 기력약 먹여주기\n"
                                   "고순 : 힐\n"
                                   "페트 :　헬베로스 – 갈푸스 – 델푸스 – 울푸스 – 베르푸스 순서대로 제거\n\n"
                                   "5턴\n"
                                   "리더(찍완이 가장 높은 캐릭) : 갈푸스가 죽을 때까지 가드 이후 충견 활공격\n"
                                   "완캐 2명 : 활공격완캐(찍완이 가장 낮은 캐릭) : 수우대\n"
                                   "고순 : 힐\n"
                                   "페트 :　헬베로스 – 갈푸스 – 델푸스 – 울푸스 – 베르푸스 순서대로 제거\n"
                                   "이후 1턴부터 반복\n\n"
                                   "※ 파티에 따라 찍완이 가장 낮은 완캐가 기력약, 수우대를 쓰지 않고\n"
                                   "순캐가 은혜의정령 대신 고급 호화 생선회를 경우가 존재합니다.\n\n"
                                   "정보제공자 - 참이슬```")

    elif message.content == ("!칠흑"):
       await message.channel.send("```보상 : [정령의 상자 (속성반지 4가지중 하나)] [보석 상자 (중급 스텟초기화 보석)] [경험치 티켓 (80만 경험치)] [흑귀 페트병] "
                                  "[다크야무 페트병] [가론고르 페트병]\n\n"
                                  "사전 퀘스트 : 기계무덤 탐색 퀘스트, 사대 퀘스트, 조력자의 단서를 찾아서\n\n하루최대 4회가능 00시초기화 클리어기준 1채 2채 한번씩클리어 "
                                  "클리어기준 한시간뒤부터 재도전가능\n\n"
                                  "입장암호 : 잠들어 있는 정령의 방으로\n"
                                  "레이드 스팩\n"
                                  "완캐 : [탑활공] 350이상 / [체력] 최소600이상 / [주술1] : 수속성 우대(순1명일경우 장착)\n"
                                  "순캐 : [탑순] 300이상 / [체력] 최소600이상 / [주술1] 오로라의정령 [주술2]수속성 우대(순2명일경우) [주술3] 은혜의 정령 Lv.6\n\n"
                                  "첫턴\n"
                                  "캐릭 : 오로라 & 수우대사용\n펫 : 충견 & 배수의 진(개인판단)\n\n첫턴이후\n순캐 : 은혜의정령사용, 오로라 & 수우대 턴 확인후 사용\n완캐 : 그냥 활공\n펫 : 배수의 진\n\n클리어이후 "
                                  "빠르게 채널변경```")


    elif message.content == ("!페트푸드"):

        await message.channel.send("```러시안 페트푸드1 [충성2전후 ] : 육포 + 물고기1\n"
                                   " 러시안 페트푸드2 [충성5전후 상승] : 큰고기(고기3) + 물고기2 + 도토리3 + 해초4```")

    elif message.content == ("!압물"):
        await message.channel.send("```아부의 성스러운 물이여 나에게 광채나는 힘을\n\n"
                                   "압물은 아부의동굴 6층에서 얻을수있습니다.\n\n"
                                   "가격 : 100스톤```")

        #완료

    elif message.content == ("!공식듀얼"):
        await message.channel.send("```매주 일요일 7시30분 2채 투기장에서 진행\n\n부족내 듀얼신청은 #듀얼게시판에서 가능\n\n참여 기본보상 : 경험치 구슬 5시간 & "
                                   "전쟁포인트 3```")
    elif message.content == ("!개인듀얼"):
        await message.channel.send("```매일 10시00분 듀얼채널에서 진행\n\n참여 기본보상 : 개인듀얼 포인트 3```")
    elif  message.content == ("!허환작"):
        await message.channel.send("```* 돈을 가장빨리 벌수있는 방법중 하나\n\n노환에서 1환을 반복하는 작업이다.\n\n\n"
                                   "아래 목록은 클리어하면 좋은 퀘스트목록입니다.\n\n"
                                   "성인식 3EP\n"
                                   "카난(휴보) 5EP\n"
                                   "루니 and 베르가(쿠보) 8EP\n"
                                   "채석장(모나시프) 5EP\n"
                                   "밤미를 갖고 싶어(알테로스) 0EP\n"
                                   "퀴즈마스터(모가로스 and 골드부비) 5EP\n"
                                   "오형제 5EP\n"
                                   "우리스케의 비밀 3EP\n"
                                   "페트와 이야기 하고 싶어 3EP\n"
                                   "4대 퀘스트 20EP\n"
                                   "하이하모 입장 10EP\n"
                                   "오랑이(타이거 스피어) 15EP + 명성 350\n"
                                   "조력자의 단서를 찾아서 20EP(4대깨면 워프로 한번에 이동가능)```")
        #완료

    elif message.content == ("!환포계산기"):
        await message.channel.send("https://fresh01.net/tip/23672\n" + "```공식홈페이지 주소입니다.```")
    elif message.content == ("!독뎀"):
        await message.channel.send("```골드볼라펫 포획시 독뎀확인방법(독정령Lv.4기준)\n\n"
                                   "독정령 구입은 후르도마을이나 투기장에서 가능\n\n"
                                   "독능력치 확인방법\n"
                                   "[내구력 1/4 + 공격력 + 방어력 + 순발력] = [능력치]\n\n"
                                   "독데미지\n"
                                   "능력치 35.75 ~ 41 독데미지 2\n\n"
                                   "능력치 41 ~ 45.5 독데미지 3\n\n"
                                   "능력치 45.5이상부터 독데미지 4\n\n"
                                   "출처 : 프레쉬헌터채널```")
        #완료
    elif message.content == ("!환포퀘"):
        await message.channel.send("히로산의 약초 : https://fresh01.net/index.php?mid=quest&category=229&document_srl=450\n"
                                   "친구의 우정 : https://fresh01.net/index.php?mid=quest&category=229&document_srl=480\n"
                                   "야무야무 도끼 전달 : https://fresh01.net/index.php?mid=quest&category=229&document_srl=499\n"
                                   "성인식 : https://fresh01.net/index.php?mid=quest&category=229&document_srl=515\n"
                                   "우리스케의 고백 : https://fresh01.net/index.php?mid=quest&category=229&document_srl=568\n"
                                   "사톤가의 가보 찾기 : https://fresh01.net/index.php?mid=quest&category=229&document_srl=607\n"
                                   "루니 포획 : https://fresh01.net/index.php?mid=quest&category=229&document_srl=638\n"
                                   "베르가 포획 : https://fresh01.net/index.php?mid=quest&category=229&document_srl=652\n"
                                   "자연의 균형 : https://fresh01.net/index.php?mid=quest&category=229&document_srl=18084\n"
                                   "한의 도끼 : https://fresh01.net/index.php?mid=quest&category=229&document_srl=24985\n"
                                   "딸을 찾아주세요 : https://fresh01.net/index.php?mid=quest&category=229&document_srl=24986\n"
                                   "빛의 대륙 하이하모를 찾아서 : https://fresh01.net/index.php?mid=quest&category=229&document_srl=24987\n"
                                   "채굴권 다툼 : https://fresh01.net/index.php?mid=quest&category=229&document_srl=24992\n"
                                   "오형제의 시험 : https://fresh01.net/index.php?mid=quest&category=229&document_srl=24997\n"
                                   "채석장의 비밀 : https://fresh01.net/index.php?mid=quest&category=229&document_srl=25000\n"
                                   "선견의 빛(몽환이벤트) : https://fresh01.net/index.php?mid=quest&category=229&document_srl=25002\n"
                                   "카난 이벤트(황금색 페트) : https://fresh01.net/index.php?mid=quest&category=229&document_srl=25009\n"
                                   "퀴즈마스터 : https://fresh01.net/index.php?mid=quest&category=229&document_srl=25025\n"
                                   "마쥬의 우편배달 : https://fresh01.net/index.php?mid=quest&category=229&document_srl=25030\n"
                                   "4개의 보물 : https://fresh01.net/index.php?mid=quest&category=229&document_srl=25033")
        #완료
    elif message.content == ("!강화"):
        embed = discord.Embed(title="강화정보", description="강화 능력치", color=0xAC58FA)
        embed.set_footer(
            text="+4강 이상의 장비는 강화 실패시 파괴됩니다.\n강화에 필요한 큐브는 이벤트포인트 & 레이드에서 획득이 가능하다.")
        embed.set_image(url="http://121.149.113.201/File/" + message.content + ".PNG")
        await message.channel.send(embed=embed)
        #완료
    elif message.content == ("!경험치테이블"):
        embed = discord.Embed(title="경험치 테이블 정보", description="경험치 테이블", color=0xAC58FA)
        embed.set_footer(
            text="노환 : 경험치 100퍼 추가경험치\n1환 : 경험치 80퍼 추가경험치\n2환 : 60퍼 추가경험치")
        embed.set_image(url="https://fresh01.net/files/attach/images/11875/483/030/57dfdbecdcb20bcfdb6fae622339b5d9.jpg")
        await message.channel.send(embed=embed)

    elif message.content == ("!합성재료"):
        embed = discord.Embed(title="합성 재료 정보", description="합성 재료 정보", color=0xAC58FA)
        embed.set_footer(
            text="* 합성 귀걸이4 의 경우 속성 부여시 해당 속성 소재6 으로 하시는 게 가장 가공 점수와 일치하여 성공률이 높습니다.\n\n"
                 "* 합성 팔찌 4 의 경우 속성 부여시 해당 속성 소재9 로 하시는 게 가장 가공점수와 일치하여 성공률이 높습니다.\n\n"
                 "* 합성 반지 4 의 경우 속성 부여시 해당 속성 소재7 로 하시는 게 가장 가공 점수와 일치하여 성공률이 높습니다.\n\n"
                 "* 가공 추천 페트 : 무기류 - 케이비 / 방어구 - 북이, 돌북이 / 악세사리 - 골드부비")
        embed.set_image(url="https://fresh01.net/files/attach/images/11875/969/034/da68a94bcee8af5b18d40a994aba7e02.jpg")
        await message.channel.send(embed=embed)
    elif message.content == ("!만포"):
        await message.channel.send("```#만포루트는 추천사항이며 꼭따라하지 않으셔도 됩니다.\n\n"
                                   "완캐\n\n"
        "0환 > 1환 - [레벨 : 140 / 체력 : 52 / 완력 : 380 / 순발력 : 5]\n"
        "1환 > 2환 - [레벨 : 140 / 체력 : 41 / 완력 : 438 / 순발력 : 4]\n"
        "2환 > 3환 - [레벨 : 140 / 체력 : 45 / 완력 : 467 / 순발력 : 3]\n"
        "3환 > 4환 - [레벨 : 137 / 체력 : 48 / 완력 : 487 / 순발력 : 3]\n"
        "4환 > 5환 - [레벨 : 140 / 체력 : 68 / 완력 : 507 / 순발력 : 2]\n"
        "[6환이후의 스텟은 자유롭게 찍으셔도 됩니다.]\n\n"
                                   "순캐\n\n"
        "0환 > 1환 - [레벨 : 140 / 체력 : 203 / 건강 & 완력 : 4 / 순발력 : 230]\n"
        "1환 > 2환 - [레벨 : 140 / 체력 : 129 / 건강 & 완력 : 4 / 순발력 : 350]\n"
        "2환 > 3환 - [레벨 : 140 / 체력 : 155 / 건강 & 완력 : 3 / 순발력 : 357]\n"
        "3환 > 4환 - [레벨 : 137 / 체력 : 174 / 건강 & 완력 : 3 / 순발력 : 361]\n"
        "4환 > 5환 - [레벨 : 140 / 체력 : 203 / 건강 & 완력 : 2 / 순발력 : 371]\n"
        "[6환이후의 스텟은 자유롭게 찍으셔도 됩니다.]\n\n"
        "만포\n"
                                   "1환 : 66포\n"
                                   "2환 : 98포\n"
                                   "3환 : 129포\n"
                                   "4환 : 160포\n"
                                   "5환 : 192포\n"
                                   "6환 : 5환포인트 + 체력10포\n\n"
        "어디까지나 참고용이고 상세스텟은 환포계산기를 이용해주세요\n\n"
        "!환포계산기 명령어로 다운가능```")




    elif message.content == ("!듀얼신청"):
        channel = 683681607214825512
        await client.get_channel(int(channel)).send("듀얼신청합니다.\n" + message.author.nick)
        await message.channel.send("```신청이 완료되었습니다.\n\n"
                                   "듀얼날짜 : 매주일요일\n"
                                   "듀얼장소 : 2채 투기장\n"
                                   "듀얼시간 : 7시30분부터\n\n"
                                   "듀얼당일 7시20분까지 미리 모여주셔야합니다.\n\n```")

    elif message.content == ("!천상의팔찌"):
        embed = discord.Embed(title="아이템 정보", description="#천상의 팔찌는 3가지의 종류가있다.\n\n"
                              "천상공팔 / 천상민팔 / 천상방팔 [가격순기제]\n"
                              "천상공팔 : 공 + 15\n"
                              "천상민팔 : 민 + 15\n"
                              "천상방팔 : 방 + 15",color = 0xAC58FA)
        await message.channel.send(embed=embed)
#레이드아이템
    elif message.content == ("!흑룡의발톱"):
        embed = discord.Embed(title="아이템 정보", description="공 + 46\n내구력 + 10\n 크리티컬 확률 + 3%\n은혜의 정령Lv.6\n\n"
                                                          "얼음성레이드 : 흑룡의 전리품 레어 보상\n\n", color=0xAC58FA)
        await message.channel.send(embed=embed)
    elif message.content == ("!삼수정곤봉"):
        embed = discord.Embed(title="아이템 정보", description="공 + 23 ~ 26 [랜덤]\n"
                                                          "순 + 18 ~ 20 [랜덤]\n"
                                                          "크리티컬 + 5% ~ 7% [랜덤]\n"
                                                          "은혜의정령Lv.5\n\n"
                                                          "지옥문 레이드 - 헬바이론의 방 또는 지옥의암석(80개)으로 구매", color=0xAC58FA)
        await message.channel.send(embed=embed)
    elif message.content == ("!지옥의창"):
        embed = discord.Embed(title="아이템 정보", description="공 + 58 ~ 60 [랜덤]\n"
                                                          "순 - 13 ~ 15 [랜덤]\n"
                                                          "내구력 + 5 ~ 10 [랜덤]\n"
                                                          "크리티컬 + 5%\n\n"
                                                          "지옥문 레이드 - 헬베로스의 방 또는 지옥의 암석(100개)으로 구매", color=0xAC58FA)
        await message.channel.send(embed=embed)
    elif message.content == ("!헤티아의빛나는창"):
        embed = discord.Embed(title="아이템 정보", description="공 + 60\n"
                                                          "순 - 12\n"
                                                          "크리티컬 + 7%\n"
                                                          "은혜의정령 Lv.6\n\n"
                                                          "헤티아의 보물의 방에서 5%확률로 드랍", color=0xAC58FA)
        await message.channel.send(embed=embed)
    elif message.content == ("!불꽃장궁"):
        embed = discord.Embed(title="아이템 정보", description="공 + 20 ~ 25 [랜덤]\n"
                                                          "방 - 15\n"
                                                          "[6발 - 6발]\n\n"
                                                          "깊은 지하의 무덤 레이드 - 암흑 골로스 전리품 랜덤 레어 보상", color=0xAC58FA)
        await message.channel.send(embed=embed)
    elif message.content == ("!열공의도끼"):
        embed = discord.Embed(title="아이템 정보", description="공 + 70 ~ 77 [랜덤]\n"
                                                          "방 - 10 ~ 12 [랜덤]\n"
                                                          "민 - 30"
                                                          "크리티컬 + 7%\n\n"
                                                          "하이하모 동106,남574 상인 리버 30RP+10만스톤 구매", color=0xAC58FA)
        await message.channel.send(embed=embed)
    elif message.content == ("!지옥의투구"):
        embed = discord.Embed(title="아이템 정보", description="공 + 1 ~ 5 [랜덤]\n"
                                                          "방 + 15 ~ 18 [랜덤]\n"
                                                          "부활의 정령 Lv.2\n\n"
                                                          "지옥문 레이드 - 헬타우르스의 방 또는 지옥의 암석(60개)으로 구매", color=0xAC58FA)
        await message.channel.send(embed=embed)
    elif message.content == ("!지옥견털옷"):
        embed = discord.Embed(title="아이템 정보", description="방 + 18 ~ 20 [랜덤]\n"
                                                          "순 + 15\n"
                                                          "내 + 5 ~ 10 [랜덤]\n"
                                                          "무지개의 정령\n\n"
                                                          "지옥문 레이드 - 헬베로스의 방 또는 지옥의 암석(100개)으로 구매", color=0xAC58FA)
        await message.channel.send(embed=embed)
    elif message.content == ("!헤티아의머리장식"):
        embed = discord.Embed(title="아이템 정보", description="공 + 5\n"
                                                          "방 + 15\n"
                                                          "무지개의 정령\n\n"
                                                          "헤티아의 보물의 방에서 5%확률로 드랍", color=0xAC58FA)
        await message.channel.send(embed=embed)
    elif message.content == ("!초신성갑옷"):
        embed = discord.Embed(title="아이템 정보", description="공 + 5\n"
                                                          "방 + 40\n"
                                                          "민 - 10\n"
                                                          "윤택의 정령 Lv.5\n\n"
                                                          "헤티아의 보물의 방에서 5%확률로 드랍", color=0xAC58FA)
        await message.channel.send(embed=embed)
    elif message.content == ("!얼음옷"):
        embed = discord.Embed(title="아이템정보", description="얼음 옷", color=0xAC58FA)
        embed.set_footer(text="공 + 5 ~ 7(랜덤)\n방 + 20\n내 + 10 ~ 20(랜덤)\n치유의 정령 Lv.4\n\n하이하모 동106, 남574 상인 리버 30RP+10만스톤 구매")
        embed.set_image(url="http://121.149.113.201/File/레이드아이템/" + message.content + ".png")
        await message.channel.send(embed=embed)
    elif message.content == ("!얼음옷"):
        embed = discord.Embed(title="아이템 정보", description="공 + 5 ~ 7 [랜덤]\n"
                                                          "방 + 20\n"
                                                          "내 + 10 ~ 20 [랜덤]\n"
                                                          "치유의 정령 Lv.4\n\n"
                                                          "하이하모 동106, 남574 상인 리버 30RP+10만스톤 구매", color=0xAC58FA)
        await message.channel.send(embed=embed)
    elif message.content == ("!얼음투구"):
        embed = discord.Embed(title="아이템 정보", description="방 + 15\n"
                                                          "내 + 10 ~ 15 [랜덤]\n\n"
                                                          "하이하모 동106, 남574 상인 리버 30RP+10만스톤 구매", color=0xAC58FA)
        await message.channel.send(embed=embed)
        #레이드장신구
    elif message.content == ("!바르의바람"):
        embed = discord.Embed(title="아이템 정보", description="민 + 3~7 [랜덤]\n"
                                                          "내구력 + 5~20 [랜덤]\n\n"
                                                          "얼음성레이드 : 흑룡의 전리품 레어 보상", color=0xAC58FA)
        await message.channel.send(embed=embed)
    elif message.content == ("!머슬링귀걸이"):
        embed = discord.Embed(title="아이템 정보", description="공 + 1~5 [랜덤]\n"
                                                          "회피율 확률 + 7%\n\n"
                                                          "얼음성레이드 : 메피노 전리품 레어 보상", color=0xAC58FA)
        await message.channel.send(embed=embed)
    elif message.content == ("!번개의반지"):
        embed = discord.Embed(title="아이템 정보", description="민 + 1~5 [랜덤]\n"
                                                          "크리티컬 확률 + 7%\n\n"
                                                          "얼음성레이드 : 테로노돈 전리품 레어 보상", color=0xAC58FA)
        await message.channel.send(embed=embed)
    elif message.content == ("!티아트의대지"):
        embed = discord.Embed(title="아이템 정보", description="방 + 3 ~ 7 [랜덤]\n"
                                                          "내구력 + 5 ~ 20 [랜덤]\n\n"
                                                          "얼음성레이드 : 메피노의 전리품 레어 보상", color=0xAC58FA)
        await message.channel.send(embed=embed)
    elif message.content == ("!기계심장"):
        embed = discord.Embed(title="아이템 정보", description="공 + 2\n"
                                                          "방 + 2\n"
                                                          "순 + 2\n"
                                                          "내구력 + 5\n"
                                                          "하단 2번슬롯에 장착\n\n"
                                                          "하이하모 동106, 남574 상인 리버에게 30RP로 구매", color=0xAC58FA)
        await message.channel.send(embed=embed)
    elif message.content == ("!골로스의심장"):
        embed = discord.Embed(title="아이템 정보", description="공 + 2 ~ 5 [랜덤]\n"
                                                          "방 + 2 ~ 5 [랜덤]\n"
                                                          "순 + 2 ~ 5 [랜덤]\n"
                                                          "내구력 + 5 ~ 10 [랜덤]\n"
                                                          "하단 2번슬롯에 장착\n\n"
                                                          "골로스 전리품", color=0xAC58FA)
        await message.channel.send(embed=embed)
    elif message.content == ("!정령의반지"):
        embed = discord.Embed(title="아이템 정보", description="공 + 2 ~ 3 [랜덤]\n"
                                                          "방 + 2 ~ 3 [랜덤]\n"
                                                          "순 + 2 ~ 3 [랜덤]\n"
                                                          "크리티컬 + 1% ~ 5% [랜덤]\n"
                                                          "반지에 부여된속성 + 2\n\n"
                                                          "칠흑의 정령 레이드 레어 보상", color=0xAC58FA)
        await message.channel.send(embed=embed)
    elif message.content == ("!타우루스의부적"):
        embed = discord.Embed(title="아이템 정보", description="공 + 1 ~ 5 [랜덤]\n"
                                                          "내 + 20\n"
                                                          "고등정화의 정령\n\n"
                                                          "지옥문 레이드 - 헬타우루스의 방 또는 지옥의 암석(60개)으로 구매", color=0xAC58FA)
        await message.channel.send(embed=embed)
    elif message.content == ("!지옥의전리품"):
        embed = discord.Embed(title="아이템 정보", description="공 + 1 ~ 3 [랜덤]\n"
                                                          "방 + 1 ~ 3 [랜덤]\n"
                                                          "순 + 1 ~ 3 [랜덤]\n"
                                                          "내 + 5 ~ 15(랜덤)\n"
                                                          "하단 3번슬롯에 장착\n\n"
                                                          "지옥문 레이드 - 헬바이론의 방 또는 지옥의 암석(80개)으로 구매", color=0xAC58FA)
        await message.channel.send(embed=embed)
    elif message.content == ("!지옥의반지"):
        embed = discord.Embed(title="아이템 정보", description="공 + 2 ~ 7 [랜덤]\n"
                                                          "내 + 15 ~ 20 [랜덤]\n"
                                                          "크리티컬 + 5% ~ 7% [랜덤]\n\n"
                                                          "지옥문 레이드 - 헬베로스의 방 또는 지옥의 암석(100개)으로 구매", color=0xAC58FA)
        await message.channel.send(embed=embed)
    elif message.content == ("!풍신주머니"):
        embed = discord.Embed(title="아이템 정보", description="민 + 5 ~ 8 [랜덤]\n"
                                                          "토템3 효과\n\n"
                                                          "헤티아의 보물의 방에서 2%확률로 드랍", color=0xAC58FA)
        await message.channel.send(embed=embed)
    elif message.content == ("!대지의심장"):
        embed = discord.Embed(title="아이템 정보", description="방 + 5 ~ 8 [랜덤]\n"
                                                          "토템3 효과\n\n"
                                                          "헤티아의 보물의 방에서 2%확률로 드랍", color=0xAC58FA)
        await message.channel.send(embed=embed)
    elif message.content == ("!불사조의정신"):
        embed = discord.Embed(title="아이템 정보", description="공 + 5 ~ 8 [랜덤]\n"
                                                          "토템3 효과\n\n"
                                                          "헤티아의 보물의 방에서 2%확률로 드랍", color=0xAC58FA)
        await message.channel.send(embed=embed)
    elif message.content == ("!삼위일체"):
        embed = discord.Embed(title="아이템 정보", description="공 + 1 ~ 10 [랜덤]\n"
                                                          "방 + 1 ~ 10 [랜덤]\n"
                                                          "순 + 1 ~ 10 [랜덤]\n\n"
                                                          "삼위일체의 구슬 + 토템3 합성\n\n"
                                                          "삼위일체[眞]를 만들기\n"
                                                          "삼위일체 심장 + 삼위일체(改)\n\n"
                                                          "능력치\n"
                                                          "삼위일체(改)능력치 공방순 + 3", color=0xAC58FA)
        await message.channel.send(embed=embed)

        
    elif message.content == ("!이라의불꽃"):
        embed = discord.Embed(title="아이템 정보", description="공 + 3 ~ 7 [랜덤]\n"
                                                          "내 + 5 ~ 20 [랜덤]\n\n"
                                                          "얼음성 레이드 - 헤티아 전리품 레어 보상", color=0xAC58FA)
        await message.channel.send(embed=embed)
    elif message.content == ("!영웅의신물"):
        embed = discord.Embed(title="아이템 정보", description="장착시 5 포인트 랜덤 능력치 부여\n\n"
                                                          "하이하모 (동106, 남574) 상인 리버에게 30RP로 구매\n\n"
                                                          "아이템 능력치는 포인트를 랜덤으로 능력치를 부여하며, 공격력 방어력 순발력 내구력 관통 쉴드 중 랜덤으로 능력치가 설정됩니다.\n"
                                                         "단일 능력치는 최대 5개까지만 부여되며, 내구력은 1포인트당 3의 능력치를 얻습니다.", color=0xAC58FA)
        await message.channel.send(embed=embed)
    elif message.content == ("!영광의신물"):
        embed = discord.Embed(title="아이템 정보", description="장착시 10 포인트 랜덤 능력치 부여\n\n"
                                                          "얼음성 레이드 - 암흑 헤티아의 전리품\n\n"
                              "아이템 능력치는 포인트를 랜덤으로 능력치를 부여하며, 공격력 방어력 순발력 내구력 관통 쉴드 중 랜덤으로 능력치가 설정됩니다.\n"
                              "단일 능력치는 최대 5개까지만 부여되며, 내구력은 1포인트당 3의 능력치를 얻습니다.", color=0xAC58FA)
        await message.channel.send(embed=embed)
        
    elif message.content == ("!지옥의신물"):
        embed = discord.Embed(title="아이템 정보", description="장착시 15 포인트 랜덤 능력치 부여\n\n"
                                                          "얼음성 레이드 - 암흑 헤티아의 전리품\n\n"
                             "아이템 능력치는 포인트를 랜덤으로 능력치를 부여하며, 공격력 방어력 순발력 내구력 관통 쉴드 중 랜덤으로 능력치가 설정됩니다.\n"
                              "단일 능력치는 최대 5개까지만 부여되며, 내구력은 1포인트당 3의 능력치를 얻습니다.", color=0xAC58FA)
        await message.channel.send(embed=embed)
    elif message.content == ("!합성창"):
        embed = discord.Embed(title="아이템 정보", description="공 + 58 ~ 40\n민 - 11 ~ 15\n크리티컬 + 5%\n\n"
                                                          "나무9 + 상아9\n\n"
                             "가공추천페트 : 무기류 - 케이비 / 방어구 - 북이, 돌북이 / 악세사리 - 골드부비\n\n"
                                                          "* 합성소재 판매지\n"
                                                        "- 정령의 마을(동80 남22)에 위치한 편의점\n"
                                                        "- 석상3 소재는 소재보따리에서 랜덤으로만 획득 가능\n", color=0xAC58FA)
        await message.channel.send(embed=embed)
    elif message.content == ("!합성투구"):
        embed = discord.Embed(title="아이템 정보", description="방 + 25 ~ 17\n민 - 5 ~ 7\n\n"
                                                          "가죽9 + 뼈9\n\n"
                                                          "가공추천페트 : 무기류 - 케이비 / 방어구 - 북이, 돌북이 / 악세사리 - 골드부비"
                                                          "* 합성소재 판매지\n"
                                                          "- 정령의 마을(동80 남22)에 위치한 편의점\n"
                                                          "- 석상3 소재는 소재보따리에서 랜덤으로만 획득 가능\n",color=0xAC58FA)
        await message.channel.send(embed=embed)
    elif message.content == ("!합성갑옷"):
        embed = discord.Embed(title="아이템 정보", description="방 + 46 ~ 32\n민 - 10 ~ 14\n\n"
                                                          "가죽9 + 돌9\n\n"
                                                          "가공추천페트 : 무기류 - 케이비 / 방어구 - 북이, 돌북이 / 악세사리 - 골드부비"
                                                          "* 합성소재 판매지\n"
                                                          "- 정령의 마을(동80 남22)에 위치한 편의점\n"
                                                          "- 석상3 소재는 소재보따리에서 랜덤으로만 획득 가능\n", color=0xAC58FA)
        await message.channel.send(embed=embed)
        
        #레이드소모템
    elif message.content == ("!영혼의서약"):
        embed = discord.Embed(title="아이템 정보", description="사용 시 영구적으로 탑승페트의 경험치 획득 5% 상승[최대 1회]\n\n"
                                                          "골로스 전리품 레어 보상", color=0xAC58FA)
        await message.channel.send(embed=embed)

        #큐브
    elif message.content == ("!일반큐브"):
        embed = discord.Embed(title="아이템 정보", description="사용 시 아이템을 강화한다.\n\n"
                              "획득방법\n"
                              "접속 보상상자 또는 샴기르 이벤트NPC를 통해 구매", color=0xAC58FA)
        await message.channel.send(embed=embed)
    elif message.content == ("!장인의큐브"):
        embed = discord.Embed(title="아이템 정보", description="사용 시 아이템을 강화한다. [+5%확률 증가)\n\n"
                              "획득방법\n"
                              "2등복권 보상", color=0xAC58FA)
        await message.channel.send(embed=embed)
    elif message.content == ("!고급큐브"):
        embed = discord.Embed(title="아이템 정보", description="사용 시 아이템을 강화한다. [+10%확률 증가)\n\n"
                              "획득방법\n"
                              "[금빛 보물상자] [은빛 보물상자]에서 랜덤 획득 가능", color=0xAC58FA)
        await message.channel.send(embed=embed)
    elif message.content == ("!청록큐브"):
        embed = discord.Embed(title="아이템 정보", description="사용 시 아이템을 강화한다. [+15%확률 증가)\n\n"
                              "획득방법\n"
                              "[천상의 보물상자]에서 랜덤 획득 가능", color=0xAC58FA)
        await message.channel.send(embed=embed)
    elif message.content == ("!적색큐브"):
        embed = discord.Embed(title="아이템 정보", description="사용 시 아이템을 강화한다. [+20%확률 증가)\n\n"
                              "획득방법\n"
                              "헤티아이상 레이드 보상에서 랜덤 획득 가능", color=0xAC58FA)
        await message.channel.send(embed=embed)


    elif message.content.startswith('!'):
        await message.channel.send("```명령어가 존재하지않습니다.\n!명령어 <-를 입력하여 명령어를 확인해주세요.```")

client.loop.create_task(my_background_task())
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
