from accList import SearchList, filadelfia
import os
from pars import Getinfo
import disnake
from disnake.ext import commands
from msilib.schema import Component

def Info(author):
    accs = open(filadelfia + "\\accounts.txt", 'r')
    List = accs.readlines()
    accs.close()
    i = SearchList(List, author)
    Player = List[i]
    DisID = Player.split(" ")[0]
    lenArr = Player.split(" ")
    lenArr.remove(DisID)
    if '\n' in lenArr:
        lenArr.remove('\n')
    return lenArr


