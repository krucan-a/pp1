import csv
with open('employees.csv', newline='') as f:
    tab = []
    line_count = 0
    reader = csv.reader(f)
    for row in reader:
        if line_count == 0:
            print(f"#",end = " ")
        print(row[1],row[0],row[2],row[3],sep = "\t\t\t")
        print(line_count,end = " ")
        line_count += 1
#tab[0],tab[1] = tab[1], tab[0]
'''
for x in range(len(tab)):
    tab[x][0],tab[x][1] = tab[x][1],tab[x][0]
counter = 0
for x in tab:
    for y in x:
        print(y,end = " ")
    print()
'''