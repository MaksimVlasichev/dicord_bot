import os
List = []
filadelfia = os.getcwd()
print(filadelfia)

def SearchList(ListS, author):
    print(ListS)
    for i in range(len(ListS)):
        if str(author) in ListS[i]:
            print('+')
            return i
    return str(author) 

def AccList(author, OriginID): #проверяет есть ли человек с таким дисом в бд
    accs = open(filadelfia + "\\accounts.txt", 'r')
    List = accs.readlines()
    accs.close()
    SeaList = SearchList(List, author)
    if isinstance(SeaList, int):
        i = SeaList
        if str(OriginID) in List[i]:
             return "Такой OriginID уже есть"
        
        if "  " in List[i]:
            List[i] = List[i].replace("  ", " ")
        lenArr = len(List[i].split(" "))
        if lenArr >= 4:
            return "Превышено допустимое значение аккаунтов (Максимум 3)"
        
        List[i] +=(" " + str(OriginID) + "\n") #добавляет в список
        List[i] = List[i].replace("\n", "")
        List[i]+="\n"
        
        
    else:
        List.append(str(author) + " " + str(OriginID) + "\n")
    accs = open(filadelfia + "\\accounts.txt", 'w')
    accs.writelines(List)
    accs.close()
    return "Добавление прошло успешно"  

def DelAcc(author, OriginID):
    accs = open(filadelfia + "\\accounts.txt", 'r')
    List = accs.readlines()
    accs.close()
    SeaList = SearchList(List, author)
    print(SeaList)
    if isinstance(SeaList, int):
        if str(OriginID) in List[SeaList]:
            if str(author) in List[SeaList] and str(OriginID) in List[SeaList]: 
                List[SeaList] = List[SeaList].replace(str(OriginID), "")
                if "  " in List[SeaList]:
                    List[SeaList] = List[SeaList].replace("  ", " ")
                #List[SeaList] = tempList
                accs = open(filadelfia + "\\accounts.txt", 'w')
                accs.writelines(List)
                accs.close()
                return ("Аккаунт " + str(OriginID) + " удален")
        else:
            return ("Аккаунт " + str(OriginID) + " не обнаружен или он не твой")
        
    return "Такого аккаунта в дискорде нет"

def ResetAcc(DisID):
    accs = open(filadelfia + "\\accounts.txt", 'r')
    List = accs.readlines()
    accs.close()
    Num = SearchList(List, DisID)
    List[Num] = List[Num].replace(List[Num], DisID + "\n")
    accs = open(filadelfia + "\\accounts.txt", 'w')
    accs.writelines(List)
    accs.close()
    return ("Игрок очищен")
  

