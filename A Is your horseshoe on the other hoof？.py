l = [int(x) for x in input().split()]
s = set()
for i in l:
    s.add(i)

print(4 - len(s))