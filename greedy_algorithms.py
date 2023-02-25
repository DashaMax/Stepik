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


def get_huff_decode(d: dict, s: str) -> str:
    i = 1
    decode = ''

    while s:
        if s[:i] in d:
            decode += d[s[:i]]
            s = s[i:]
            i = 1
            continue

        i += 1

    return decode


def main():
    n, m = map(int, input('-> ').split())
    decode = {}

    for i in range(n):
        word = input('-> ').split(': ')
        decode[word[1]] = word[0]

    code = input('-> ')
    result = get_huff_decode(decode, code)
    print(result)


if __name__ == '__main__':
    main()