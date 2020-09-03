n = int(input())
x = list()
y = list()
while n > 0:
    l = [int(x) for x in input().split()]
    x.append(l[0])
    y.append(l[1])
    n-=1

d = 0

for i in x:
    for j in y:
        if i == j:
            d+=1
print(d)