def dfs(visited,graph,node):
    if node not in visited:
        print(node,end = " ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

def bfs(visited,graph,node,queue):
    visited.add(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s,end = " ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


visited1 = set() # TO keep track of DFS visited nodes
visited2 = set() # TO keep track of BFS visited nodes
queue = []       # For BFS
n = int(input("Enter number of nodes : "))
graph = dict()

for i in range(1,n+1):
    edges = int(input("Enter number of edges for node :- "))
    graph[i] = list()
    for j in range(1,edges+1):
        node = int(input("Enter edge for node:- "))
        graph[i].append(node)

print("The following is DFS")
dfs(visited1, graph, 1)

print("The following is BFS")
bfs(visited2, graph, 1, queue)



# Enter number of nodes : 8
# Enter number of edges for node :- 4
# Enter edge for node:- 2
# Enter edge for node:- 3
# Enter edge for node:- 4
# Enter edge for node:- 5
# Enter number of edges for node :- 2
# Enter edge for node:- 1
# Enter edge for node:- 6
# Enter number of edges for node :- 2
# Enter edge for node:- 1
# Enter edge for node:- 6
# Enter number of edges for node :- 2
# Enter edge for node:- 1
# Enter edge for node:- 7
# Enter number of edges for node :- 2
# Enter edge for node:- 1
# Enter edge for node:- 7
# Enter number of edges for node :- 3
# Enter edge for node:- 2
# Enter edge for node:- 3
# Enter edge for node:- 8
# Enter number of edges for node :- 3
# Enter edge for node:- 4
# Enter edge for node:- 5
# Enter edge for node:- 8
# Enter number of edges for node :- 2
# Enter edge for node:- 6
# Enter edge for node:- 7
# The following is DFS
# 1 2 6 3 8 7 4 5
# The following is BFS
# 1 2 3 4 5 6 7 8