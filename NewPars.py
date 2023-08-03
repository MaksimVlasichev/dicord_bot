import requests
import json
import os
def GenStat(nickname, platform):
    source = "https://api.mozambiquehe.re/bridge?auth=be4259adbb8de617ab91a56e6121702e&player=" + nickname + "&platform=" + platform
    infoString = requests.get(str(source))
    jsonInfo = infoString.json()
    globalBlock = jsonInfo['global']
    playerUser = ""
    if globalBlock['rank']['rankName'] == 'Apex Predator':
        playerUser = globalBlock['rank']['rankName'] + " #" + str(globalBlock['rank']['ladderPosPlatform']) 
    else:
        playerUser = globalBlock['rank']['rankName'] 
    ArrayStat = [globalBlock['level'] + globalBlock['levelPrestige']  * 500, playerUser, str(globalBlock['rank']['rankScore']),  globalBlock['rank']['rankImg']]
    return ArrayStat

def GenBRMap():
    source = "https://api.mozambiquehe.re/maprotation?auth=be4259adbb8de617ab91a56e6121702e&version=2"
    infoString = requests.get(str(source))
    jsonInfo = infoString.json()
    BR_block = jsonInfo['battle_royale']
    #Maps = ""
    ArrayMaps = [BR_block['current']['map'], BR_block['current']['asset'], BR_block['next']['map'], str(BR_block['current']['remainingTimer']).split(":")]
    return ArrayMaps

def GenRankedMap():
    source = "https://api.mozambiquehe.re/maprotation?auth=be4259adbb8de617ab91a56e6121702e&version=2"
    infoString = requests.get(str(source))
    jsonInfo = infoString.json()
    RanMap_block = jsonInfo['ranked']
    ArrayRankedMaps = [RanMap_block['current']['map'], RanMap_block['current']['asset'], RanMap_block['next']['map'], str(RanMap_block['current']['remainingTimer']).split(":")]
    return ArrayRankedMaps

def GenltmMap():
    source = "https://api.mozambiquehe.re/maprotation?auth=be4259adbb8de617ab91a56e6121702e&version=2"
    infoString = requests.get(str(source))
    jsonInfo = infoString.json()
    ltmMapMap_block = jsonInfo['ltm']
    ArrayLTMMaps = [ltmMapMap_block['current']['map'], ltmMapMap_block['current']['asset'], ltmMapMap_block['current']['eventName'], ltmMapMap_block['next']['map'], ltmMapMap_block['next']['eventName'] ,str(ltmMapMap_block['current']['remainingTimer']).split(":")]
    return ArrayLTMMaps

def GenReplic():
    source = "https://api.mozambiquehe.re/crafting?auth=be4259adbb8de617ab91a56e6121702e"
    infoString = requests.get(str(source))
    jsonInfo = infoString.json()
    ReplicatorArray = []
    if jsonInfo[0]['bundleType'] == "daily":
        replicatorDaily = os.getcwd() + "\Replicator_bundle\\" + jsonInfo[0]['bundle'] + ".png"
        ReplicatorArray.append(replicatorDaily)
    if jsonInfo[1]['bundleType'] == "weekly":
        replicatorWeekly = os.getcwd() + "\Replicator_bundle\\" + jsonInfo[1]['bundle'] + ".png"
        ReplicatorArray.append(replicatorWeekly)
    return ReplicatorArray

def GenShop():
    source = "https://api.mozambiquehe.re/store?auth=be4259adbb8de617ab91a56e6121702e"
    infoString = requests.get(str(source))
    jsonInfo = infoString.json()
    ShopArray = []
    for i in range(len(jsonInfo)):
        # jsonInfo[i]['pricing'][0]['quantity']
        prices = jsonInfo[i]['pricing']
        ArrPriceForOne = []
        for j in prices:
            ArrPriceForOne.append(j['quantity'])
        ArrayComponent = [jsonInfo[i]['title'], ArrPriceForOne, jsonInfo[i]['asset']]
        ShopArray.append(ArrayComponent)
    return ShopArray