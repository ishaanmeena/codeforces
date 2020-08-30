n = int(input())

for i in range(1, n):
    if n == 1:
        print("I love it")
        break
    else:
        if(i%2 == 0):
            print("I love that", end=" ")
        else:
            print("I hate that", end=" ")
if(n%2 == 0 and n!=1):
    print("I love it")
else:
    print("I hate it")
