from collections import defaultdict

def dfs_cycle_detection(graph, num_nodes):
    # Conjunto de nodos ya visitados globalmente (completamente procesados)
    visited = set()
    # Conjunto de nodos en el camino de recursión actual
    recursion_stack = set()
    
    # Recorrer todos los nodos en caso de que el grafo no esté conectado
    for node in range(1, num_nodes + 1):
        if node not in visited:
            if explore(node, visited, recursion_stack, graph):
                return True # Ciclo detectado
    
    return False # No se detectó ciclo en ninguna componente
    
def explore(node, visited, recursion_stack, graph):
    
    # 1. Marcar como visitado globalmente
    visited.add(node)
    
    # 2. Agregar a la pila de recursión (camino actual)
    recursion_stack.add(node) 

    # 3. Explorar vecinos
    for neighbor in graph[node]:
        
        # CASO 1: Vecino en la pila de recursión (¡CICLO!)
        if neighbor in recursion_stack:
            return True 
        
        # CASO 2: Vecino no ha sido visitado nunca
        if neighbor not in visited:
            if explore(neighbor, visited, recursion_stack, graph):
                return True

    # 4. Procesamiento completado: eliminar de la pila de recursión
    recursion_stack.remove(node)
    return False

graph = defaultdict(list)

graph[1].append(2)
graph[2].append(3)
graph[3].append(4)  
graph[4].append(2)  # <-- Ciclo

num_nodes = 4

if dfs_cycle_detection(graph, num_nodes):
    print("⚠️ Se detectó un ciclo")
else:
    print("✅ No hay ciclos")