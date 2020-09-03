def main():
    t = int(input())
    m = 0
    c = 0
    for i in range(0, t):
        p = [int(x) for x in input().split()]
        x = p[0]
        y = p[1]

        if x > y:
            m += 1
        elif x<y:
            c += 1
    if m>c:
        print("Mishka")
    elif c>m:
        print("Chris")
    else:
        print("Friendship is magic!^^")

if __name__ == "__main__":
    main()

