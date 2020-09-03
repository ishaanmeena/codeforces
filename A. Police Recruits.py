def main():
    n = int(input())
    q = list()
    p = [int(x) for x in input().split()]
    counter = 0
    for i in p:
        if i != -1:
            for y in range(0, i):
                q.append(1)
                counter += 1
        else:
            if counter > 0:
                counter -= 1
                q.remove(1)
            else:
                q.append(-1)
    print(q.count(-1))


if __name__ == "__main__":
    main()
