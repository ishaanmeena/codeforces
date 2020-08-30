def process(x):
    x = str(x)
    l = list()
    for i in range(len(x)):
        if x[i] == '0':
            continue
        else:
            l.append(x[i]+("0" * (len(x) - i - 1)))
    print(len(l))
    for item in l:
        print(item, end=" ")
    print("")


def main():
    n = int(input())
    l = list()
    for i in range(n):
        l.append(input())

    for i in range(n):
        process(str(l[i]))


if __name__ == "__main__":
    main()
