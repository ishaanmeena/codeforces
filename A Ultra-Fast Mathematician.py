l = list(input())
g = list(input())

for i in range(0,len(l)):
    if(l[i] != g[i]):
        print(1,end="")
    else:
        print(0,end="")