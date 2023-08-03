import asyncio
import disnake
import sys
from disnake.ext import commands
import os, sqlite3
from obr import rand
import pars
from accList import AccList, DelAcc, ResetAcc, SearchList
from typing import Optional
import disnake_paginator
import emoji
import string
from ToDataBase import Info
import datetime
import time 
from enum import Enum
from Party import CreateParty
from NewPars import GenStat, GenBRMap, GenRankedMap, GenltmMap, GenReplic, GenShop
import typing
from rand_legens_and_gun import rand_gun, rand_leg

TOKEN =''

bot = commands.InteractionBot()

PartyCreator = {}

async def UStats(userName, platform):
    try:
        info = GenStat(userName, platform)
    except Exception:
        embed = disnake.Embed(title = "Такой ea ник не найден, возможно вы написали никнейм в стиме, а он не совпадает с ником в ea, либо ошиблись в написании", color=0x0091ff)
        return embed 
    else:
        lvl = info[0]
        rank = info[1]
        LP = info[2]
        RankImg = info[3]
        embed = disnake.Embed(title = "Статистика " + userName + ":", color=0x0091ff)
        embed.set_thumbnail(url=RankImg)
        embed.add_field(name = "Уровень " + str(lvl), value="", inline=False)
        embed.add_field(name = "Ранг: " + rank, value="LP: " + str(LP), inline=False)
        return embed
    
async def ButtStat(message: disnake.ApplicationCommandInteraction):
    PlayerInfo = Info(message.author.id)
    emojiArr = ["🇲", "🇹", "🇹"]
    
    if len(PlayerInfo) < 1:
        await message.reply("У вас нет аккаунтов, вам следует их добавить")
        return False
    for i in range(len(PlayerInfo)):
        PlayerInfo[i] = disnake.ui.Button(label=PlayerInfo[i], style=disnake.ButtonStyle.blurple, emoji=emojiArr[i], custom_id=str(i))
    return PlayerInfo

@bot.event #ивент включения
async def on_ready():
    print("Буп")
    # infoEnt = rand()
    # character = infoEnt.split("\n")[0]
    # url = infoEnt.split("\n")[1]
    # citata = infoEnt.split("\n")[2]
    # print(character, url, citata)
    # embed=disnake.Embed(title ="Напишите команду &help для просмотра списка команд", description = (citata + "\n©"+ character), color=0x0091ff)
    # embed.set_thumbnail(url= url)
    # await bot.get_channel(496234920188968960).send(embed = embed) #в скобочках айди канала
    await bot.change_presence(activity=disnake.Game(name="/help")) #статус бота
    
# @bot.command(pass_context=True)
# @bot.event #приветсвие доработать с цитатами
# async def on_member_join(member):
#     await bot.get_channel(450717218804596771).send(f" Ку {member.mention} приземляется, пришло время стать новым чемпионом игр Апекса:\n")
#     embed=disnake.Embed(title = rand())
#     await bot.get_channel(450717218804596771).send(embed=embed)

@bot.slash_command(description="Помощь") #чтение сообщения
async def help(inter):
    embed=disnake.Embed(title = "Список команд\n ", description = "Список используемых команд\n", color=0x0091ff)
    embed.set_thumbnail(url="https://i.pinimg.com/564x/eb/fc/09/ebfc09c9f0b39af612956cfb734d27e2.jpg")
    embed.add_field(name = "<:radio_button:1036676020545269812> /map_in_{ranked/pubs/ltm}", value ="Посмотреть текущую карту в КБ в рейтинге/пабликах или сменяемых режимах", inline = False)
    embed.add_field(name = "<:radio_button:1036676020545269812> /replicator", value ="Посмотреть что находится в репликаторе", inline = False)
    embed.add_field(name = "<:radio_button:1036676020545269812> /player_stat {OriginID}", value ="Посмотреть статистику аккаунта", inline = False)
    embed.add_field(name = "<:radio_button:1036676020545269812> /create_party", value ="Создает отряд вдвоем или втроем показывает ники игроков для быстрого добавления, если они есть в БД и их рейтинг на выбранных аккаунтов, не показывается кроме создателя", inline = False)
    embed.add_field(name = "<:radio_button:1036676020545269812> /add_acc {OriginID}", value ="Добавить основной/твинк аккаунт вписав айди в Origin (Если вы делаете это в первый раз, то сначала добавляется мейн акк, а только потом 1 и 2 твинк)", inline = False)
    embed.add_field(name = "<:radio_button:1036676020545269812> /del_acc {main/twink} {OriginID}", value ="Удалить основной/твинк аккаунт вписав айди в Origin", inline = False)
    embed.add_field(name = "<:radio_button:1036676020545269812> /reset_all_acc {member}", value ="Удалить все привязанные аккаунты конкретного пользователя через пинг участника", inline = False)
    embed.add_field(name = "<:radio_button:1036676020545269812> /stat_accs", value ="Посмотреть общую статистику аккаунтов (аккаунты должны быть добавлены в БД)", inline = False)
    embed.add_field(name = "<:radio_button:1036676020545269812> /rand_leg_and_guna", value ="Случайный герой и ганы", inline = False)
    embed.add_field(name = "<:radio_button:1036676020545269812> /shop", value ="Посмотреть что продается в магазинах", inline = False)
    await inter.response.send_message(embed=embed, ephemeral=True)

@bot.listen("on_button_click")
async def Ustats_listener(inter: disnake.MessageInteraction):
    UStat = None
    
    await inter.response.defer()
    if inter.component.custom_id not in ["mainplus", "tw1plus", "tw2plus", "link", "del2pl", "del3pl", "delparty"]:
        UStat = await UStats(inter.component.label, platform="PC")
    
    elif inter.component.custom_id in ["mainplus", "tw1plus", "tw2plus", "link", "del2pl", "del3pl", "delparty"]:
        tempembed = inter.message.embeds[0]
        if inter.component.custom_id in ["del2pl", "del3pl", "delparty"] and str(inter.author.id) == tempembed.fields[0].value.split('@')[1].replace(">", ""):
            if inter.component.custom_id == "del2pl":
                if len(tempembed.fields) == 3:
                    tempembed.set_field_at(index=1, name="", value=tempembed.fields[2].value.replace("3.", "2."), inline=False)
                    tempembed.set_field_at(index=2, name="", value="3.", inline=False)
                    UStat = tempembed
                
                else:
                    tempembed.set_field_at(index=1, name="", value="2.", inline=False)
                    UStat = tempembed

            elif inter.component.custom_id == "del3pl":
                tempembed.set_field_at(index=2, name="", value="3.", inline=False)
                UStat = tempembed

            elif inter.component.custom_id == "delparty":
                await inter.edit_original_response(components=[])
                await inter.message.delete()
                return
        
        elif inter.component.custom_id in ["mainplus", "tw1plus", "tw2plus", "link"]:
            global PartyCreator
            mes = ""
            url = ""
            try:
                    url = PartyCreator[inter.message.id].voice.channel.id
            except Exception:
                mes = "создатель не в войсе"
            else:
                mes = await inter.bot.get_channel(url).create_invite()
            for i in range(len(tempembed.fields)):
                
                if len(tempembed.fields[i].value) > 3 and str(inter.author.id) in tempembed.fields[i].value.split(" ")[1]:
                    if inter.component.custom_id == "link":
                        
                        await inter.send(mes, ephemeral=True)
                        break
                    else:
                        break
                elif len(tempembed.fields[i].value) > 3:
                    pass
    
                else:
                    filadelfia = os.getcwd()
                    accs = open(filadelfia + "\\accounts.txt", 'r')
                    List = accs.readlines()
                    accs.close()
                    SeaList = SearchList(List, inter.author.id)
                    
                    plat= "PC"
                    if len(str(SeaList)) > 5:
                        tempembed.set_field_at(index=i, name="", value=tempembed.fields[i].value + f" {inter.author.mention}", inline=False)
                        break
                    
                    elif inter.component.custom_id == "mainplus":
                        if len(List[SeaList].split(" "))>=2:
                            username = List[SeaList].split(" ")[1]
                            
                            tempembed.set_field_at(index=i, name="", value=tempembed.fields[i].value + f" {inter.author.mention} {username}  LP: {GenStat(nickname=username, platform=plat)[2]}", inline=False)
                            break
                    
                    elif inter.component.custom_id == "tw1plus":
                        if len(List[SeaList].split(" "))>=3:
                            username = List[SeaList].split(" ")[2]
                            tempembed.set_field_at(index=i, name="", value=tempembed.fields[i].value + f" {inter.author.mention} {username}  LP: {GenStat(nickname=username, platform=plat)[2]}", inline=False)
                            break
                    
                    elif inter.component.custom_id == "tw2plus":
                        if len(List[SeaList].split(" "))==4:
                            username = List[SeaList].split(" ")[3].replace("\n", "")
                            tempembed.set_field_at(index=i, name="", value=tempembed.fields[i].value + f" {inter.author.mention} {username}  LP:  {GenStat(nickname=username, platform=plat)[2]}", inline=False)
                            break
                    
                    # elif inter.component.custom_id == "link":
                    #     pass
                    
        UStat = tempembed
        
        # print(url)
        

    else:
        return
    await inter.edit_original_message(embed=UStat)
    
@bot.slash_command(description="Cтатистика любого игрока")
async def player_stat(inter: disnake.ApplicationCommandInteraction, originid: str, platform: typing.Literal["PC","PS4", "X1"]):
    OtherStat = await UStats(originid, platform)
    await inter.response.send_message(embed = OtherStat, content = "")

@bot.slash_command(description="Общая статистика аккаунтов (только для ПК)")
async def stat_accs(inter: disnake.ApplicationCommandInteraction):
    arrButt = await ButtStat(inter)
    await inter.response.send_message(components=arrButt, ephemeral=True)

@bot.slash_command(description="Добавить основной/твинк Origin только для ПК")
async def add_acc(inter, originid: str):
    YayOrError = AccList(inter.author.id, originid)
    await inter.response.send_message(YayOrError, ephemeral=True)

@bot.slash_command(description="Удалить свой аккаунт")
async def del_acc(inter, originid: str):
    deleteAcc = DelAcc(inter.author.id, originid)
    await inter.response.send_message(deleteAcc, ephemeral=True)

@bot.slash_command(description="Удалить все аккаунты игрока")
async def reset_all_accs(inter: disnake.ApplicationCommandInteraction, member: disnake.Member):
    if inter.author.guild_permissions.view_audit_log == True:
        ResAcc = ResetAcc(str(member.id))
        await inter.response.send_message(ResAcc, ephemeral=True)
    else: await inter.response.send_message("У вас недостаточно прав, по вопросам обратитесь к модераторам", ephemeral=True)

@bot.slash_command(description="Посмотреть карты в пабликах")
async def map_in_pubs(inter):
    # Zdyn = await inter.response.send_message("https://tenor.com/view/wait-star-wars-watching-looking-staring-gif-10097895")
    MapInPubs = GenBRMap()
    time = datetime.datetime.now() + datetime.timedelta(hours=int(MapInPubs[3][0]), minutes=int(MapInPubs[3][1]), seconds=int(MapInPubs[3][2]))
    countdown = disnake.utils.format_dt(time,style='R')
    embed = disnake.Embed(title="Текущая карта в пабликах: " + MapInPubs[0], color=0x0091ff)
    embed.set_image(url = MapInPubs[1])
    embed.add_field(name="Следующая карта: " + MapInPubs[2], value="", inline = False)
    embed.add_field(name="Сменится: " + countdown, value="", inline=False)
    await inter.response.send_message(embed=embed, content = "")

@bot.slash_command(description="Посмотреть карты в ранкеде")
async def map_in_ranked(inter):
    #Zdyn = await inter.response.send_message("https://tenor.com/view/wait-star-wars-watching-looking-staring-gif-10097895")
    MapInRanked = GenRankedMap()
    time = datetime.datetime.now() + datetime.timedelta(hours=int(MapInRanked[3][0]), minutes=int(MapInRanked[3][1]), seconds=int(MapInRanked[3][2]))
    countdown = disnake.utils.format_dt(time,style='R')
    embed = disnake.Embed(title="Текущая карта в ранкеде: " + MapInRanked[0], color=0x0091ff)
    embed.set_image(url=MapInRanked[1])
    embed.add_field(name="Следующая карта: " + MapInRanked[2], value="", inline = False)
    embed.add_field(name="Сменится: " + countdown, value="", inline=False)
    await inter.response.send_message(embed=embed, content = "")

@bot.slash_command(description="Посмотреть карты в режимах")
async def map_in_ltm(inter):
    #Zdyn = await inter.response.send_message("https://tenor.com/view/wait-star-wars-watching-looking-staring-gif-10097895")
    MapInLTM = GenltmMap()
    time = datetime.datetime.now() + datetime.timedelta(hours=int(MapInLTM[5][0]), minutes=int(MapInLTM[5][1]), seconds=int(MapInLTM[5][2]))
    countdown = disnake.utils.format_dt(time,style='R')
    embed = disnake.Embed(title="Текущая карта в режиме: " + MapInLTM[0], color=0x0091ff)
    embed.set_image(url=MapInLTM[1])
    embed.add_field(name="Название режима: " + MapInLTM[2], value="", inline = False)
    embed.add_field(name="Следующая карта: " + MapInLTM[3], value="", inline = False)
    embed.add_field(name="Следующий режим: " + MapInLTM[4], value="", inline = False)
    embed.add_field(name="Сменится: " + countdown, value="", inline=False)
    await inter.response.send_message(embed=embed, content = "")

@bot.slash_command(description="Ротация репликатора")
async def replicator(inter: disnake.ApplicationCommandInteraction):
    ArrayReplicators = GenReplic()
    embed = disnake.Embed(title="Ежедневный текущий: ", color=0x0091ff)
    embed.set_image(file=disnake.File(ArrayReplicators[0]))
    embed1 = disnake.Embed(title="Еженедельный текущий: ", color=0x0091ff)
    embed1.set_image(file=disnake.File(ArrayReplicators[1]))
    await inter.response.send_message(embeds=[embed, embed1])

@bot.slash_command(description="Магазин")
async def shop(inter: disnake.ApplicationCommandInteraction):
    ArrayShop = GenShop()
    AllEmbeds = []

    for i in ArrayShop:
        print(AllEmbeds)
        embed = disnake.Embed(title=i[0], color=0x0091ff)
        if len(i[1]) == 2:
            embed.add_field(name="Цена: " + str(i[1][0]) + " LT", value="", inline=False)
            embed.add_field(name="Цена: " + str(i[1][1])+ " AC", value="", inline=False)
        else:
            embed.add_field(name="Цена: " + str(i[1][0])+ " AC", value="", inline=False)
        # embed.add_field(name="Цена: " + str(i[1]), value="", inline=False)
        embed.set_image(url=i[2])
        AllEmbeds.append(embed)
        print(i[2])
    paginator = disnake_paginator.ButtonPaginator(title="shop", color=0x0091ff, segments=AllEmbeds, button_style=disnake.ButtonStyle.blurple)
    await paginator.start(inter, ephemeral=True) #sends a message in the channel
	
@bot.slash_command(description="Создать группу")
async def create_party(inter: disnake.ApplicationCommandInteraction, players_count: commands.Range[int, 2, 3], your_rank_or_mode: disnake.Role, description_party: str):
    global PartyCreator
    
    await inter.channel.send(your_rank_or_mode.mention,delete_after=3600)
    PartyIsCreate = CreateParty(inter, players_count, your_rank_or_mode, description_party)
    mess = await inter.channel.send(embed=PartyIsCreate[0], components=PartyIsCreate[1])
    
    PartyCreator[mess.id] = inter.author
    await inter.response.send_message("Секундочку", delete_after=0)

@bot.slash_command(description="Случайный герой и ганы")
async def rand_leg_and_gun(inter: disnake.ApplicationCommandInteraction):
    ArrayGun = rand_gun()
    
        
    embed1gun = disnake.Embed(title="Первый ган: " + ArrayGun[0], color=0x0091ff)
    embed1gun.set_image(url=ArrayGun[1])
    embed2gun = disnake.Embed(title="Второй ган: " + ArrayGun[2], color=0x0091ff)
    embed2gun.set_image(url=ArrayGun[3])
    embed3gun = disnake.Embed(title="Третий ган(Если предыдущие красные или на Баллистике): " + ArrayGun[4], color=0x0091ff)
    embed3gun.set_image(url=ArrayGun[5])
    if type(ArrayGun[6]) == str:
        embed3gun.set_footer(text = ArrayGun[6])
    ArrayLeg = rand_leg()
    embed1leg = disnake.Embed(title="Первый герой: " + ArrayLeg[0], color=0x0091ff)
    embed1leg.set_image(url=ArrayLeg[1])
    embed2leg = disnake.Embed(title="Второй герой: " + ArrayLeg[2], color=0x0091ff)
    embed2leg.set_image(url=ArrayLeg[3])
    embed3leg = disnake.Embed(title="Третий герой(Если предыдущие выбраны): " + ArrayLeg[4], color=0x0091ff)
    embed3leg.set_image(url=ArrayLeg[5])
    await inter.response.send_message(embeds=[embed1leg, embed2leg, embed3leg, embed1gun, embed2gun, embed3gun], ephemeral=True)
                
# @bot.slash_command(description="test")
# async def test(inter: disnake.ApplicationCommandInteraction):
#     global PartyCreator
#     PartyIsCreate = CreateParty(inter, 3, "platinum", "description_party")
#     await inter.response.send_message("tewt", delete_after= 0)
#     mess = await inter.channel.send(embed=PartyIsCreate[0], components=PartyIsCreate[1])
#     PartyCreator[mess.id] = inter.author
#     await inter.response.send_message("Секундочку", delete_after=0)
    
           
bot.run(os.getenv('TOKEN'))
