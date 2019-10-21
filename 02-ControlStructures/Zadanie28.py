a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
for n in range(1, a+1):
    if(n == 1 or n == a):
        print('*' * (b - 1))
    else:
        print('*'," " * (b - 2),'*')