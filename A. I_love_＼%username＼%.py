def main():
    n = int(input())
    l = [int(x) for x in input().split()]
    l = list(set(l))
    counter = 1

    r = 0

    for i in range(0,len(l) - 1):
        if l[i] == l[i+1]:
            r += 1
        else:
            break

    if len(l) == 1:
        counter -= 1
    elif l[r] > l[r+1]:
        p = l[r]
        q = l[r+1]
    elif l[r] < l[r+1]:
        p = l[r+1]
        q = l[r]

    for i in range(1, len(l)):
        if l[i] > p:
            p = l[i]
            counter += 1
        elif l[i] < q:
            q = l[i]
            counter += 1
    print(counter)


if __name__ == "__main__":
    main()
