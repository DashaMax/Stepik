def fib_mod(n, m):
    mod = [0, 1]
    a, b = 0, 1
    for i in range(1, n):
        a, b = b, (a + b) % m
        mod.append(b)
        if i > 3:
            if mod[i - 1] == 0 and mod[i] == 1 and mod[i + 1] == 1:
                mod = mod[:-3]
                break

    return mod[n % len(mod)]


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()