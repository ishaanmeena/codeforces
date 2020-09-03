x = input()
y = input()
z = input()

p = dict()
q = dict()

x = x + y

isEqual = True

for i in x:
    if i in p:
        p[i] = p[i] + 1
    else:
        p[i] = 1
    
for i in z:
    if i in q:
        q[i] = q[i] + 1
    else:
        q[i] = 1

if (len(x) != len(z)):
    isEqual = False
else:
    for i in p:
        try:
            if p[i] != q[i]:
                isEqual = False
                break
        except KeyError:
                isEqual = False
                break

if isEqual:
    print("YES")
else:
    print("NO")
    
        