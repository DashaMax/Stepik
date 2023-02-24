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
#
#
# if __name__ == '__main__':
#     main()





###########################
#   Continuous backpack   #
###########################


def get_max_cost(l: list, volume: float) -> float:
    costs = [(thing[0], thing[1], thing[0] / thing[1]) for thing in l]
    costs.sort(key=lambda x: x[2], reverse=True)
    max_cost = 0
    volume = volume

    for thing in costs:
        if not volume:
            break

        if thing[1] <= volume:
            max_cost += thing[0]
            volume -= thing[1]

        else:
            max_cost += volume * thing[2]
            volume = 0

    return max_cost


def main():
    count_things, backpack_volume = map(float, input('-> ').split())
    things = [tuple(map(float, input('-> ').split())) for _ in range(int(count_things))]
    costs = f'{get_max_cost(things, backpack_volume):.3f}'
    print(costs)


if __name__ == '__main__':
    main()
