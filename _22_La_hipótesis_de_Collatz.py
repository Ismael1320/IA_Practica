c0 = int(input("Ingrese un numero entero que no sea cero o un numero negativo: ")) #Solicita al usuario que ingrese un número entero positivo. 

pasos=0 #Variable que contará cuantos pasos se realizan en el proceso.

while c0 <= 0: #Verifica que el numero ingresado no cero ni negativo
    
    c0 = int(input("Ingrese un valor diferente: ")) #Si el número no es válido, pide otro valor.

while c0 != 1: #El ciclo se ejecuta hasta que el valor de c0 sea igual a 1.
    
    if c0 % 2 == 0: #Verifica si el número es par.
        
        c0 = c0//2 #Si es par, se divide entre 2usando división entera.
        
    else: #Si el numero es impar.
        
        c0 = 3*c0+1 #se aplica la formula 3n+1.
        
    print(c0) #Muestra el numero actual después de aplicar la operación.
    pasos +=1 #Incrementa el número de pasos en 1.
    
print("Número de pasos: ",pasos) #Muestra el total de pasos realizados hasta llegar a 1.