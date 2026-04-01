import math

def primesToLimit(lim:int):
    isPrime = [True]*(lim+1);              isPrime[0] = False; isPrime[1] = False
    iterLim = math.isqrt(lim)

    primes = []
    for i in range(2, iterLim + 1):
        if not isPrime[i]: continue

        primes.append(i)
        for j in range(i*2, lim+1, i):
            isPrime[j] = False

    for i in range(iterLim + 1, lim + 1):
        if isPrime[i]: primes.append(i)

    return primes

def primesInRange(rMin:int, rMax:int):
    isPrime = [True]*(rMax+1);              isPrime[0] = False; isPrime[1] = False
    iterLim = math.isqrt(rMax)

    primes = []
    for i in range(2, iterLim + 1):
        if not isPrime[i]: continue

        for j in range(i*2, rMax+1, i):
            isPrime[j] = False

    for i in range(rMin, rMax + 1):
        if isPrime[i]: primes.append(i)

    return primes

while True:
    print(primesInRange(int(input()), int(input())))