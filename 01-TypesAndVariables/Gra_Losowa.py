#wygenerowanie losowej liczby z zakresu [1,6]
import random
losowa = random.randint(1,6)
#pytanie gracza o ilość wyrzuconych oczek
strzal = int(input("Podaj, ile oczek kostki wyrzucił komputer: "))
#sprawdzanie booleanem czy gracz wygrał
print(f"Komputer wyrzucił: {losowa}")
print(f"Zgadłeś: {bool(losowa == strzal)}")