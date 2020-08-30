n = int(input())
l = [100,20,10,5,1]
x = 0
while n>0:
    for i in l:
        if n-i >= 0:
            n-=i
            x+=1
            break
print(x, end="")


        