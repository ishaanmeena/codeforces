def process(l, k):
    x = 0
    for i in l:
        if i >= l[k-1] and i > 0:
            x+=1
    return x
        


n = [int(x) for x in input().split()]
l = [int(x) for x in input().split()]
x = process(l, n[1])
print(x)
