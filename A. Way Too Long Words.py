def process(string):
    answer = ""
    l = len(string)
    if l>10:
        answer+=string[0]
        answer+=str(l-2)
        answer+=string[l-1]
        print(answer)
    else:
        print(string)

n = int(input())

while n > 0:
    x = str(input())
    process(x)
    n-=1
    
    