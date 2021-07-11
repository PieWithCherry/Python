from sys import argv

nb, base = argv[1:3]


def itoBase(nb, base):
    alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    base = len(base)
    n = abs(int(nb))
    b = alpha[n % base]
    while n >= base:
        n = n // base
        b += alpha[n % base]

    return b[::-1]


if __name__ == '__main__':
    print(itoBase(nb, base))
