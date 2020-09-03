import math


def driver(x, y, z):
    i = 2
    while z > 0:
        if i % 2 == 0:
            if math.gcd(x, z) < z:
                z -= math.gcd(x, z)
            else:
                print("0")
                return
        else:
            if math.gcd(y, z) < z:
                z -= math.gcd(y, z)
            else:
                print("1")
                return
        i += 1


def main():
    p = [int(x) for x in input().split()]
    driver(p[0], p[1], p[2])


if __name__ == "__main__":
    main()
