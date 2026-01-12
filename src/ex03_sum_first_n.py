"""
Ejercicio 3:
Suma de los primeros n números.
"""

def sum_first_n(n: int) -> int:
    """
    Devuelve la suma 1 + 2 + ... + n.

    - Si n <= 0, devuelve 0.
    - Debe resolverse usando un bucle (for o while).
    """
    if n <= 0:
        print(0)
        return 0
    suma = 0
    for i in range(1, n + 1):
        suma += i
        print(suma)
    return suma
n = 5
sum_first_n(n)
print("Suma total es:", sum_first_n(n))