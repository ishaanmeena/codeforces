n = int(input())

l = [int(x) for x in input().split()]
flag = False

for i in l:
    if i == 1:
        flag = True
        break

if flag:
    print("HARD")
else:
    print("EASY")