texto = input("Pone un texto :")

cuantas = 0

for letra in texto:
    if letra == "a":
        cuantas +=1
        
print("La letra a esta ",cuantas," veces en el texto")