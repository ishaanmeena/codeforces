def solve(l):
    for x in l:
        g = list(x)
        i = 0
        while i < len(g) - 1:
            if g[i] == g[i + 1]:
                print(g[i], end="")
                i += 1
            else:
                print(g[i], end="")
            i += 1
        print(g[-1])


def main():
    n = int(input())
    l = list()
    for i in range(n):
        l.append(input())
    solve(l)


if __name__ == "__main__":
    main()
