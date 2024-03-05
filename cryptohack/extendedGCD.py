def extend_gcd(p, q):
    if p == 0:
        return (q, 0, 1)
    else:
        (gcd, u, v) = extend_gcd(q % p, p)
        return (gcd, v - (q // p) * u, u)
a, x, y = extend_gcd(26513, 32321)
print("crypto{{{},{}}}".format(x, y))