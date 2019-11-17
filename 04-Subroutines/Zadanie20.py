def potega(x,n):
    if n == 0:
        return 1
    if n > 0:
        return x * potega(x, n-1)
print(potega(2,8))