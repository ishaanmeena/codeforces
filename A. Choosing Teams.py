def process(l, k):
    l.sort()
    for i in range(0, len(l)):
        l[i] += k
    counter = 0
    for i in range(0, len(l)):
        if l[i] > 5:
            counter += 1
    print((len(l) - counter)//3)


def main():
    q = [int(x) for x in input().split()]
    p = [int(x) for x in input().split()]
    process(p, q[1])


if __name__ == "__main__":
    main()
