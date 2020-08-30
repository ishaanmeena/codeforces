def process(l):
    l.sort()
    for i in range(0, len(l) - 1):
        if abs(l[i] - l[i+1]) > 1:
            print("NO")
            return
        else:
            continue
    print("YES")


def main():
    n = int(input())
    for i in range(n):
        g = int(input())
        p = [int(x) for x in input().split()]
        process(p)


if __name__ == "__main__":
    main()
