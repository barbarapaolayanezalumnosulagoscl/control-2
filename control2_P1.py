puntaje_diario = []

for dia in range(1, 16):
    puntaje = int(input("Ingrese el puntaje (de 1 a 100) del día: "))
    while puntaje < 1 or puntaje > 100:
        print("El puntaje debe estar entre el 1 y 100. Intentelo nuevamente.")
        puntaje = int (input("ingrese el puntaje (de 1 a 100) del día:" ))
    puntaje_diario.append(puntaje)

mayor_o_igual_60 = []
menor_a_60 = []

for dia in range(1, 16):
    puntaje = puntaje_diario[dia - 1]
    if puntaje >= 60:
        mayor_o_igual_60.append(dia)
    else:
        menor_a_60.append(dia)

print("Días con puntaje mayor o igual a 60:")
for dia in mayor_o_igual_60:
    print("dia:",dia)

print("Días con puntaje menor a 60:")
for dia in menor_a_60:
    print("dia:",dia)