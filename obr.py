import os
import random
def rand():
    file1 = open("words.txt","r" , encoding='utf-8') 
    mnogo_citat = file1.read()
    allData = mnogo_citat.split("$")
    allData.remove(allData[0])
    a = random.randint(0, len(allData)-1)
    dates = allData[a].split("#")
    charak = dates[0]
    print(charak)
    url = dates[1].split("\n")
    if '' in url:
        url.remove('')
    url = random.choice(url)
    return charak + url+ "\n"+ allData[a].split("#")[2].split("\n")[random.randint(0,len(allData[a].split("#")[2].split("\n"))-1)]

