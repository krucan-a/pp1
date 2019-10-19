# wczytanie zmiennych
numer = str(input(("Podaj nr rachunku bankowego: ")))
"""
x = 0
while x < len(numer):
    print(numer[x])
    if x % 4 == 1:
        print(" ")
    x += 1
"""
# wypisanie numeru w pożądany sposób
print(f"{numer[0:2]} {numer[2:6]} {numer[6:10]} {numer[10:14]} {numer[14:18]} {numer[18:22]} {numer[22:26]}")