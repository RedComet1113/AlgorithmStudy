import math

def factorization(n:int, toString:bool=False):
    if n < 1: raise ValueError

    if n == 1:
        if toString: return "1"
        return [[1, 1]]

    sqrt_n = math.isqrt(n)

    facs = []
    for i in range(2, sqrt_n+1):
        cnt = 0
        while n%i == 0:
            n //= i; cnt += 1

        if cnt: facs.append([i, cnt])

    if n != 1: facs.append([n, 1])

    if toString:
        res = None
        if facs[0][1] == 1:
            res = str(facs[0][0])
        else:
            res = str("{}^{}".format(facs[0][0],facs[0][1]))
        for i in facs[1:]:
            if i[1] == 1:
                res += " * {}".format(i[0])
            else:
                res += " * {}^{}".format(i[0], i[1])
        return res
    return facs

while True:
    print(factorization(int(input()), True))