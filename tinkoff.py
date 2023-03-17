from random import randint, choice
from time import time


# Task 1

# def check_height(a: list) -> str:
#     i = 1
#
#     while i < len(a) - 1:
#         if not(a[i - 1] <= a[i] <= a[i + 1]):
#             break
#         i += 1
#     else:
#         return 'YES'
#
#     i = 1
#
#     while i < len(a) - 1:
#         if not(a[i + 1] <= a[i] <= a[i - 1]):
#             return 'NO'
#         i += 1
#     return 'YES'
#
#
# def main():
#     list_height = list(map(int, input().split()))
#     # list_height = [randint(0, 300) for _ in range(4)]
#     # print(list_height)
#     # time_start = time()
#     result = check_height(list_height)
#     print(result)
#     # print(time() - time_start)
#
#
# if __name__ == '__main__':
#     main()





# Task 2
#
# from math import ceil
#
#
# def check(n: int, m: int, k: int) -> int:
#     return ceil(n * k / m)
#
#
# def main():
#     n, m, k = map(int, input().split())
#     # n, m, k = sorted([randint(1, 5) for _ in range(3)], reverse=True)
#     # print(n, m, k)
#     # time_start = time()
#     result = check(n, m, k)
#     print(result)
#     # print(time() - time_start)
#
#
# if __name__ == '__main__':
#     main()





# Task 3
#
# def good_str(s: str) -> int:
#     if 'a' in s and 'b' in s and 'c' in s and 'd' in s:
#         min_good_str = len(s)
#
#         for i in range(len(s)):
#             j = i + 4
#
#             while j < len(s) and len(s[i:j]) < min_good_str:
#                 if 'a' in s[i:j] and 'b' in s[i:j] and 'c' in s[i:j] and 'd' in s[i:j]:
#                     min_good_str = len(s[i:j])
#
#                 j += 1
#
#         return min_good_str
#
#     return -1
#
#
# def main():
#     n = int(input())
#     s = input()
#     # s = ''.join(choice('abcd') for _ in range(randint(5, 20)))
#     # print(s)
#     # time_start = time()
#     result = good_str(s)
#     print(result)
#     # print(time() - time_start)
#
#
# if __name__ == '__main__':
#     main()





# Task 4

# def boring_list(a: list) -> int:
#     l = 0
#     i = 0
#
#     while i < len(a) and len(a) > l:
#         set_a = set(a)
#         counts = [a.count(x) for x in set_a]
#
#         if counts.count(max(counts)) == 1 and counts.count(max(counts) - 1) == len(counts) - 1 or \
#            counts.count(max(counts)) == len(counts) - 1 and [x for x in counts if x != max(counts)][0] == 1 or \
#            counts.count(max(counts)) == len(counts):
#             l = len(a)
#
#         a.pop()
#         i += 1
#
#     return l
#
#
# def main():
#     n = int(input())
#     nums = input().split()
#     time_start = time()
#     result = boring_list(nums)
#     print(result)
#     print(time() - time_start)
#
#
# if __name__ == '__main__':
#     main()







