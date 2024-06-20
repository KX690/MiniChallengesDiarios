palabra= input("Introduzca una palabra: ")
palabra= palabra.lower()
tamanio = len(palabra)
contador=0
arreglo = [0,0,0,0,0]
for i in range(tamanio-1):
    match palabra[i]:
        case "a":
            arreglo[0]+=1
            contador+=1
        case "e":
            arreglo[1]+=1
            contador+=1
        case "i":
            arreglo[2]+=1
            contador+=1        
        case "o":
            arreglo[3]+=1
            contador+=1
        case "u":
            arreglo[4]+=1
            contador+=1
print(f"Existen: {arreglo[0]} - a ")    
print(f"Existen: {arreglo[1]} - e ")
print(f"Existen: {arreglo[2]} - i ")
print(f"Existen: {arreglo[3]} - o ")
print(f"Existen: {arreglo[4]} - u ")
print(f"Posee un total de {contador} vocales")