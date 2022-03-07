"""
Litt annerledes enn den jeg leverte inn. Link til problemet: https://open.kattis.com/problems/engineeringenglish
"""

def fjernDuplikater(setning):
    alleOrd = {}

    biter = setning.split()
    for ord in biter:
        if ord.lower() not in alleOrd:
            alleOrd[ord.lower()] = ord
            print(ord, end=" ")
        else:
            print(".", end=" ")

# fjernDuplikater("Engineering will save the world from inefficiency\
#                 Inefficiency is a blight on the world and its \
#                 humanity")

fjernDuplikater("he said that that that that that man used was wrong")
