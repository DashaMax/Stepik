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


# COUNT = 0
#
#
# def get_inversions(l: list):
#     if len(l) == 1:
#         return l
#
#     left = get_inversions(l[:len(l) // 2])
#     right = get_inversions(l[len(l) // 2:])
#     list_sort = []
#     global COUNT
#     i = j = 0
#
#     while i < len(left) and j < len(right):
#         if left[i] > right[j]:
#             COUNT += len(left) - i
#             list_sort.append(right[j])
#             j += 1
#         else:
#             list_sort.append(left[i])
#             i += 1
#
#     if i < len(left):
#         list_sort.extend(left[i:])
#     elif j < len(right):
#         list_sort.extend(right[j:])
#
#     return list_sort
#
#
# def main():
#     numbers = list(map(int, input('-> ').split()))
#     get_inversions(numbers)
#     print(COUNT)





###########################
#   Sorting by counting   #
###########################


# def sort_by_counting(l: list) -> map:
#     counts = [0] * 10
#     s = ''
#
#     for num in l:
#         counts[num - 1] += 1
#
#     for i, num in enumerate(counts):
#         s += (str(i + 1) + ' ') * num
#
#     return map(int, s.split())
#
#
# def main():
#     nums = list(map(int, input('-> ').split()))
#     print(*sort_by_counting(nums))










###########################
#   Points and segments   #
###########################


from random import randint
import bisect


def count_point(l1: list, l2: list, dot: int) -> int:
    return abs(bisect.bisect(l1, dot) - bisect.bisect_left(l2, dot))


def quick_sort(l: list) -> list:
    if len(l) == 1 or not l:
        return l

    value = l[randint(0, len(l) - 1)]
    left = [x for x in l if x < value]
    eq = [x for x in l if x == value]
    right = [x for x in l if x > value]

    return quick_sort(left) + eq + quick_sort(right)


def main():
    n, m = map(int, input('-> ').split())
    coords_start = []
    coords_end = []

    for i in range(n):
        coords = input('-> ').split()
        coords_start.append(int(coords[0]))
        coords_end.append(int(coords[1]))

    dots = [int(x) for x in input('-> ').split()]

    coords_start = quick_sort(coords_start)
    coords_end = quick_sort(coords_end)

    for dot in dots:
        print(count_point(coords_start, coords_end, int(dot)), end=' ')


if __name__ == '__main__':
    main()