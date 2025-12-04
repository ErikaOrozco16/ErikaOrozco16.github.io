from collections import deque
from copy import deepcopy


class PlanificadorAcademico:
    def __init__(self):
        self.grafo = {}            # Lista de adyacencia
        self.grado_entrada = {}    # Grado de entrada para cada materia

    # ---------------------------------------------------
    # 1. Construcción del grafo y verificación inicial
    # ---------------------------------------------------
    def CargarDatos(self, lista_materias, lista_prerequisitos):
        # Inicializar nodos
        for materia in lista_materias:
            self.grafo[materia] = []
            self.grado_entrada[materia] = 0

        # Llenar el grafo y calcular grados de entrada
        for materia, prereq in lista_prerequisitos:
            # Arista: prereq → materia
            self.grafo[prereq].append(materia)
            self.grado_entrada[materia] += 1

        return True

    # ---------------------------------------------------
    # 2. Detección de ciclos usando Kahn (Topológico)
    # ---------------------------------------------------
    def DetectarCiclo(self):
        grado_copia = deepcopy(self.grado_entrada)
        cola = deque()
        nodos_ordenados = 0

        # Materias sin prerequisitos
        for materia in grado_copia:
            if grado_copia[materia] == 0:
                cola.append(materia)

        # Proceso de Kahn
        while cola:
            u = cola.popleft()
            nodos_ordenados += 1

            for v in self.grafo[u]:
                grado_copia[v] -= 1
                if grado_copia[v] == 0:
                    cola.append(v)

        # Si no pudimos ordenar todas, hay ciclo
        if nodos_ordenados < len(self.grafo):
            return True  # Hay ciclo
        else:
            return False

    # ---------------------------------------------------
    # 3. Generar plan óptimo por semestres
    # ---------------------------------------------------
    def GenerarPlanOptimo(self):
        if self.DetectarCiclo():
            return "ERROR: Dependencias circulares detectadas. El plan es imposible."

        # Copia para el proceso real de planificación
        grado_plan = deepcopy(self.grado_entrada)
        cola_niveles = deque()
        plan_semestres = []

        # Primer semestre: materias sin prerequisitos
        materias_nivel_1 = []
        for materia in grado_plan:
            if grado_plan[materia] == 0:
                materias_nivel_1.append(materia)

        cola_niveles.append(materias_nivel_1)
        semestre_actual = 0

        # BFS por niveles
        while cola_niveles:
            materias_sem = cola_niveles.popleft()
            semestre_actual += 1

            plan_semestres.append({
                "Semestre": semestre_actual,
                "Materias": materias_sem
            })

            materias_siguiente = []

            for u in materias_sem:
                for v in self.grafo[u]:
                    grado_plan[v] -= 1
                    if grado_plan[v] == 0:
                        materias_siguiente.append(v)

            if len(materias_siguiente) > 0:
                cola_niveles.append(materias_siguiente)

        return plan_semestres, semestre_actual


# ----------------------------
# Ejemplo de uso EXACTO a tu caso
# ----------------------------

Materias = ["M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "M9", "M10"]
PreRequisitos = [
    ("M3", "M1"), ("M7", "M1"),
    ("M4", "M3"), ("M4", "M2"),
    ("M5", "M3"), ("M6", "M3"),
    ("M9", "M5"), ("M9", "M7"),
    ("M8", "M6"),
    ("M10", "M4"), ("M10", "M9")
]

plan = PlanificadorAcademico()
plan.CargarDatos(Materias, PreRequisitos)

Plan_Final, Semestres = plan.GenerarPlanOptimo()

print("Plan Final:", Plan_Final)
print("Semestres Mínimos:", Semestres)
