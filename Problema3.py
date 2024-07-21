pares = 0
impares = 0

while True:
    numero = input("Ingrese un número (o escriba 'no' para detenerse): ")
    
    if numero.lower() == 'no':
        break
    
    try:
        numero = int(numero)
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue
    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")