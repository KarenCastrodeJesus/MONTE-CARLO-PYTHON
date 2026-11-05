import random
import math

def monte_carlo():
    NT = 1000
    Nc = 0
    print("=" * 65)
    print("       METODO DE MONTE CARLO PARA CALCULAR PI")
    print("=" * 65)
    print(f"Total de puntos aleatorios: {NT}")
    print("Cuadrado: 2 x 2")
    print("Radio del circulo: 1")
    print("-" * 65)
    print(f"{'Punto':<10}{'X':<15}{'Y':<15}{'Resultado'}")
    print("-" * 65)
    for i in range(1, NT + 1):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            Nc += 1
            resultado = "Dentro"
        else:
            resultado = "Fuera"
        print(f"{i:<10}{x:<15.6f}{y:<15.6f}{resultado}")
    pi_aproximado = 4 * Nc / NT
    print("\n" + "=" * 65)
    print("                RESULTADOS FINALES")
    print("=" * 65)
    print(f"Total de puntos generados (NT): {NT}")
    print(f"Puntos dentro del circulo (Nc): {Nc}")
    print(f"Puntos fuera del circulo: {NT - Nc}")
    print(f"\nProporcion Nc/NT: {Nc / NT:.6f}")
    print(f"Valor aproximado de PI: {pi_aproximado:.6f}")
    print(f"Valor real de PI:       {math.pi:.6f}")
    error = abs(math.pi - pi_aproximado)
    print(f"Error absoluto:         {error:.6f}")
    print("\nFormula utilizada:")
    print("PI = 4 * (Nc / NT)")
    print("=" * 65)

monte_carlo()
