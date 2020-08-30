n = int(input())
l = list()

while n>0:
    x = input()
    l.append(x)
    n-=1
   
l = list(zip(l, l[1:]))

x = 1

for i in l:
    if i[0] != i[1]:
        x+=1
print(x)