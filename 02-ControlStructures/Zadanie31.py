uczelnia = input("Podaj ciąg znaków: ")
x = 0
while x < len(uczelnia):
    if x != len(uczelnia) - 1:
        print(uczelnia[x], end = " ")
        x += 1
    else:
        print(uczelnia[x])
        x += 1
    