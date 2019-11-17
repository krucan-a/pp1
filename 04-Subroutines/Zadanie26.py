def podatek(dochod):
    if dochod <= 5000:
        return 0.17 * dochod
    else:
        return (dochod - 5000) * 0.32 + 850
dochod = int(input("Podaj dochód: "))
print(f"Podatek należny: {podatek(dochod)} zł")