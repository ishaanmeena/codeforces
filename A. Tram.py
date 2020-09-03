n = int(input())
mainList = list()
total = 0
maxm = 0
    
def process(e):
    global total
    global maxm
    current = total - e[0] + e[1]
    total = current
    if total > maxm:
         maxm = total

while n > 0:
    f = [int(x) for x in input().split()]
    mainList.append(f)
    n -= 1

for e in mainList:
    process(e)
    
print(maxm)