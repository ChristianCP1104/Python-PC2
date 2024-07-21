def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("El número debe ser un entero no negativo.")
    
    if n == 0:
        return 1
    
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    
    return resultado

numero = 5
print(f"El factorial de {numero} es: {factorial(numero)}")