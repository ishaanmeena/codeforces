def process(p):
    x = p.count(1)
    y = p.count(2)
    z = p.count(3)

    m = min(x, y, z)
    print(m)

    if m != 0:
        i = 0
        while i < m:
            a = p.index(1)
            b = p.index(2)
            c = p.index(3)
            print("{} {} {}".format(a+1, b+1, c+1))
            p[a] = 4
            p[b] = 4
            p[c] = 4
            i+=1


def main():
    t = int(input())
    p = [int(x) for x in input().split()]
    process(p)


if __name__ == "__main__":
    main()
