def process(n):
    if n == 2:
        print(1)
        print(2)
        return
    x = n % 2
    y = n // 2
    if x == 0:
        print(x + y)
    else:
        print(x + y - 1)
    if x == 0:
        for i in range(0, y):
            print(2, end=" ")
        return
    else:
        for i in range(0, y - 1):
            print(2, end=" ")
    for i in range(0, x):
        print(3, end=" ")


def main():
    t = int(input())
    process(t)


if __name__ == "__main__":
    main()
