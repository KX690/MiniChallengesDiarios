lista=[]


print("Introduzca 7 numero de cualquier valor: ")

for i in range(7):
    numero=int(input(f"Introduzca el numero {i+1}: "))
    lista.append(numero)
for j in range(7):
    for i in range(6):
        if (lista[i]>lista[i+1]):
            aux=lista[i]
            lista[i]=lista[i+1]
            lista[i+1]=aux
        
print(lista)