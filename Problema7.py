def divisores_propios(numero):
    divisores = []
    for i in range(1, numero):
        if numero % i == 0:
            divisores.append(i)
    return divisores

def es_numero_perfecto(numero):
    return sum(divisores_propios(numero)) == numero

numeros_perfectos = []

for num in range(1, 1000):
    if es_numero_perfecto(num):
        numeros_perfectos.append(num)

print("Números perfectos menores que 1000:")
print(numeros_perfectos)