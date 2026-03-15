beatles = [] #Se crea una lista vacía donde se gurdarán los nombres de los integrantes de la banda
print("Paso 1:", beatles) #Muestra la lista vacía del inicio.

beatles.append("John Lennon") #Se guarda el nombre de "John Lennon" al final de la lista.
beatles.append("Paul McCartney") #Se guarda el nombre de "Paul McCartney" al final de la lista.
beatles.append("George Harrison") #Se guarda el nombre de "George Harrison" al final de la lista.
print("\nPaso 2:", beatles) #Muestra la lista después de agregar tres integrantes.

for i in range(2): #Crea un ciclo que se ejecutará dos veces para agregar dos integrrantes más.
    nuevo = input("\nIngrese a 2 miembros de la banda: ") #Solicita la usuario el nombre de un integrante.
    beatles.append(nuevo) #Agrega al nuvo integrante al final de la lista.
    
print("\nPaso 3:", beatles) #Muestra la lista después de agregar a los nuevos integrantes.

del beatles[3] #Elimina el elemento en la pocisión 3 de la lista.
del beatles[3] #Elimina el elemento en la pocisión 3 de la lista (porque la lista se reacomoda).
print("\nPaso 4:", beatles) #Muestra la lista después de eliminar a esos integrantes.

beatles.insert(0,"Ringo Starr") #Inserta a "Ringo Starr" al inicio de la lista (pocisión 0).
print("\nPaso 5:", beatles) #Muestra la lista final con todos los integrantes correctos.


print("\nLos Fav", len(beatles)) #Muestra la cantidad total de integrantes en la lista.