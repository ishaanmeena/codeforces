n = input()
n = n[1:len(n)-1]
n = n.split(",")
s = set()
for i in n:
    i = i.strip()
    s.add(i)
    


if n[0] == '':
    print ('0')
else:
    print(len(s))
