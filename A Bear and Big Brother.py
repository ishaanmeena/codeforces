f = [int(x) for x in input().split()]
k = f[0] #k dollars for the first banana, 2k dollars for the second one and so on
n = f[1] #n dollars
x = 0
while k <= n:
    k = k * 3
    n = n * 2
    x+=1
print(x)