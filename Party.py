import disnake
import os
import asyncio

def CreateParty(author: disnake.ApplicationCommandInteraction, players_count, your_rank_or_mode, description_party):

    # print(inter.author.voice.channel.create_invite())
    # await inter.response.send_message(await inter.author.voice.channel.create_invite())
    ArrButt = [disnake.ui.Button(label="", style=disnake.ButtonStyle.green, emoji="🇲", custom_id="mainplus"),
                  disnake.ui.Button(label="", style=disnake.ButtonStyle.green, emoji="🇹", custom_id="tw1plus"),
                  disnake.ui.Button(label="", style=disnake.ButtonStyle.green, emoji="🇹", custom_id="tw2plus"),
                  disnake.ui.Button(label="Войс", style=disnake.ButtonStyle.blurple, emoji= "🔗", custom_id="link"),
                  [disnake.ui.Button(label="2️⃣", style=disnake.ButtonStyle.red, custom_id="del2pl"),
                  disnake.ui.Button(label="3️⃣", style=disnake.ButtonStyle.red, custom_id="del3pl"),
                  disnake.ui.Button(label="❌", style=disnake.ButtonStyle.red, custom_id="delparty")],
                # [disnake.ui.Button(label="🔗", style=disnake.ButtonStyle.link, url=author.author.voice.channel.create_invite())
                   ]
    if players_count == 2:
        ArrButt[3].pop(1)
    Ranks = str(your_rank_or_mode).replace("apex-", "").capitalize()
    embed = disnake.Embed(title=description_party, color=0x0091ff)
    rang_ur = None   
    ArrayPic = ["https://cdn.discordapp.com/attachments/453509048080400394/1123607401535393964/Platinum.png", 
                "https://cdn.discordapp.com/attachments/453509048080400394/1123607400524562432/Silver.png",
                "https://cdn.discordapp.com/attachments/453509048080400394/1123607399941554236/Bronze.png",
                "https://cdn.discordapp.com/attachments/453509048080400394/1123607399492747334/Diamond.png",
                "https://cdn.discordapp.com/attachments/453509048080400394/1123607399031390208/Public.png",
                "https://cdn.discordapp.com/attachments/453509048080400394/1123607398586777650/Master.png",
                "https://cdn.discordapp.com/attachments/453509048080400394/1123607397987012718/Gold.png"]
    for i in range(len(ArrayPic)):
        if Ranks in ArrayPic[i]:
            rang_ur = ArrayPic[i]
            break
    embed.set_thumbnail(url = rang_ur)
    # embed.set_thumbnail(file=disnake.File(f"D:\\BOTIK\\mashBot\\mashBot\\proj\\bot\\Ranks\\{Ranks}.png"))
    embed.add_field(name="", value="1. 👑 " + author.author.mention, inline=False)
    i=1
    for i in range(players_count - 1):
        embed.add_field(name="", value=str(i+2) + ". ", inline=False)   
    return [embed, ArrButt]
# 2️⃣3️⃣🐱‍👤✅✔➕🔵