x = int(input("Podaj wartość x: "))
y = int(input("Podaj wartość y: "))
if(x >= 0 and y>= 0):
    print(f"Punkt P({x},{y}) znajduje się w pierwszej ćwiartce układu współrzędnych")
elif(x < 0 and y >= 0):
    print(f"Punkt P({x},{y}) znajduje się w drugiej ćwiartce układu współrzędnych")
elif(x < 0 and y < 0):
    print(f"Punkt P({x},{y}) znajduje się w trzeciej ćwiartce układu współrzędnych")
else:
    print(f"Punkt P({x},{y}) znajduje się w czwartej ćwiartce układu współrzędnych")