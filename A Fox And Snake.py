l = [int(x) for x in input().split()]
flag = True
for i in range(2, l[0]+2):
    if(i % 2 == 0):
        print("#"*l[1])
    elif(flag):
        print("." * (l[1] - 1),end="#\n")
        flag=False
    else:
        print("#",end="")
        print("." * (l[1]-1))
        flag=True