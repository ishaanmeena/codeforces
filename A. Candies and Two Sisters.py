n = int(input())
l = list()
for i in range(n):
    l.append(int(input()))

for i in l:
    if i == 1:
        print(0)
    elif i==2:
        print(0)
    else:
        print((i-1)//2)