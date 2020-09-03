f = [int(x) for x in input().split()]
g = [int(x) for x in input().split()]

x = 0

for i in g:
    if i > f[1]:
        x+=2
    else:
        x+=1
print(x)