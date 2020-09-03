l = list()

for i in range(0,5):
    a = [int(x) for x in input().split()]
    l.append(a)

for i in range(len(l)):
    for j in range(len(l[i])):
        if(l[i][j] == 1):
            print(abs(i-2) + abs(j-2))