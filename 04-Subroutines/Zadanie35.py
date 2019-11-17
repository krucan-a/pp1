def sum_digit(x):
    if x < 10:
        return x % 10
    else:
        return sum_digit(x // 10) + x % 10
print(sum_digit(88888))