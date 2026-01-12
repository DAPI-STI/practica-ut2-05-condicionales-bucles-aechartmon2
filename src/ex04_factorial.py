"""
Ejercicio 4 (un poco más complejo):
Factorial de un número.
"""

def factorial(n: int) -> int:
    """
    Devuelve n! (n factorial).

    Reglas:
    - 0! = 1
    - Si n < 0, lanza ValueError.
    - Debe resolverse usando un bucle (no recursión).
    """
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    elif n == 0:
        print(1)
        return 1 
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        print(resultado)
        return resultado
    factorial = factorial(8)
factorial(8)
