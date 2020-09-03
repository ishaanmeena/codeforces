def main():
    l = [int(x) for x in input().split()]
    l.sort()
    for i in range(0, len(l) - 1):
        print(abs(l[i] - l[3]), end=" ")


if __name__ == "__main__":
    main()
