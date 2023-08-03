from urllib import response
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
import time
def Getinfo(login):
    sourse = "https://apexlegendsstatus.com/profile/PC/"+login
    driver = webdriver.Chrome("D:\\BOTIK\\mashBot\\mashBot\\proj\\bot\\chromedriver.exe")
    driver.maximize_window()
    driver.get(sourse)
    time.sleep(5)
    content = driver.page_source.encode('utf-8').strip()
    # getting the contents of the website and parsing them
    webpage = requests.get(sourse)
    soup = BeautifulSoup(content, 'html.parser')
    s = soup.find("main", class_ = "wrapper")
    ss = s.find("div", {"data-role":"profile-content"})
    sss = ss.find("div", {"class":"container-fluid"}).find("div", class_ = "row").find("div", class_ ="col-md-3").find("div", class_ = "legpickrate").find("div", class_ = "row").findAll(class_ = "col-xs-4")
    lvl = "Уровень " + str(sss[0].find(class_ = "levelNumber").text) + "\n" + str(sss[0].find(class_ = "center-element general-stats general-stats-rank").text).replace("Prestige", "Престиж ")
    print('\n----------\n')
    brck = sss[1].findAll(class_ = "center-element general-stats general-stats-rank")
    predlvl =''
    if len(brck) ==  3:
        predlvl = brck[2].text
    brlvl = "КБ "+ str(brck[1].text)
    #print(sss[1].find(class_ = "center-element general-stats general-stats-rank").text + sss[1].findNext(class_ = "center-element general-stats general-stats-rank").text)
    print('\n----------\n')
    areck = sss[2].findAll(class_ = "center-element general-stats general-stats-rank")
    predAreaLvl = ''
    if len(areck) ==  3:
        predAreaLvl = areck[2].text
    arealvl = "Арены " + str(areck[1].text)
    #print(sss[2].find(class_ = "center-element general-stats general-stats-rank").text + sss[2].findNext(class_ = "center-element general-stats general-stats-rank").text)

    img = sss[1].find('img')
    imgn = str(img['src'])
    imgar = sss[2].find('img')
    imgnArens = str(imgar['src'])
    #image = sss.find
        
    return [lvl, brlvl, imgn, predlvl]
    # print(title)
    # sameinfo = soup.findAll("div", calss = "container-fluid")
    # print(sameinfo)
# print(Getinfo("kymsksksks"))