# Define the graph with weighted edges
graph = {
    'a': [('b', 3), ('c', 5), ('d', 4)],
    'b': [('f', 6), ('e', 3)],
    'c': [('g', 4), ('d', 2)],
    'd': [('e', 1), ('h', 5)],
    'e': [('f', 2), ('i', 4)],
    'f': [('j', 5)],
    'g': [('h', 3), ('k', 6)],
    'h': [('i', 6), ('k',7)],
    'i': [('j', 3),('l', 5)],
    'j': [('l', 9)],
    'k': [('l', 8)],
    'l': []
}

# Generate the sorted list of edges
edges = []
for node, neighbors in graph.items():
    for neighbor, weight in neighbors:
        edges.append((node, neighbor, weight))

sorted_edges = sorted(edges, key=lambda x: (x[2], x[0], x[1]))  # Sort by weight, then node1, then node2
print(len(sorted_edges))

# Kruskal's algorithm to generate the MST
parent = {}
rank = {}

def make_set(node):
    parent[node] = node
    rank[node] = 0

def find_set(node):
    if parent[node] != node:
        parent[node] = find_set(parent[node])
    return parent[node]

def union(node1, node2):
    root1 = find_set(node1)
    root2 = find_set(node2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1

mst_edges = []
for edge in sorted_edges:
    node1, node2, weight = edge
    if node1 not in parent:
        make_set(node1)
    if node2 not in parent:
        make_set(node2)
    if find_set(node1) != find_set(node2):
        union(node1, node2)
        mst_edges.append(edge)

# Print the edges that form the MST
# for edge in mst_edges:
#     print(edge)

import heapq

# Define the graph with weighted edges
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    pq = [(0, start)]
    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

distances = dijkstra(graph, 'a')
# print(distances)

def knapsack_bottom_up(weights, profits, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] <= j:
                dp[i][j] = max(profits[i - 1] + dp[i - 1][j - weights[i - 1]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][capacity]

weights = [1, 2, 3, 4, 2, 1]
profits = [2, 4, 5, 5, 2, 3]
capacity = 1

max_profit = knapsack_bottom_up(weights, profits, capacity)
print("Maximum profit:", max_profit)

def knapsack(weights, profits, capacity):
    n = len(weights)
    # Initialize a table to store the maximum profit for each subproblem
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    # Build the table bottom-up
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            # If the current item's weight is greater than the current capacity,
            # we cannot include it in the knapsack
            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                # Consider both options: include the current item or exclude it
                dp[i][w] = max(dp[i - 1][w], profits[i - 1] + dp[i - 1][w - weights[i - 1]])

    # Print the entire table
    print("Dynamic Programming Table:")
    for row in dp:
        print(row)

    # Trace back to find the items included in the knapsack
    items = []
    i, w = n, capacity
    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:
            items.append(i - 1)
            w -= weights[i - 1]
        i -= 1

    return dp[n][capacity], items

# Example usage:
weights = [1, 2, 3, 4, 2, 1]
profits = [2, 4, 5, 5, 2, 3]
capacity = 8
max_profit, selected_items = knapsack(weights, profits, capacity)
print("\nMaximum profit:", max_profit)
print("Selected items:", selected_items)
 
def knapsack_topdown(weights, profits, capacity):
    n = len(weights)
    # Initialize the memoization table with 'X'
    memo = [['X'] * (capacity + 1) for _ in range(n + 1)]

    def helper(n, capacity):
        # Base case: if the capacity is 0 or there are no items left, return 0
        if capacity == 0 or n == 0:
            return 0

        # If the value is already computed, return it
        if memo[n][capacity] != 'X':
            return memo[n][capacity]

        # If the weight of the current item is greater than the capacity, skip it
        if weights[n - 1] > capacity:
            memo[n][capacity] = helper(n - 1, capacity)
        else:
            # Consider both options: include the current item or exclude it
            include = profits[n - 1] + helper(n - 1, capacity - weights[n - 1])
            exclude = helper(n - 1, capacity)
            # Store the maximum of the two options
            memo[n][capacity] = max(include, exclude)

        # Mark the value as "R" if it's retrieved without recomputation
        if memo[n][capacity] == max(include, exclude):
            memo[n][capacity] = 'R'

        return memo[n][capacity]

    # Start the recursion
    max_profit = helper(n, capacity)

    # Replace 'X' with sentinel value -1
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if memo[i][j] == 'X':
                memo[i][j] = -1

    # Print the memoization table
    for row in memo:
        print(row)

    return max_profit

max_profit, selected_items = knapsack_topdown(weights, profits, capacity)
print("\nMaximum profit:", max_profit)