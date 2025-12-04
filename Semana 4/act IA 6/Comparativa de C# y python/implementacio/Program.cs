using System;
using System.Collections.Generic;
using System.Linq;

public static class GraphValidator
{
    /// <summary>
    /// Valida si una secuencia es gráfica usando Havel-Hakimi.
    /// </summary>
    public static bool IsGraphicalSequence(List<int> degrees)
    {
        if (degrees.Count == 0) return true;

        var seq = new List<int>(degrees);

        seq.Sort((a, b) => b.CompareTo(a));

        int sum = seq.Sum();
        if (sum % 2 != 0 || seq[0] > seq.Count) return false;

        while (seq.Count > 0)
        {
            int d1 = seq[0];
            seq.RemoveAt(0);

            if (d1 == 0) return true;
            if (d1 > seq.Count) return false;

            for (int i = 0; i < d1; i++)
            {
                seq[i]--;
                if (seq[i] < 0) return false;
            }

            seq.Sort((a, b) => b.CompareTo(a));

            Console.WriteLine($"Paso: [{string.Join(", ", seq)}]");
        }
        return true;
    }

    /// <summary>
    /// Verifica consistencia: suma grados par para grafo no dirigido.
    /// </summary>
    public static bool ValidateConsistency(Graph<String> graph)
    {
        int totalDegree = graph.Vertices().Sum(v => graph.OutDegree(v));
        // En grafo no dirigido, suma de grados = 2 * |aristas|, debe ser par
        return totalDegree % 2 == 0;
    }

    /// <summary>
    /// Extrae secuencia de grados de un grafo.
    /// </summary>
    public static List<int> ExtractDegreeSequence(Graph<String> graph)
    {
        var degrees = graph.Vertices()
                           .Select(v => graph.OutDegree(v))
                           .OrderByDescending(d => d)
                           .ToList();
        return degrees;
    }
}

class Program
{
    static void Main()
    {
        var seq1 = new List<int> {5,5,5,5,5,5,4,4,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2};
        Console.WriteLine($"Secuencia: [{string.Join(", ", seq1)}]");
        Console.WriteLine($"¿Es Grafica? {GraphValidator.IsGraphicalSequence(seq1)}");
    }
}
