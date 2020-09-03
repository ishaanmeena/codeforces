f = [int(x) for x in input().split()]
k = f[0] #k dollars for the first banana, 2k dollars for the second one and so on
n = f[1] #n dollars
w = f[2] #buy w bananas
cost = 0
for i in range(1,w+1):
    cost+=k*i
if n-cost < 0:
    print(abs(n-cost))
else:
    print(0)