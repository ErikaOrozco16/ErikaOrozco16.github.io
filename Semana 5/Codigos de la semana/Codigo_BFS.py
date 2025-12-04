from collections import deque, defaultdict

# codigo original 

def bfs(graph, start , return_order= False): # Mejora 1 por la IA :  se le agrega return order para poder utilizar los datos optenidos de nuevo
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    # Mejora 2 por la IA : Validación: grafo vacío
    if not graph:
        return [] if return_order else set()

    # Mejora 3 por la IA : Validación: nodo inicial ausente en el grafo
    if start not in graph:
        return [] if return_order else set()


    # Mejora 4 por la IA : Se añadió lista opcional para guardar el orden de recorrido
    order = []

    while queue:
        
        current = queue.popleft()
        

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                

    return visited
 


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D', 'E'],
    'D': ['B', 'C'],
    'E': ['C']
}

resultado = bfs(graph, 'A')
print(resultado)

#