def process(l):
    s = set(l)
    print(len(s))


def main():
    for i in range(int(input())):
        n = input()
        p = [int(x) for x in input().split()]
        process(p)


if __name__ == "__main__":
    main()
