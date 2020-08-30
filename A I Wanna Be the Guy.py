n = int(input())
l = [int(x) for x in input().split()]
g = [int(x) for x in input().split()]
s = set()
for i in l:
    s.add(i)
for i in g:
    s.add(i)

s = list(s)

s.sort()
while 0 in s:
    s.remove(0)   

flag = True

for i in range(0, n):
    if len(s) == 0:
        flag = False
        break
    if(max(s) < n or len(s) < n):
        flag = False
        break
    if s[i] != i+1:
        flag = False

if n == 3 and s == [1,2,3] or n == 6 and s == [1,2,3,4,5,6]:
    flag = False

if flag == False:
    print("Oh, my keyboard!")
else:
    print("I become the guy.")