l = [int(x) for x in input().split()]

l.sort()

print(abs(l[1] - l[0]) + abs(l[2] - l[1]))