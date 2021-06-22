# a*b where len(a) > len(b) a, b는 10^n의 계수로된 리스트


def addTo(a, b, exp):
    return (a + b)*(10**exp)


def subFrom(a, b):
    return a - b


def karatsuba(a, b):
    sa, sb = str(a), str(b)
    an, bn = len(sa), len(sb)

    if an == 1 or bn == 1:
        return a * b

    half = min(an, bn)//2

    a0 = int(sa[:half])
    a1 = int(sa[half:])
    b0 = int(sb[:half])
    b1 = int(sb[half:])
    z2 = karatsuba(a1, b1)
    z0 = karatsuba(a0, b0)
    z1 = karatsuba(a0+a1, b0+b1) - z0 - z2

    return 10**(2*half) * z0 + 10**half * z1 + z2


print(karatsuba(25, 15))