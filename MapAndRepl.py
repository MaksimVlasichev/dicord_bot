from urllib import response
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

def SearchMap(MapInfoBox):
    NameNowMapInPubs = MapInfoBox.find("h1").text.replace("Battle Royale: ", "")
    Mapimg = str(NameNowMapInPubs).capitalize()
    if " " in NameNowMapInPubs:
        Mapimg = Mapimg.split(" ")[0].capitalize() + "_" + Mapimg.split(" ")[1].capitalize()
    TimerMap = MapInfoBox.find("h2").text
    NextMapInPubs = MapInfoBox.findAll("h5")[1].find_next().text
    return [NameNowMapInPubs, Mapimg, TimerMap, NextMapInPubs]

def PubsMap():
    syte = "https://apexlegendsstatus.com/current-map"
    syteopen = webdriver.Chrome("D:\\BOTIK\\mashBot\\mashBot\\proj\\bot\\chromedriver.exe") #путь до драйвера
    syteopen.get(syte) #открытие неообходимого сайта
    time.sleep(5)
    get_syte_info = syteopen.page_source.encode("utf-8").strip()
    SoupObject = BeautifulSoup(get_syte_info, "html.parser")
    PubMap = SoupObject.findAll("div", class_ = "col-lg-6")[0]
    return SearchMap(MapInfoBox = PubMap)

def RankedMap():
    syte = "https://apexlegendsstatus.com/current-map"
    syteopen = webdriver.Chrome("D:\\BOTIK\\mashBot\\mashBot\\proj\\bot\\chromedriver.exe") #путь до драйвера
    syteopen.get(syte) #открытие неообходимого сайта
    time.sleep(5)
    get_syte_info = syteopen.page_source.encode("utf-8").strip()
    SoupObject = BeautifulSoup(get_syte_info, "html.parser")
    RankedMap = SoupObject.findAll("div", class_ = "col-lg-6")[1]
    return SearchMap(MapInfoBox = RankedMap)

def SearchRepRotation(RepInBox):
    DayliBundleRotation = RepInBox.find("div", class_ = "col-lg-6").find("h5").text.replace("Current - ", "")
    DayliTimerRep = RepInBox.find("p").text.replace("Changes in ", "").replace("hours", ":").replace(" minutes ", "")
    NextBundleRotation = RepInBox.findAll("div", class_ = "col-lg-6")[1].find("h5").text.replace("Next - ", "")
    return [DayliBundleRotation, DayliTimerRep, NextBundleRotation]

def DayliReplicator():
    syte = "https://apexlegendsstatus.com/crafting-rotation"
    syteopen = webdriver.Chrome("D:\\BOTIK\\mashBot\\mashBot\\proj\\bot\\chromedriver.exe")
    syteopen.get(syte)
    time.sleep(5)
    get_syte_info = syteopen.page_source.encode("utf-8").strip()
    SoupObject = BeautifulSoup(get_syte_info, "html.parser")
    RepRotation = SoupObject.findAll("div", class_ = "col-lg-6")[0]
    # SearchRepRotation(RepRotation)
    return SearchRepRotation(RepRotation)
# print(DayliReplicator())





