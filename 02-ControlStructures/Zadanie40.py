from random import randrange
jdn = dwa = trzy = cztr = piat = szst = 0
for x in range(100):
    rzut = randrange(1,7)
    if(rzut == 1):
        jdn += 1
    elif(rzut == 2):
        dwa += 1
    elif(rzut == 3):
        trzy += 1
    elif(rzut == 4):
        cztr += 1
    elif(rzut == 5):
        piat += 1
    elif(rzut == 6):
        szst += 1
print(f"Szostka: {szst}\nPiatka: {piat}\nCzworka: {cztr}\nTrójka: {trzy}\nDwójka: {dwa}\nJedynka: {jdn}")