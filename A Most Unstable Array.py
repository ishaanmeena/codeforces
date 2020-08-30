def process(x, y):
    if x == 1:
        print(0)
        return
    elif x == 2:
        print(y)
    else:
        print(y * 2)


def main():
    t = int(input())
    while t > 0:
        p = [int(x) for x in input().split()]
        process(p[0], p[1])
        t -= 1


if __name__ == "__main__":
    main()
