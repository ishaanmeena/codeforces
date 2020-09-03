n = list(input())
lower = 0
upper = 0
for i in n:
    if i.isupper():
        upper+=1
    else:
        lower+=1
if lower<upper:
    print("".join(n).upper())
else:
    print("".join(n).lower())
