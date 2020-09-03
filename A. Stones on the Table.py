n = input()
string = input()
a = list(string)
x = 0
res = list(zip(a, a[1:]))
for i in res:
    if i[0] == i[1]:
        x+=1
print(x)