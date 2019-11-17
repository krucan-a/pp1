def rndnmbr():
    import random
    return random.randrange(1,50)
def tab_evenness(tab):
    even = 0
    odd = 0
    for x in tab:
        if(x % 2 == 0):
            even += 1
        else:
            odd += 1
    percent = round(even / len(tab) * 100, 2)
    print(f"Liczby parzyste: {percent}%")
    print(f"Liczby nieparzyste: {100 - percent}%")
tab = [rndnmbr()]
for x in range(999):
    tab.append(rndnmbr())
tab_evenness(tab)

