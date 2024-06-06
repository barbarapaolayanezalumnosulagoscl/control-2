palabras = []

while True:
    palabra = input("Ingrese una palabra (No escriba nada y presione enter es para finalizar): ")
    if not palabra:
        break
    palabras.append(palabra)

longitud_max = 0

for palabra in palabras:
    longitud_actual = len(palabra)
    if longitud_actual > longitud_max:
        longitud_max= longitud_actual

print("La palabra más larga tiene", longitud_max, "caracteres.")
