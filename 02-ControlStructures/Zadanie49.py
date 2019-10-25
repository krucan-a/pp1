nrDniaTygodnia = int(input("Podaj dzień tygodnia pierwszego dnia(0-6): "))
print("| PN | WT | SR | CZ | PT | SB | ND |")
dzien = 1
for x in range(nrDniaTygodnia):
    print("|   ", end = " ")
while dzien < 31:
    if(dzien < 10):
        print(f"|  {dzien}",end = " ")
    else:
        print(f"| {dzien}",end = " ")
    if(nrDniaTygodnia == 6):
        print("|")
        nrDniaTygodnia = 0
    else:
        nrDniaTygodnia += 1
    dzien += 1
if(nrDniaTygodnia!=0):
    while(nrDniaTygodnia<7):
        print("|   ", end = " ")
        nrDniaTygodnia += 1
    print("|",end = "")
        
    
    
