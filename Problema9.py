def eliminar_vocales(texto):
    vocales = "aeiouAEIOU"
    resultado = []

    for caracter in texto:
        if caracter not in vocales:
            resultado.append(caracter)
    
    return ''.join(resultado)

entrada = input("Ingrese una cadena de texto: ")

salida = eliminar_vocales(entrada)

print("Texto sin vocales:", salida)