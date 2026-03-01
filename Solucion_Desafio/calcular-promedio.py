suma = 0

name = str(input("Hola, bienvenido, cuál es su nombre?: "))

print(f"Hola {name}, bienvenido al sistema de calificaciones, por favor ingresa tus calificaciones")

for i in range(5):
    while True:
        try:
            grade = int(input(f"Ingresa la calificación {i + 1}: "))
            if 0 <= grade <= 100:
                suma += grade
                break
            else:
                print("La calificación debe estar entre 0 y 100. Inténtalo de nuevo.")
        except ValueError:
            print("Ingresa una calificación válida (número).")

promedio = suma / 5

print(f"{name}, tu promedio de calificaciones es: {promedio: }")

if promedio >= 60:
    print("¡Felicidades! Has aprobado")
elif 59 >= promedio >= 40:
    print("Estás en recuperación, no te rindas")
elif promedio < 40:
    print("Lo siento, has reprobado")