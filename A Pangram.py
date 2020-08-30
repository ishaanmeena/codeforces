n = int(input())
l = input()
s = set()
for i in l:
    s.add(i.lower())
s = list(s)
if(len(s) == 26):
    print("YES")
else:
    print("NO")