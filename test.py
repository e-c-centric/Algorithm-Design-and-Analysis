# # def rod_cutting(n, prices):
# #     # Create a memoization table initialized with zeros
# #     memo = [0] * (n + 1)

# #     # Iterate over each rod length
# #     for i in range(1, n + 1):
# #         max_price = -1
# #         # Consider all possible ways to cut the rod
# #         for j in range(1, i + 1):
# #             # Update the maximum sale price for the current rod length
# #             # using the sale price of a piece of length j (prices[j - 1])
# #             max_price = max(max_price, prices[j - 1] + memo[i - j])
# #         memo[i] = max_price

# #     # Return the maximum sale price for a rod of length n
# #     return memo[n]

# # Example usage:
# # rod_length = 5
# # prices = [1, 5, 8, 9, 10]  # Sale prices for rods of length 1, 2, 3, 4, 5
# # max_sale_price = rod_cutting(rod_length, prices)
# # print("Maximum total sale price:", max_sale_price)

# import itertools
# import numpy as np
# def multifragment_heuristic(graph):
#     tour_edges = set()
#     sorted_edges = sorted([(weight, src, dest) for src, neighbors in graph.items() 
#                            for dest, weight in sorted(neighbors.items()) if src < dest])

#     for weight, src, dest in sorted_edges:
#         if len(tour_edges) == 2 * (len(graph) - 1):
#             break  # All cities are connected, stop adding edges
        
#         if _check_valid_edge(tour_edges, src, dest):
#             tour_edges.add((src, dest))
    
#     return tour_edges

# def _check_valid_edge(tour_edges, src, dest):
#     if _creates_vertex_of_degree_3(tour_edges, src, dest):
#         return False
#     if _creates_cycle_less_than_n(tour_edges, src, dest):
#         return False
#     return True

# def _creates_vertex_of_degree_3(tour_edges, src, dest):
#     return sum(1 for edge in tour_edges if src in edge or dest in edge) >= 3

# def _creates_cycle_less_than_n(tour_edges, src, dest):
#     visited = set()
#     visited.add(src)
#     visited.add(dest)
#     queue = [src, dest]

#     while queue:
#         current = queue.pop(0)
#         for edge in tour_edges:
#             if current in edge:
#                 neighbor = edge[0] if edge[1] == current else edge[1]
#                 if neighbor not in visited:
#                     visited.add(neighbor)
#                     queue.append(neighbor)

#     return len(visited) < len(tour_edges) + 1
# # Example usage:
# graph = {
#     'A': {'B': 10, 'C': 15, 'D': 20},
#     'B': {'C': 35, 'D': 25},
#     'C': {'D': 50},
#     'D': {}
# }

# for src, neighbors in graph.items():
#     for dest in neighbors:
#         if dest not in graph or src not in graph[dest]:
#             if dest not in graph:
#                 graph[dest] = {}
#             graph[dest][src] = graph[src][dest]

# tour_edges = multifragment_heuristic(graph)
# print("Tour Edges:", tour_edges)

# def brute_force(graph):
#     # Generate all possible permutations of the vertices
#     vertices = list(graph.keys())
#     permutations = itertools.permutations(vertices)

#     # Initialize variables to track the minimum weight and corresponding tour
#     min_weight = float('inf')
#     min_tour = None

#     # Iterate over each permutation
#     for tour in permutations:
#         # Calculate the weight of the tour
#         weight = 0
#         for i in range(len(tour) - 1):
#             src = tour[i]
#             dest = tour[i + 1]
#             weight += graph[src][dest]

#         # Check if the weight is smaller than the current minimum
#         if weight < min_weight:
#             min_weight = weight
#             min_tour = tour

#     return min_tour, min_weight

# # Example usage:
# min_tour, min_weight = brute_force(graph)
# print("Minimum tour:", min_tour)
# print("Minimum weight:", min_weight)

# accuracy_ratio = sum(graph[src][dest] for src, dest in tour_edges) / min_weight

# # Print the accuracy ratio
# print("Accuracy ratio:", accuracy_ratio)
# print(sum(graph[src][dest] for src, dest in tour_edges))

import heapq


def dijkstra(graph, start):
    # Initialize distances dictionary with infinity for all vertices except start
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    # Initialize priority queue with start vertex and its distance
    pq = [(0, start)]

    while pq:
        # Pop vertex with minimum distance from priority queue
        current_distance, current_vertex = heapq.heappop(pq)

        # Skip if the current distance is greater than the stored distance
        if current_distance > distances[current_vertex]:
            continue

        # Iterate over neighbors of the current vertex
        for neighbor, weight in graph[current_vertex].items():
            # Calculate the new distance to the neighbor
            distance = current_distance + weight

            # Update the distance if it's smaller than the stored distance
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # Push the neighbor and its distance to the priority queue
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Example usage:
graph = {
    'A': {'B': 2, 'C': 7, 'E': 12},
    'B': {'C': 2},
    'C': {'D': -1, 'E': 2, 'B':3},
    'D': {'F':2},
    'E': {'A': -4, 'G': -7},
    'F': {'G': 2},
    'G': {'D': 1}
}

# Remove the edge from 'C' to 'B'
del graph['E']['G']

start_vertex = 'A'
distances = dijkstra(graph, start_vertex)
print("Distances from", start_vertex + ":", distances)