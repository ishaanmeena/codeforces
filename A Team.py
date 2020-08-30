def process(string):
    k = 0
    for i in string:
        if i == '1':
            k+=1
    if k > 1:
        return True


n = int(input())
y = 0
while n > 0:
    x = str(input())
    result = process(x)
    if result:
        y+=1
    n-=1
print(y)
