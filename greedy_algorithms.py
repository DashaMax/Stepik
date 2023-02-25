################################
#   Cover segments with dots   #
################################


# def get_dots(l: list) -> list:
#     l.sort(key=lambda x: x[1])
#     dots = [l[0][1]]
#     dot = dots[0]
#     i = 0
#
#     while l:
#         if l[i][0] <= dot:
#             l.pop(i)
#             i -= 1
#
#         if i >= len(l) - 1 and l:
#             i = 0
#             dot = l[0][1]
#             dots.append(dot)
#             continue
#
#         i += 1
#
#     return dots
#
#
# def main():
#     n = int(input('-> '))
#     dots = [tuple(map(int, input('-> ').split())) for _ in range(n)]
#     result = get_dots(dots)
#     print(len(result))
#     print(*result)





###########################
#   Continuous backpack   #
###########################


# def get_max_cost(l: list, volume: float) -> float:
#     costs = [(thing[0], thing[1], thing[0] / thing[1]) for thing in l]
#     costs.sort(key=lambda x: x[2], reverse=True)
#     max_cost = 0
#     volume = volume
#
#     for thing in costs:
#         if not volume:
#             break
#
#         if thing[1] <= volume:
#             max_cost += thing[0]
#             volume -= thing[1]
#
#         else:
#             max_cost += volume * thing[2]
#             volume = 0
#
#     return max_cost
#
#
# def main():
#     count_things, backpack_volume = map(float, input('-> ').split())
#     things = [tuple(map(float, input('-> ').split())) for _ in range(int(count_things))]
#     costs = f'{get_max_cost(things, backpack_volume):.3f}'
#     print(costs)





#####################
#   Various terms   #
#####################


# def get_terms(n: int) -> list:
#     terms = []
#     i = 1
#
#     while n:
#         if (n - i) > i or not (n - i):
#             n -= i
#             terms.append(i)
#         i += 1
#
#     return terms
#
#
# def main():
#     n = int(input('-> '))
#     result = get_terms(n)
#     print(len(result))
#     print(*result)





######################
#   Huffman coding   #
######################


# def get_huff_code(s: str) -> dict:
#     symbols = [(sym, s.count(sym)) for sym in set(s)]
#     symbols.sort(key=lambda x: x[1])
#     huff_code = {}
#
#     if len(symbols) == 1:
#         return {symbols[0][0]: '0'}
#
#     while len(symbols) > 1:
#         for i in range(len(symbols[0][0])):
#             huff_code[symbols[0][0][i]] = '0' + huff_code.get(symbols[0][0][i], '')
#
#         for i in range(len(symbols[1][0])):
#             huff_code[symbols[1][0][i]] = '1' + huff_code.get(symbols[1][0][i], '')
#
#         new = (symbols[0][0] + symbols[1][0], symbols[0][1] + symbols[1][1])
#         symbols.pop(0)
#         symbols[0] = new
#         symbols.sort(key=lambda x: x[1])
#
#     return dict(sorted(huff_code.items(), key=lambda x: len(x[1])))
#
#
# def main():
#     text = input('-> ')
#     result = get_huff_code(text)
#     huff_code = ''.join(result[x] for x in text)
#     print(len(result), len(huff_code))
#
#     for key, value in result.items():
#         print(f'{key}: {value}')
#
#     print(huff_code)





########################
#   Huffman decoding   #
########################


# def get_huff_decode(d: dict, s: str) -> str:
#     i = 1
#     decode = ''
#
#     while s:
#         if s[:i] in d:
#             decode += d[s[:i]]
#             s = s[i:]
#             i = 1
#             continue
#
#         i += 1
#
#     return decode
#
#
# def main():
#     n, m = map(int, input('-> ').split())
#     decode = {}
#
#     for i in range(n):
#         word = input('-> ').split(': ')
#         decode[word[1]] = word[0]
#
#     code = input('-> ')
#     result = get_huff_decode(decode, code)
#     print(result)





######################
#   Priority Queue   #
######################


import sys


def sift_up(l: list) -> list:
    if len(l) > 1:
        i = len(l) - 1

        while i and l[i] > l[(i - 1) // 2]:
            l[i], l[(i - 1) // 2] = l[(i - 1) // 2], l[i]
            i = (i - 1) // 2

    return l


def sift_down(l: list) -> list:
    if len(l) > 1:
        i = 0

        while 2 * i + 1 < len(l):
            if 2 * i + 2 < len(l) and l[i] < max((l[2 * i + 1], l[2 * i + 2])):
                index = 2 * i + 1 if l[2 * i + 1] > l[2 * i + 2] else 2 * i + 2
            elif l[i] < l[2 * i + 1]:
                index = 2 * i + 1
            else:
                break

            l[i], l[index] = l[index], l[i]
            i = index

    return l


def main():
    n = int(sys.stdin.readline())
    q = []

    for i in range(n):
        command = sys.stdin.readline().split()

        if command[0] == 'Insert':
            q.append(int(command[1]))
            q = sift_up(q)

        elif q:
            print(q[0])
            q[0] = q[-1]
            q.pop()
            q = sift_down(q)





######################
#   Priority Queue   #
######################


# import heapq
#
#
# def priority_queue(l: list):
#     q = []
#     heapq.heapify(q)
#
#     for command in l:
#         if command[0] == 'Insert':
#             heapq.heappush(q, -command[1])
#         elif q:
#             print(-heapq.heappop(q))
#
#
# def main():
#     n = int(input('-> '))
#     commands = []
#
#     for i in range(n):
#         command = input('-> ').split()
#
#         if len(command) == 1:
#             commands.append((command[0], ''))
#         else:
#             commands.append((command[0], int(command[1])))
#
#     priority_queue(commands)


if __name__ == '__main__':
    main()