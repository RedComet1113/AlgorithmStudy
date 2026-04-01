import math

def factors(n:int):
    if n < 1: raise ValueError

    sqrt_n = math.isqrt(n) # int(math.sqrt(n))와 동치
    
    # facs = []
    # for d in range(1, sqrt_n+1):
    #     if n%d == 0: facs.append(d)
    facs = [d for d in range(1, sqrt_n + 1) if n%d == 0]
    
    if facs[-1]*facs[-1] == n:
        for d in range(len(facs)-2, -1, -1):
            facs.append(n//facs[d])
        return facs
    for d in range(len(facs)-1, -1, -1):
        facs.append(n//facs[d])
    return facs

while True:
    print(factors(int(input())))