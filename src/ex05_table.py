"""
Ejercicio 5:
Tabla de multiplicar.
"""

def multiplication_table(n: int) -> list[int]:
    """
    Devuelve una lista con 10 elementos:
    [n*1, n*2, ..., n*10]
    """
    table = []
    for i in range(1, 11):
        table.append(n * i)
        print(table)
    return table

result = multiplication_table(8)
print("Tabla de multiplicar es:", result)
