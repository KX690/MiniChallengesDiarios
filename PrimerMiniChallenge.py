palabra = input("Introduzca una palabra que le gustaria ver del reves: ")
tamanio = len(palabra)
palabra_invertida=""
for i in range (tamanio-1 , -1 ,-1):
    palabra_invertida = palabra_invertida + palabra[i] 
    
print(palabra_invertida)