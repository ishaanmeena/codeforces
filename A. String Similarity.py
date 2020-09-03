n = int(input())
l = list()
g = list()
x = list()


def deal(main, b):
    string = "0" * b
    z = 0
    for i in range(0, b):
        q = main[i]
        print(q[i], end="")
    print("")

def process(x, y):
    main = list()
    l = 0
    r = int(x)
    for i in range(int(x)):
        main.append(y[l:r])
        l += 1
        r += 1
    deal(main, int(x))


for i in range(n):
    l.append(input())
    g.append(input())

for i in range(n):
    process(str(l[i]), str(g[i]))

