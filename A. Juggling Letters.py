def process(l, p):
    d = dict()
    for item in l:
        g = list(item)
        for i in g:
            if i in d.keys():
                d[i] = d[i] + 1
            else:
                d[i] = 1

    for i in d:
        if d[i] % p != 0:
            print("NO")
            return

    print("YES")


def main():
    t = int(input())
    k = list()
    while t > 0:
        k.clear()
        n = int(input())
        for i in range(0, n):
            k.append(input())
        process(k, n)
        t -= 1


if __name__ == "__main__":
    main()
