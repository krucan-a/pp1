import math
jezyki = ["Java","Python","JavaScript","C++","C#","Ruby","Perl","PHP","C","Android"]
wartosci = [61, 47, 37, 32, 26, 18, 14, 14, 9, 7]
def rysujWykres(jezyki, wartosci):
    print(jezyki[0],"\t\t",":","#" * 30)
    x = 1
    while x < len(jezyki):
        if(len(jezyki[x])<7):
            print(jezyki[x],"\t\t",":","#" * math.ceil(30 * wartosci[x]/ 61))
        else:
            print(jezyki[x],"\t",":","#" * math.ceil(30 * wartosci[x]/ 61))
        x += 1
rysujWykres(jezyki,wartosci)