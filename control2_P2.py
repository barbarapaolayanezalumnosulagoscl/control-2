nombres = []

for i in range(7):
    nombre = input("Ingrese un nombre de persona: ")
    nombres.append(nombre)

nombres_que_terminan_con_a = [nombre for nombre in nombres if nombre[-1] == "a"]

print("Nombres que terminan con 'a':", nombres_que_terminan_con_a)
