def normalize(x):
    integ = int(x)
    if integ != 0:
        sign = integ // abs(integ)
    else:
        sign = 1
    integ = abs(integ)

    part = str(x)
    part = part[part.index('.') + 1:]

    if part == '0':
        return sign * integ

    k0 = 0
    k9 = 0

    for i in range(len(part)):
        if part[i] == '0':
            k0 += 1
            k9 = 0
        elif part[i] == '9':
            k9 += 1
            k0 = 0
        else:
            k0 = 0
            k9 = 0

        if k0 >= 8:
            part = part[:i - k0 + 1]
            break
        elif k9 >= 8:
            part = part[:i - k9 + 1]

            if part == '':
                integ += 1
            else:
                part = part[:-1] + str(int(part[-1]) + 1)

            break

    x = str(integ) + '.' + part
    x = sign * float(x)
    return x
