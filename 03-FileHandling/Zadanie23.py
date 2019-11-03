import re
file = open('land.txt','r')
cyfry = re.findall('\d',file.read())
file.close()
suma = 0
for x in cyfry:
    suma += int(x)
print(suma)