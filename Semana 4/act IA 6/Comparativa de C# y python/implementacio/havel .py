# graph_validator.py

def is_graphical_sequence(seq):
    """
    Verifica si una secuencia es gráfica usando Havel-Hakimi.
    """
    seq = sorted((x for x in seq if x > 0), reverse=True)

    while seq:
        d = seq.pop(0)

        if d == 0:
            return True
        if d > len(seq):
            return False

        for i in range(d):
            seq[i] -= 1
            if seq[i] < 0:
                return False

        seq = sorted((x for x in seq if x > 0), reverse=True)

    return True


def validate_consistency(graph):
    """
    Verifica consistencia: suma de grados par para grafo no dirigido.
    """
    total_degree = sum(graph.out_degree(v) for v in graph.vertices())
    return total_degree % 2 == 0


def extract_degree_sequence(graph):
    """
    Extrae secuencia de grados de un grafo.
    """
    degrees = [graph.out_degree(v) for v in graph.vertices()]
    degrees.sort(reverse=True)
    return degrees


# ejemplo de uso
if __name__ == "__main__":
    # Ejemplo de secuencia
    s = [5,5,5,5,5,5,4,4,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2]
    print("¿Es gráfica?", is_graphical_sequence(s))
