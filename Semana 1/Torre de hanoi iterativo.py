'''
    Torres de Hanoi Iterativo
'''

def hanoi_iterativo(n, origen, auxiliar, destino):
    """
    Resuelve el problema de las Torres de Hanói de forma iterativa,
    siguiendo un patrón matemático.

    Args:
        n (int): El número de discos.
        origen (str): El pilar de origen.
        auxiliar (str): El pilar auxiliar.
        destino (str): El pilar de destino.

    Returns:
        list: Una lista de cadenas que representan los movimientos.
    """
    moves = []
    
    # Definir el ciclo del disco más pequeño según la paridad de n.
    if n % 2 == 1:
        # Para n impar, el ciclo es A -> C -> B -> A...
        ciclo = [(origen, destino), (destino, auxiliar), (auxiliar, origen)]
    else:
        # Para n par, el ciclo es A -> B -> C -> A...
        ciclo = [(origen, auxiliar), (auxiliar, destino), (destino, origen)]

    # Rastrear la posición de cada disco.
    pos = {d: origen for d in range(1, n + 1)}

    total_movimientos = (1 << n) - 1
    idx_ciclo = 0

    # Funciones auxiliares para encontrar el disco superior y hacer un movimiento legal.
    def top_disk(peg):
        for d in range(1, n + 1):
            if pos[d] == peg:
                return d
        return float('inf') # Retorna infinito si la torre está vacía

    def mover_legal(p1, p2):
        top1 = top_disk(p1)
        top2 = top_disk(p2)
        
        if top1 > top2: # Si el disco superior de p1 es más grande
            pos[top2] = p1
            moves.append(f"{p2} -> {p1}")
        else:
            pos[top1] = p2
            moves.append(f"{p1} -> {p2}")

    # Algoritmo principal: alternar entre mover el disco pequeño y el movimiento legal.
    for move in range(1, total_movimientos + 1):
        if move % 2 == 1:
            # Movimientos impares: mover el disco más pequeño.
            from_peg, to_peg = ciclo[idx_ciclo]
            idx_ciclo = (idx_ciclo + 1) % 3
            pos[1] = to_peg
            moves.append(f"{from_peg} -> {to_peg}")
        else:
            # Movimientos pares: único movimiento legal entre las otras dos torres.
            pegs = {origen, auxiliar, destino}
            pegs.remove(pos[1])
            p1, p2 = pegs
            mover_legal(p1, p2)
    
    return moves

# Ejemplo de uso con 3 discos
movimientos = hanoi_iterativo(3, 'A', 'B', 'C')
for movimiento in movimientos:
    print(movimiento)

print(f"\nTotal de movimientos: {len(movimientos)}")

'''
    Torres de Hanoi con recursividad
'''

def hanoi_recursivo(n, origen, destino, auxiliar):
    """
    Resuelve el problema de las Torres de Hanói de forma recursiva.

    Args:
        n (int): El número de discos a mover.
        origen (str): El pilar de origen.
        destino (str): El pilar de destino.
        auxiliar (str): El pilar auxiliar.

    Returns:
        list: Una lista de cadenas que representan los movimientos.
    """
    moves = []

    def solve(k, from_peg, to_peg, aux_peg):
        # Caso base: si no hay discos, no hacer nada.
        if k == 0:
            return

        # Paso 1: Mover k-1 discos al auxiliar.
        solve(k - 1, from_peg, aux_peg, to_peg)

        # Paso 2: Mover el disco grande al destino.
        moves.append(f"{from_peg} -> {to_peg}")

        # Paso 3: Mover k-1 discos del auxiliar al destino.
        solve(k - 1, aux_peg, to_peg, from_peg)

    solve(n, origen, destino, auxiliar)
    return moves

# Ejemplo de uso:
# Para 3 discos, moviendo de 'A' a 'C' usando 'B' como auxiliar.
movimientos = hanoi_recursivo(3, 'A', 'C', 'B')

# Imprimir los movimientos
for movimiento in movimientos:
    print(movimiento)

print(f"\nTotal de movimientos: {len(movimientos)}")
'''
    Prueba de tiempo Iterativo y Recursivo
'''

import time

def hanoi_recursivo(n, origen, destino, auxiliar):
    # Implementación recursiva aquí (no incluida para mantener el ejemplo conciso)
    # ...
    pass

def hanoi_iterativo(n, origen, destino, auxiliar):
    # Implementación iterativa aquí (no incluida para mantener el ejemplo conciso)
    # ...
    pass

def analisis_comparativo(n):
    """
    Realiza un análisis comparativo de la velocidad de las implementaciones
    recursiva e iterativa de las Torres de Hanói.
    
    Args:
        n (int): Número de discos para la prueba.
    """
    warmups = 1
    runs = 5

    # Calentamiento (evita medir JIT/interpretación inicial)
    for _ in range(warmups):
        hanoi_recursivo(n, 'A', 'C', 'B')
        hanoi_iterativo(n, 'A', 'C', 'B')

    total_tiempo_rec = 0
    total_tiempo_ite = 0

    # Múltiples ejecuciones para mayor precisión
    for _ in range(runs):
        # Medir recursivo
        start_time_rec = time.perf_counter()
        hanoi_recursivo(n, 'A', 'C', 'B')
        end_time_rec = time.perf_counter()
        total_tiempo_rec += (end_time_rec - start_time_rec)

        # Medir iterativo
        start_time_ite = time.perf_counter()
        hanoi_iterativo(n, 'A', 'C', 'B')
        end_time_ite = time.perf_counter()
        total_tiempo_ite += (end_time_ite - start_time_ite)

    # Calcular el tiempo promedio en milisegundos
    ms_rec = (total_tiempo_rec / runs) * 1000
    ms_ite = (total_tiempo_ite / runs) * 1000
    
    # Calcular el total de movimientos
    movimientos = (1 << n) - 1

    print(f"ANÁLISIS COMPARATIVO (n={n}):")
    print(f"Recursivo: {ms_rec:.3f} ms - {movimientos} movimientos")
    print(f"Iterativo: {ms_ite:.3f} ms")
    print("\nComplejidad temporal (ambas): O(2^n)")
    print("Complejidad espacial: recursivo O(n); iterativo O(1) si es bitwise, O(n) si usa pila.")