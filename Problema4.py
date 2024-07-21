alumnos = []

n = int(input("Ingrese la cantidad de alumnos: "))

for i in range(n):
    nombre = input(f"Ingrese el nombre del alumno {i + 1}: ")
    
    notas = []
    
    for j in range(3):
        while True:
            try:
                nota = float(input(f"Ingrese la calificación {j + 1} del alumno {nombre}: "))
                notas.append(nota)
                break
            except ValueError:
                print("Por favor, ingrese una calificación válida (número).")
    
    alumno = {
        "Alumno": nombre,
        "Notas": notas
    }
    
    alumnos.append(alumno)

print("\nListado completo de alumnos y sus calificaciones:")
for alumno in alumnos:
    print(f"Alumno: {alumno['Alumno']}, Notas: {alumno['Notas']}")