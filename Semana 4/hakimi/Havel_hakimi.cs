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
        
        // Crear copia para no modificar la original
        var seq = new List<int>(degrees);
        
        // Ordenar no creciente
        seq.Sort((a, b) => b.CompareTo(a));
        
        // Verificar suma par y máximo grado
        int sum = seq.Sum();
        if (sum % 2 != 0 || seq[0] >= seq.Count) return false;
        
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
            //Modificacion de la IA
            seq.Sort((a, b) => b.CompareTo(a));
            Console.WriteLine($"Paso: [{string.Join(", ", seq)}]");
        }
        return true;
    }
}

 

class Program
{
    static void Main()
    {
        // 🟢 Secuencia gráfica
        var seq1 = new List<int> {5,5,5,5,5,5,4,4,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2};
        Console.WriteLine($"Secuencia: [{string.Join(", ", seq1)}]");
        Console.WriteLine($"¿Es Grafica? {GraphValidator.IsGraphicalSequence(seq1)}");
        
       
    }
}
