n = int(input())
x = 0
for i in range(0,n):
    s = input()
    if s[1] == '-':
        x -= 1
    elif s[1] == '+':
        x += 1

print(x)
