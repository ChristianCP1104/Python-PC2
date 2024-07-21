fibonacci = [0, 1]

while True:
    siguiente_numero = fibonacci[-1] + fibonacci[-2]
    if siguiente_numero > 50:
        break
    fibonacci.append(siguiente_numero)

print("Serie de Fibonacci entre 0 y 50:")
print(fibonacci)