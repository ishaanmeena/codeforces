def driver(l, n):
    s = 0
    d = 0
    start = 0
    end = n - 1
    for i in range(0, n):
        if i % 2 == 0:
            if l[start] > l[end]:
                s += l[start]
                start += 1
            elif l[start] < l[end]:
                s += l[end]
                end -= 1
            elif l[start] == l[end]:
                s += l[start]
                start += 1
        else:
            if l[start] > l[end]:
                d += l[start]
                start += 1
            elif l[start] < l[end]:
                d += l[end]
                end -= 1
            elif l[start] == l[end]:
                d += l[start]
                start += 1
    print("{} {}".format(s, d))
 
 
def main():
    n = int(input())
    p = [int(x) for x in input().split()]
    driver(p, n)
 
 
if __name__ == "__main__":
    main()