import csv
tab = [['Marek','Zelnik','zelnik@sed.pl'],['Ewa','Maj','maje@wp.pl'],['Piotr','Wyga','wygap@gop.pl']]
with open('Zadanie24.csv', mode='w',newline='') as csv_file:
    fieldnames = ['Imie', 'Nazwisko', 'Email']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for x in range(2):
        writer.writerow({'Imie': tab[x][0], 'Nazwisko': tab[x][1],'Email': tab[x][2]})