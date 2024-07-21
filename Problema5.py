def es_primo(n):
    """Función para verificar si un número es primo."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def suma_primos_menores_100():
    """Función para calcular la suma de todos los números primos menores que 100."""
    suma = 0
    for num in range(2, 100):
        if es_primo(num):
            suma += num
    return suma

resultado = suma_primos_menores_100()
print("La suma de todos los números primos menores que 100 es:", resultado)