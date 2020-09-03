n = int(input())

isDistinct = True

while isDistinct:
    n+=1
    if(len(set(str(n))) == len(str(n))):
        print(n)
        isDistinct = False