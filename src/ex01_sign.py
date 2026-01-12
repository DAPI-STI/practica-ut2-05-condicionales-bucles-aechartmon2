"""
Ejercicio 1:
Clasifica un número como positivo, negativo o cero.
"""

def sign(n: int) -> str:
    """
    Devuelve:
    - "positivo" si n > 0
    - "negativo" si n < 0
    - "cero" si n == 0
    """
    if n > 0:
        print("positivo")
        return "positivo"
    elif n < 0:
        print("negativo")
        return "negativo"
    elif n == 0:
        print("cero")
        return "cero"
    raise ValueError ("no válido")
sign(8)
sign(-8)
sign(0)
