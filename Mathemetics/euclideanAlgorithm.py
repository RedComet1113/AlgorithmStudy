def gcd(a:int, b:int):
    if a == 0 and b == 0:
        return 0
    
    while b != 0:
        r = a%b
        a = b
        b = r

    return a

while True:
    a, b = map(int, input().split())
    print(gcd(a, b))