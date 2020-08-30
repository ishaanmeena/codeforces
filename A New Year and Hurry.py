def solve(n, k):
    total = 240 - k
    counter = 0
    for i in range(1, n + 1):
        if(total - 5*i) >= 0:
            total -= 5 * i
            counter += 1
        else:
            break
    print(counter)


def main():
    l = [int(x) for x in input().split()]
    solve(l[0], l[1])


if __name__ == "__main__":
    main()
