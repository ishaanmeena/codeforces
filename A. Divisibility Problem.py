n = int(input())
l = list()

def process(x,y):
    r = 0
    if x%y != 0:
        print(y - x%y)
    else:
        print('0')

while n > 0:
    f = [int(x) for x in input().split()]
    l.append(f)
    n-=1

for i in l:
    process(i[0], i[1])