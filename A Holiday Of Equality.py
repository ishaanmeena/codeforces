n = int(input())
p = [int(x) for x in input().split()]
m = max(p)
counter = 0
for i in p:
    if i < m:
        counter = counter + m - i

print(counter)
