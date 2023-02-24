def gcd(a, b):
    if a == b:
        return a
    elif a == 0:
        return b
    elif b == 0:
        return a

    if b > a:
        a, b = b, a

    while b:
        a, b = b, a % b

    return a


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()

