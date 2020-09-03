def process(x, y):
    return x * y // 2
        
n = [int(x) for x in input().split()]
x = process(n[0], n[1])
print(x)