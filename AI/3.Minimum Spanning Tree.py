class Graph:
    def add_edge(graph, u, v, w):
        graph.append([u - 1, v - 1, w])  # Subtract 1 from vertex numbers

    def find(parent, i):
        if parent[i] == i:
            return i
        return Graph.find(parent, parent[i])

    def union(parent, rank, x, y):
        x_root = Graph.find(parent, x)
        y_root = Graph.find(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def kruskal(graph, vertex):
        result = []
        i, e = 0, 0

        graph = sorted(graph, key=lambda item: item[2])

        parent = [i for i in range(vertex)]
        rank = [0] * vertex

        while e < vertex - 1:
            u, v, w = graph[i]
            i += 1
            x = Graph.find(parent, u)
            y = Graph.find(parent, v)

            if x != y:
                e += 1
                result.append([u + 1, v + 1, w])  # Add 1 to vertex numbers
                Graph.union(parent, rank, x, y)

        return result

#----------------------------------------------------------------------------
# Get input for number of vertices and edges
vertex = int(input("Enter the number of vertices: "))
edge = int(input("Enter the number of edges: "))

# Create graph object
graph = []

# Input edges
print("Enter edge details (source, destination, weight):")
for i in range(edge):
    src, dest, weight = map(int, input().split())
    Graph.add_edge(graph, src, dest, weight)

# Find Minimum Spanning Tree using Kruskal's algorithm
mst = Graph.kruskal(graph, vertex)

# Print Minimum Spanning Tree edges
print("Edges in the Minimum Spanning Tree:")
for u, v, weight in mst:
    print(f"{u} - {v} : {weight}")


#---------------------------------------------------------------------------------
# Enter the number of vertices: 4
# Enter the number of edges: 5
# Enter edge details (source, destination, weight):
# 1 2 1
# 1 3 3
# 1 4 4
# 2 3 2
# 3 4 5

# Edges in the Minimum Spanning Tree:
# 1 - 2 : 1
# 2 - 3 : 2
# 1 - 4 : 4