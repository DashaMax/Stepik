#####################
#   Binary search   #
#####################


# def binary_search(l: list, a: int) -> int:
#     left = 0
#     right = len(l)
#     middle = (left + right) // 2
#
#     while left <= right and middle < len(l):
#         if a == l[middle]:
#             return middle + 1
#         elif a < l[middle]:
#             right = middle - 1
#         else:
#             left = middle + 1
#
#         middle = (left + right) // 2
#
#     return -1
#
#
# def main():
#     A = list(map(int, input('-> ').split()))[1:]
#     B = list(map(int, input('-> ').split()))[1:]
#     result = [binary_search(A, x) for x in B]
#     print(*result)





############################
#   Number of inversions   #
############################


COUNT = 0


def get_inversions(l: list):
    if len(l) == 1:
        return l

    left = get_inversions(l[:len(l) // 2])
    right = get_inversions(l[len(l) // 2:])
    list_sort = []
    global COUNT
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            COUNT += len(left) - i
            list_sort.append(right[j])
            j += 1
        else:
            list_sort.append(left[i])
            i += 1

    if i < len(left):
        list_sort.extend(left[i:])
    elif j < len(right):
        list_sort.extend(right[j:])

    return list_sort


def main():
    numbers = list(map(int, input('-> ').split()))
    get_inversions(numbers)
    print(COUNT)


if __name__ == '__main__':
    main()