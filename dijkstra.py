##############################
#    Dijkstra's algorithm    #
##############################


graph = {
    'start': {'A': 5, 'B': 2},
    'A': {'C': 4, 'D': 2},
    'B': {'A': 8, 'D': 7},
    'C': {'D': 6, 'end': 3},
    'D': {'end': 1},
    'end': {}
}
costs = {'A': 5, 'B': 2, 'C': float('inf'), 'D': float('inf'), 'end': float('inf')}

parents = {'A': 'start', 'B': 'start', 'C': None, 'D': None, 'end': None}
processed = []


def find_lowest_cost_node(costs: dict) -> str:
    lower_cost = float('inf')
    lower_cost_node = None

    for node, cost in costs.items():
        if cost < lower_cost and node not in processed:
            lower_cost = cost
            lower_cost_node = node

    return lower_cost_node


node = find_lowest_cost_node(costs)

while node:
    cost_node = costs[node]
    neighbors = graph[node]

    for neighbor, cost in neighbors.items():
        new_cost = cost_node + cost

        if new_cost < costs[neighbor]:
            costs[neighbor] = new_cost
            parents[neighbor] = node

    processed.append(node)
    node = find_lowest_cost_node(costs)


result_cost_end = costs['end']

print(graph)
print(costs)
print(parents)
print(result_cost_end)



####################################