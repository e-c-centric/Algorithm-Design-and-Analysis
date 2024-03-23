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
for edge in mst_edges:
    print(edge)
