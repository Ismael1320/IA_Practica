while True: #Crea un bucle infinito que se ejecutará hasta que se use la instrucción break.
    
    palabra = input("Si quieres salir del bucle debes ingrsar la palabra secreta: ") #Solicita al ususario que ingrese la palbra secreta
    
    if palabra == "chupacabra" : #Verifica si la palabra ingresada es igual a la palabra seceta
         print("Has dejado el bucle con éxito.") #Muestra un mensaje indicando que el usuario salió del bucle correctamente
         break #Terminael bucle infinito cuando la palabra correcta es ingresada
     
    else: #Si la palabra ingresada no es correcta
        print("Vuelvea intentar.", end=" ") #Muestra un mensaje (sin salto de linea), para que el usuario vuelva a intentar