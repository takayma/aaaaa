def f(k, n):
    alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
    s = ''
    while k != 0:
        s += alphabet[k % n]
        k //= n
    s = s[::-1]

    return s


if __name__ == '__main__':
    print(f(int(input()), int(input())))
