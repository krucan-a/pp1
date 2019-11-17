parity = lambda a: a % 2 == 0
tab = [1,2,3,4,5,6,7,8]
tab_parited = filter(parity, tab)
for x in tab_parited:
    print(x)