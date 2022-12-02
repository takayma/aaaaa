def f(k, n):
    alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
    s = 0
    i = 1
    for x in k[::-1]:
        if alphabet.index(x) >= n:
            print(f"Значение {x} в числе {k} >= системы счисления {n}")
            break
        s += i * alphabet.index(x)
        i *= n

    return s


if __name__ == '__main__':
    print(f(input(), int(input())))
