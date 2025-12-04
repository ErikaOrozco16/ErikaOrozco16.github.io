from collections import defaultdict

def dfs(graph, start):
    visited = set()

    def explore(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                explore(neighbor)

    explore(start)
    return visited


graph = {
    'A': ['A', 'B'],
    'B': ['B', 'C'],
    'C': ['C', 'D'],
    'D': ['D', 'B']
    
}

resultado = dfs(graph, 'A')
print(resultado)