nombres = []

while True:
    nombre = input("Ingrese un nombre (o 'fin' para terminar): ")
    
    if nombre == "fin":
        break
    
    nombres.append(nombre)


nombres.sort()
print("Lista ordenada:", nombres)

contador = 0
for n in nombres:
    if n.startswith("A") or n.startswith("E"):
        contador += 1

print("Nombres que empiezan con A o E:", contador)

buscar = input("Ingrese un nombre para buscar: ")

if buscar in nombres:
    print("El nombre está en la lista")
else:
    print("El nombre no está en la lista")
