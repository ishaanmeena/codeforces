def process(k):
    l = [int(x) for x in input().split()]
    g = [int(x) for x in input().split()]
    l.sort()
    g.sort(reverse=True)
    for i in range(0, len(l)):
        if k > 0:
            if l[i] > g[i]:
                continue
            else:
                l[i] = g[i]
                k -= 1
        else:
            break
    print(sum(l))


def main():
    t = int(input())
    for i in range(0, t):
        q = [int(x) for x in input().split()]
        k = q[1]
        process(k)


if __name__ == "__main__":
    main()
