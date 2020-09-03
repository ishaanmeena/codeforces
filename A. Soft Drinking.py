def main():
    f = [int(x) for x in input().split()]
    n = f[0]
    k = f[1]
    l = f[2]
    c = f[3]
    d = f[4]
    p = f[5]

    nl_juice = f[6]
    np_salt = f[7]
    total_slices = c * d

    total_ml = k * l

    x = total_ml // nl_juice
    y = p // np_salt
    z = total_slices

    print(min(x, y, z) // n)


if __name__ == "__main__":
    main()
