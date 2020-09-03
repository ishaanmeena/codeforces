def main():
    f = [int(x) for x in input().split()]
    n = f[0]
    pen = f[1]
    notebook = f[2]

    if n <= min(pen, notebook):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
