def process(n, k):
    for i in range(k):
        if(n % 10 != 0):
            n = n-1
        else:
            n = n//10
    return n

f = [int(x) for x in input().split()]
ans = process(f[0], f[1])
print(ans)