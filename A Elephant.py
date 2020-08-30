def process(n):
    l = [5, 4, 3, 2, 1]
    x = 0

    while n > 0:
        for i in l:
            if n - i >= 0:
                n = n - i
                x += 1
                break
    return x


f = [int(x) for x in input().split()]
ans = process(f[0])
print(ans)