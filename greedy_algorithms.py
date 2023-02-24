################################
#   Cover segments with dots   #
################################


def get_dots(l: list):
    l.sort(key=lambda x: x[1])
    dots = [l[0][1]]
    dot = dots[0]
    i = 0

    while l:
        if l[i][0] <= dot:
            l.pop(i)
            i -= 1

        if i >= len(l) - 1 and l:
            i = 0
            dot = l[0][1]
            dots.append(dot)
            continue

        i += 1

    return dots


def main():
    n = int(input('-> '))
    dots = [tuple(map(int, input('-> ').split())) for _ in range(n)]
    result = get_dots(dots)
    print(len(result))
    print(*result)


if __name__ == '__main__':
    main()
