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