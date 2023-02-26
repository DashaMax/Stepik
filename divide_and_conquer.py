#####################
#   Binary search   #
#####################


def binary_search(l: list, a: int) -> int:
    left = 0
    right = len(l)
    middle = (left + right) // 2

    while left <= right and middle < len(l):
        if a == l[middle]:
            return middle + 1
        elif a < l[middle]:
            right = middle - 1
        else:
            left = middle + 1

        middle = (left + right) // 2

    return -1


def main():
    A = list(map(int, input('-> ').split()))[1:]
    B = list(map(int, input('-> ').split()))[1:]
    result = [binary_search(A, x) for x in B]
    print(*result)


if __name__ == '__main__':
    main()