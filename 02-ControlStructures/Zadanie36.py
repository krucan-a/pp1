x = 7
warunek = False
while warunek == False:
    if(x % 6 == 1 and x % 5  == 1 and x % 4 == 1):
        break
    else:
        x += 7
print(x)