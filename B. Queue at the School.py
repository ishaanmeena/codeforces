def shift(mod_string):
    l = list(mod_string)
    i = 0
    while i < len(mod_string) - 1:
        if l[i] == 'B' and l[i+1] == 'G':
            l[i] = 'G'
            l[i+1] = 'B'
            i += 1
        i += 1
    return "".join(l)


def process(n, shifter):
    string = input()
    while shifter > 0:
        string = shift(string)
        shifter -= 1
    print(string)


def main():
    p = [int(x) for x in input().split()]
    process(p[0], p[1])


if __name__ == "__main__":
    main()
