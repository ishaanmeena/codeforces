def find_diff(current_word, next_word):
    cost = 0
    x = 1
    d = dict()
    e = dict()
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    for i in alphabet:
        d[i] = x
        x += 1
    return min(abs(d[current_word] - d[next_word]), 26 - abs(d[current_word] - d[next_word]))


def driver(text):
    text = list(text)
    total_cost = find_diff('a', text[0])
    for i in range(0, len(text) - 1):
        current_cost = find_diff(text[i], text[i + 1])
        total_cost += current_cost
    print(total_cost)


def main():
    n = input()
    driver(n)


if __name__ == "__main__":
    main()
