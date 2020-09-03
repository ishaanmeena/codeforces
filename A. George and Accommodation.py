n = int(input())
mainList = list()

def process(mainList):
    counter = 0
    for i in mainList:
        if i[1] - i[0] >= 2:
            counter+=1
    print(counter)

while n>0:
    f = [int(x) for x in input().split()]
    mainList.append(f)
    n-=1
    
process(mainList)