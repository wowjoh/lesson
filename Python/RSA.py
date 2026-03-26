def gcd(a, b): 
    while a != 0:
        a, b = b% a, a
    return b


p, q = 11, 3
n = p * q
l = n / gcd(p-1, q-1)
