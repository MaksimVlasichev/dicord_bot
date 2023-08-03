def GetNameRang(url, predlvl):
    stri = str(url).split("/")[5].replace(".png", "")
    print(type(stri))
    if predlvl == '':
        stris = stri.replace(stri[len(stri)-1], " "+stri[len(stri)-1])
    else:
        stris = stri.replace(stri[len(stri)-1], "")+predlvl
    return stris